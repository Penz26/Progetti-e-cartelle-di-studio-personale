#Proxmox 

# **Cos'è?**
>Il fratello di Proxmox VE ma solamente per i backup

Proxmox Backup Server (PBS) permette di passare da:
- un **Backup Tradizionale** con il quale ad ogni esecuzione crea una copia completa per le VM e i container **==🔴anche se non cambia nulla==** . Questo comporta alla scrittura di dati uguali più volte.
a dei
- **Backup Incrementali** utilizzando la **deduplicazione** in cui i dati vengono spezzati in piccoli blocchi (circa 4MB) identificati da un hash crittografico SHA-256.
  Al primo backup vengono scritti tutti i blocchi mentre al secondo verranno scritti solamente quelli modificati

---
# **Come si installa**
>Al momento della scrittura di questa nota la versione attuale supportata è Proxmox Backup Server 4

Ci sono 2 metodi:
1. attraverso la ISO su un nodo apposta per poi poterlo mettere in cluster
2. tramite un pacchetto APT debian 13 (trixie)

Per motivi di povertà personale affronteremo l'installazione e la configurazione tramite pacchetto APT

---
# **Creazione della macchina virtuale**

Proxmox backup Server 4 necessita delle seguenti specifiche:
- Debian 13 come template
- 2 core
- 2gb di ram
- 16gb di memoria

>[!NOTE] Siccome girerà sullo stesso proxmox di cui si occuperà di fare i backup dovremo dargli la possibilità di scrivere i backup sul disco/directory in cui andremo a salvarli.

Per farlo dobbiamo:
1. identificare quale sia il disco/directory in cui salvare i backup
2. montarlo sulla macchina appena creata per PBS

>I dischi e le directory su Proxmox si possono vedere nella directory /mnt/pve/NOMEDISCO
```bash
ls /mnt/pve/NOMEDISCO
```

>Mentre le configurazioni delle singole macchine e container si trovano in /etc/pve/
```bash
ls /etc/pve/lxc # per i container
```

---
# **Preparazione Ambiente**

>Creiamo la directory dedicata al datastore sul disco fisic
```bash
mkdir -p /mnt/pve/NOMEDISCO/NOMEDIRECTORY
```

>La cartella dovrà avere come owner lo **user backup (UID 34)** **==🔴MA==** essendo PBS dentro un container non privilegiato dobbiamo sommare all' UID 100'000 (shift di sicurezza applicato da proxmox)
```bash
chown -R 100034:100034 /mnt/pve/NOMEDISCO/NOMEDIRECTORY
chmod 770 -R /mnt/pve/NOMEDISCO/NOMEDIRECTORY
```

>All'interno del file del container che vogliamo modificare (es. 106.conf) andremmo ad aggiungere questa riga:
```bash
#Diciamo di prendere come mount point /mnt/pve/NOMEDISCO e di montarlo sulla macchina come /mnt/datastore
mp0: /mnt/pve/NOMEDISCO/NOMEDIRECTORY,mp=/mnt/datastore
```

---
# **Installazione**

```bash
# 1. Scaricamento della chiave GPG ufficiale di Proxmox per Debian 13 (Trixie)
wget https://enterprise.proxmox.com/debian/proxmox-archive-keyring-trixie.gpg -O /usr/share/keyrings/proxmox-archive-keyring.gpg

# 2. Configurazione del repository gratuito (pbs-no-subscription) in formato deb822
cat << 'EOF' > /etc/apt/sources.list.d/pbs-no-subscription.sources
Types: deb
URIs: http://download.proxmox.com/debian/pbs
Suites: trixie
Components: pbs-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF

# 3. Aggiornamento del sistema e installazione di PBS 4
apt update && apt full-upgrade -y
apt install -y proxmox-backup-server

# 4. Rimozione del repository Enterprise di default (evita errori 401 durante futuri apt update)
rm -f /etc/apt/sources.list.d/pbs-enterprise.sources
```

---
# **Configurazione datastore, utente e API token su PBS**
>I prossimi passaggi si possono fare anche da GUI

![proxmox-backup-server][proxmox-backup-server.png]

```bash
# 1. Creazione e inizializzazione del datastore (crea le cartelle .chunks e il file .lock)
proxmox-backup-manager datastore create NOME-DATASTORE /mnt/datastore

# 2. Creazione dell'utente dedicato a Proxmox VE
proxmox-backup-manager user create NOME-UTENTE@pbs

# 3. Generazione dell'API Token (da segnarsi il token, servirà per collegare PBS a PVE)
proxmox-backup-manager user generate-token NOME-UTENTE@pbs NOME-TOKEN

# 4. Assegnazione dei permessi (Ruolo DatastoreAdmin) sia all'utente che all'API Token
proxmox-backup-manager acl update /datastore/local-backups DatastoreAdmin --auth-id 'NOME-UTENTE@pbs'
proxmox-backup-manager acl update /datastore/local-backups DatastoreAdmin --auth-id 'NOME-UTENTE@pbs!NOME-TOKEN'

# 5. Lettura del Fingerprint SHA-256 del certificato SSL di PBS
proxmox-backup-manager cert info | grep Fingerprint
```

---
# **Collegamento dello storage e Job di Backup su Proxmox VE**

>Per aggiungere il datastore che abbiamo creato per PBS a PVE basta andare su
>**Datacenter --> Storage --> Add -->Proxmox Backup Server**
- **ID**: (nome a piacere che spunterà nella UI)
- **Server**: IPSERVERPBS
- **User name**: NOME-UTENTE@pbs!NOME-TOKEN
- **Password**: **==🔴TOKEN SEGRETO==**
- **Datastore**: NOME-DATASTORE
- **Fingerprint**: Fingerprint del certificato SSl di PBS

>[!IMPORTANT] Una volta fatti questi passaggi si vedrà in basso a sinistra tra i dischi spuntare anche il datastore di PBS

>Nel job di Backup programmati in **Datacenter --> Backup** bisognerà mettere:
1. Storage di destinazione: NOME-DATASTORE
2. **==🔴escludere la macchina su cui gira PBS==** 
3. **Settare la retention dei backups**
4. **Nella sezione avanzate in basso PBS change Detection Mode** mettere **==🔴Metadata==**

>Differenze tra le modalità di change Detection Mode:
- **Default**: legge per intero il contenuto di tutti i file del container, calcola gli hash e invia solo i blocchi nuovi (costringe il disco a leggere tutti i gigabyte ad ogni backup)
- **Data**: Separa metadati e dati in flussi diversi, ma legge comunque per intero tutti i file
- **MetaData**: Confronta solo i metadati dei file con quelli del backup precedente. Se un file non risulta modificato non lo legge nemmeno e i suoi dati non vengono rimandati

---
# **Ciclo di vita dei dati su PBS**

## **Prune**
>- Cancella la voce dei backup più vecchi della retention applicata
>- Rimuove il backup dalla lista **ma non libera lo spazio sul disco**

>Viene gestito in automatico dal Job di backup di PVE

## **Garbage Collection**
>- Scansiona la cartellla .chunks e cancella dal disco tutti i dati che non sono più referenziati in alcun backup attivo


>[!IMPORTANT] Questi 2 passaggi devono essere fatti in momenti diversi rispetto al momento di Backup, solitamente 48 ore dopo.

## **Verify Job**
>- Rilegge i blocchi salvati sul disco, ricalcola l'hash SHA-256 e verifica che coincida con quello registrato, individuando così eventuali settoei corrotti sul disco
