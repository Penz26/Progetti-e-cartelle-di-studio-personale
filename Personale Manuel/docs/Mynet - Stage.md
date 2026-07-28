
# ==***07/07/2026***==
## Imap e Smtp

>Imap (Internet Message Access Protocol):
>protocollo per gestire la ricezione e la sincronizzazione della posta su più dispositivi

>Smtp (Simple Mail Transfer Protocol):
>protocollo standard utilizzato dai client di posta per inviare


## Samba file server
>Samba è un software open source che permette di condividere file e stampanti all'interno di una stessa rete


## Ansible [[Ansible]]
>Ansible è un tool di automazione IT open source che semplifica la configurazione dei server, il deployment delle applicazione e la gestione dell'infrastruttura.

>Sulla macchina principale (nodo) risiede il software mentre le macchine remote non necessitano di agenti dedicati. La comunicazione avviene tramite canali sicuri e standard come SSH.
>
>Tramite i **playbook** Ansible stabilisce lo stato desiderato dell'infrastruttura. E' idempotente, ovvero ripete l'azione solo se necessario per evitare modifiche accidentali o indesiderate.

- inventario
- playbook
- ruoli

---
# ==***08/07/2026***==
## Aggiornamento server mail
>E' stata rilasciata una nuova versione di un client web  che patcha determinate vulnerabilità

1. Controllare le CVE e cosa effettivamente veniva fixato
2. Entrati ssh sulla vm con il servermail
3. controllata versione installata e su cosa si girasse e su che webserver (apache o ngnix) sudo apt policy nome_pacchetto
4. Entrati nelle configurazione /etc/nginx/sites-enabled che ci diceva il path dove sono contenuti il software
5. Scaricato ed estratto il pacchetto
6. FATTO BACKUP dell'attuale database e dei file della versione precedente del software
```sh
   pg_dump nome_database > path/file/di/salvataggio
   stessa roba per altri db
   
   --- Oppure se fosse stato un altro DB ci sarebbero comandi come: ---
   mysqldump
   
   cp -Ra html html_1.6.16
```
7.  Controllare che sia andato tutto liscio

## **Pulizia dischi rigidi e ssd**

## **shred (dischi HDD)**
>Sovrascrive il disco più volte con dati casuali per rendere impossibile il recupero magnetico ed infine scrive una passata finale di zeri per nascondere il processo
```sh
sudo shred -v -n 3 -z /dev/sdX
-v: verbose
-n 3: esegue 3 passaggi di sovrascrittura con dati casuali
-z: esegue un ultima passata scrivendo solo zeri
/dev/sdX: HDD di cui eseguire la sovrascrittura
```

**blkdiscard (SSD)**
>Ripulisce velocemente senza passare dai controller. Questo comando invia un segnale TRIM a ogni blocco del disco dicendo al controller che tutte le celle sono vuote. In questo modo (visto che blkdiscard non esegue cicli di scrittura) preserviamo anche l'integrità dei dischi
```sh
sudo blkdiscard -v /dev/sdX
```

## **dmesg**
>Legge le chiamate del kernel

## **dd**
>Riempe l'intero disco di zeri
```sh
sudo dd if=/dev/zero of=/dev/sdX bs=4M status=progress

if=/dev/zero : #la sorgente dei dati
of=/dev/sdX : #il disco di destinazione
bs=4M : #scrive in blocchi da 4 Megabyte per velocizzare il processo
status=progress : #mostra la velocità e il tempo rimanente
```

>Può anche essere usato per flashare delle  ISO su una chiavetta
```sh
sudo dd if=percorso/file.iso of=/dev/sdX bs=4M status=progress conv=fdatasync

if=percorso/file.iso : #è la sorgente (il file ISO che si ha scaricato)
of=/dev/sdX #la destinazione (chiavetta USB)
bs=4M #velocità di scrittura
status=progress #mostra in tempo reale quanti dati sono stati scritti e la velocità di trasferimento
conv=fdatasync : #costringe linux a svuotare la cache e scrivere fisicamente l'ultimo bit prima di chiudere il comando
```

---
# ==***09/07/2026***==

dns autoritativi, record dns, tipi di dns

generari chiavi ssh, usare passphrase per la chiave per proteggerla

## Fatta procedura esplicativa di come applicare la firma digitale (file .htm)

>1. Entrato con remmina in una VM Windows10 per fare le prove con Outlook.
>2. Scaricato il file in estensione .htm della firma digitale dell'azienda
>3. Inserito il file nella cartella "%AppData%\Microsoft\Signatures\"
>4. Andare in File, Options, Mail, SIgnatures, e mettere come firma di ricezione e risposta

## **Aggiornamento di Zone dns sul server dns Mynet**
>Abbiamo dovuto cambiare le configurazioni delle zone DNS di alcuni clienti.

==**Fatto un snapshot del server dns in caso venga cambiato qualcosa in modo errato**==
- Procedura 
1. Sanificato campi TXT che non erano conformi agli standard (il testo andava messo tra "")
2. Cambiato il SOA (Start of Authority) per far sì che d'ora in poi il dominio principale venga risolto dal dns autoritativo di Mynet con il suo TTL, Serial, Refresh, Retry, Expiry e Minimum TTL
3. Cambiati i due record dns (record NS) così che il dominio venga gestito dal server dns di Mynet
4. Controllati eventuali errori
5. Entrare nel server dns in ssh (con utente abilitato a usare solo determinati comandi come sudo)
6. Usati comandi:
```sh
--- zona = dominio principale ---
--- zona.txt = file di configurazione dns ---

pdnsutil load-zone <zona> <zona.txt> 
#Importa tutti i record direttamente nel database di PowerDNS assegnandoli al dominio <zona>

pdnsutil check-zone <zona>
#Fa la stessa identica cosa di named-checkzone in BIND. Analizza la zona importata nel database per verificare che non ci siano errori sintattici

pdnsutil set-kind <zona> master
#Dice a PowerDNS che questo server dns dove attualmente si è loggati è il master ovvero il primario, significa che se ci sono altri server DNS dovranno recuperare le info da lui

pdnsutil set-meta <zona> SOA-EDIT-API-DEFAULT
#Questa regola dice a PowerDNS che ogni volta che si cambia un record tramite API aggiorna e incrementa il Serial del SOA in automatico
```

---
# ==***10/07/2026***==
>Diagnostica su un server Hp Ceph guasto

## Cos'è Ceph:
>Ceph è un sistema di archiviazione distribuito che fornisce servizi di archiviazione oggetti blocchi e file da un singolo cluster

>Dopo una giornata passata a sovrascrivere gli hard disk con dati randomici abbiamo seguito la procedura cercando di capire cosa effettivamente non andasse sul server.

## **1° Osservazione**
>Attraverso l'ILO (software embedded per la gestione da un altro PC collegato con un cavo RJ45 del server con interfaccia grafica) abbiamo trovato i dati seriali dei vari dischi.
>Questi dati sono stati comparati con quelli che ricevevamo con
```sh
sudo dmesg -T | grep -E -i "io error|failed|bad sector|rejecting I/O|buffer i/o" | awk '{print$6}' | sort | uniq
```

>Questo comando ci riportavo il disco (la sesta colonna del dmesg $6)che dava problemi ("io error ...) una sola volta (sort | uniq ci permette di vedere il disco una sola volta invece che per ogni errore che hanno mai dato)

>All'inizio i dischi che davano errore sembravano essere solo quelli nella cage anteriore. Per riprovare abbiamo spostato altri dischi sulla prima cage e anche loro davano problemi.

>Di conseguenza abbiamo pensato che il problema fosse dell'intero 1° cage (primi 12 dischi).

## **2° Osservazione**
>Dopo abbiamo provato con un altro metodo per verificare se effettivamente fosse un problema del cage o del controller o dei cavi.

>Dopo aver spostato i cavi Sas abbiamo notato che non davano più problemi i dischi davanti ma bensì quelli dietro (2° Cage).
>I cavi partivano dal controller in un unico posto da due da 8 che si divideva in 4 cavi da 2 Sas. 
>2 andavano alla prima cage
>gli altri 2 andavano alla seconda cage ed uno dei due tornava indietro per tornare alla scheda madre.

>Di conseguenza abbiamo stabilito che il problema non era nella posizione dei dischi ma bensì nei cavi del controller che saranno da sostituire e controllare per eventuali danni smontando il case del server.

---

# ==***13/07/2026***==

1. Prova di configurazione di un profilo di rete per un nuovo utente (IO)
2. Rinnovo certificati ssl (CA godaddy) per un sito di un cliente per cui hostiamo il server web (apache2)

## **Configurazione profilo di rete**
>Una volta arrivato il mini pc che doveva fungere da workstation abbiamo provato ad aggiungere il mio utente come profilo di rete di dominio.

>Arrivati alle impostazioni la password di root del proprietario di dominio che doveva abilitarmi la connessione LAN non funzionava.

>Così abbiamo deciso di utilizzare un'istanza live di un ISO sullo stesso pc per cercare di cambiare la password di root.

>Operazioni:
>1. Flashata ISO sulla mia chiavetta con Ventoy
>2. Inserita nel pc
>3. Entrare nel BIOS e cambiato Boot Order (Secure boot già disabilitato)

>Una volta dentro abbiamo:
```sh
sudo -i # Per diventare root per la sessione

lsblk   #Per vedere i dischi e capire la partizione su cui operare (nvme0n1p3)

cryptsetup luksOpen /dev/nvme0n1p3 cryptroot
```

>Abbiamo notato che il disco fosse protetto da crittografia LUKS.  Inserita la passphrase dopo lo sblocco comparirà la tipologia di filesystem (ext4)

```sh
sudo mount /dev/mapper/cryptroot /mnt
```

>Abbiamo poi montato i principali file del sistema per poterci entrare con chroot:
```sh
sudo mount --bind /dev /mnt/dev
sudo mount --bind /dev/pts /mnt/dev/pts
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo mount --bind /run /mnt/run

#Dopo aver copiato tutti i file che servivano abbiamo usato chroot per entrarci

sudo chroot /mnt

#Per vedere che utenti ci siano in quel sistema
ls /home

#una volta identificato l'utente amministratore cambiata la password con

passwd nome_utente

#Una volta cambiata la password controllare che essa sia stata salvata abbiamo guardato il file /etc/shadow che mantiene le password in modo criptato

ls /etc/shadow
```

>Usciti abbiamo riprovato ma non ha funzionato :(

---
## **Rinnovo certificati SSL su un server web apache2**

>Il sito di un nostro cliente aveva i certificati ssl che garantivano l' Https del sito in scadenza.

>Abbiamo proceduto ad individuare i file di configurazione del Virtualhost del sito in
>**/etc/apache2/sites-enabled**

```html
<VirtualHost *:80>
    ServerName il-tuo-sito.it
    ServerAlias www.il-tuo-sito.it

    # 🛠️ Attivazione e regole di riscrittura (HTTP -> HTTPS)
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

    ErrorLog ${APACHE_LOG_DIR}/http_error.log
    CustomLog ${APACHE_LOG_DIR}/http_access.log combined
</VirtualHost>
<VirtualHost *:443>
    ServerName il-tuo-sito.it
    ServerAlias www.il-tuo-sito.it
    DocumentRoot /var/www/html/wordpress

    #Attivazione del motore SSL
    SSLEngine on

    #1. Certificato principale del dominio (scaricato da GoDaddy)
    SSLCertificateFile /etc/apache2/certificates/sito.crt

    #2. Chiave privata associata alla richiesta CSR
    SSLCertificateKeyFile /etc/apache2/certificates/sito.key

    #3. Bundle intermedio di GoDaddy (es. gd_bundle-g2-g1.crt)
    SSLCertificateChainFile /etc/apache2/certificates/gd_bundle.crt

    <Directory /var/www/html/wordpress>
        Options FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

>Abbiamo trovato la directory in cui tenevamo i certificati ssl, abbiamo fatto un backup di questi vecchi ed abbiamo scaricato i certificati nuovi con godaddy dalla gestione dei nostri prodotti.

>Una volta scaricati i file dei nuovi certificati abbiamo mandato i file al nostro server tramite scp:
```sh
scp sito.crt utente@indirizzo_ip_server:/tmp/
```

>E da lì li abbiamo spostati nella cartella specificata in VirtualHost entrando in ssh al server

>Una volta fatto ciò abbiamo fatto 2 controlli finali:

1. Controllo della sintassi sul file di configurazione con il comando
```sh
sudo apachectl -t

#oppure su sistemi debian
sudo apache2ctl configtest
```

2. Ricaricato il servizio Apache2
```sh
sudo systemctl reload apache2
```

>Fatto questo ci basterà cercare sul browser il dominio per cui abbiamo aggiornato i certificati e guardare con l'icona del lucchetto la CA emittente e la data di scadenza del certificato.

---
# ==***14/07/2026***==

>Continuato studio di Ansible [[Ansible]]
>- Ruoli
>- modulo package
>- gruppi, 
>- variabili di gruppo, 
>- vault Ansible
>- tag,
>- services

## Task per il futuro:
- Finire di studiare i ruoli e template
- Controllare possibilità di automazione di Proxmox collegando Ansible
- Guardare NetBox (e la relativa implementazione con Ansible)

---

# ==***15/07/2026***==

>Studiato come implementare Ansible con Netbox e Proxmox [[Automazione Netbox ---> Proxmox via Ansible]]

>Creata documentazione a riguardo, continuata implementazione con gli appunti.

---
# ==***16/07/2026***==

>Continuato studio dell'implementazione tra i 3 tool


---
# ==***17/07/2026***==

>Aggiunti record per delle macchine su Netbox

# ==***20/07/2026***==
>Installato nuovo controller per il server di cui avevamo fatto la diagnosi i primi giorni

## **Repository Debian/Ubuntu con aptly e firme GPG** [[aptly Repository Debian-Ubuntu]]
---

# ==***21/07/2026***==
>Continuato lavoro della repository locale ubuntu, ora funziona in TLS

---
# ==***22/07/2026***==
>Continuato lavoro della repository locale ubuntu, ora funziona in mTLS , snapshot di istanze aptly niziato basic auth con password

---
# ==***23/07/2026***==
>Il server Aptly funziona con basic auth, iniziato a studiare [[Cos'è Gitlab]].

---
# ==***24/07/2026***==
>Continuato con Gitlab, installazione su macchina del server con prime configurazioni e test per il server aptly per un flusso CI/CD.

---
# ==***27/07/2026***==
>Continuato lavoro repository CI/CD, spostato su container Docker per compilazione più pulita. Separato spazio di compilazione e di pubblicazione. Unico runner che compila in un container docker dentro una VM. Sposta i file tramite SCP e poi si collega in ssh sul server aptly con un utente abilitato solamente ai comandi aptly.

>Flashati Google Pixel 9a e 10a con GrapheneOS seguendo wiki 
>[Documentazione Installazione CLI per GrapheneOS](https://grapheneos.org/install/cli)

---


# ==***28/07/2026***==
>Automazione con GitLab CI/CD + Docker.
>- Finalizzato connessioni ssh ed scp senza password,
>- configurazione di rete per docker,
>- configurazione del runner per usare docker come executor,
>- 