#Linux 

# **Cos'è?**
>Samba è un software che implementa il protocollo SMB/CIFS su Linux, permettendo la condivisione di file e stampanti in rete.

>Opera a livello di utente di sistema e permessi di filesystem (POSIX)

>Ma anche a livello applicativo attraverso credenziali e policy definite nel database TDB di Samba (smbpasswd)

---
# **Installazione**

>Pacchetti da installare:
>- samba, server principale che include il deamon (smbd) e nmbd(risoluzione nomi)
>- smbclient, client a riga di comando per eseguire test locali

```shell
sudo apt update
sudo apt install samba
```

>I file di configurazione si trovano in **/etc/samba**

>smb.conf
```shell
[global]  #configurazioni che si applicano all'intero server
server string = File Server #Nome server / Descrizione
workgroup = WORKGROUP       #gruppo di lavoro / dominio su windows
security = user             #Bash 
map to guest = Bad User           #chi si connette non ha bisogno di un utente
name resolver order = bdcast host #
include = /etc/samba/shares.conf
```

>shares.conf (Cartelle condivise)
```shell
[Pubblica]   #Nome che si vedrà in rete della cartella
path = /share/public_files   #path alla directory da condividere
force user = smbuser         # 
force group = smbgroup
create mask = 0664
create mode = 0664
directory mask = 0775
force directory mode = 0775
public = yes
writable = yes

[Protetti]   #Nome che si vedrà in rete della cartella
path = /share/protect_files   #path alla directory da condividere
force user = smbuser         # 
force group = smbgroup
create mask = 0664
create mode = 0664
directory mask = 0775
force directory mode = 0775
public = yes
writable = no
```

>Creazione del gruppo con cui condivideremo le cartelle
```shell
sudo groupadd --system smbgroup

sudo useradd --system --no-create-home --group smbgroup -s /bin/false smbuser
```

>Cambiare gli owner e i permessi delle cartelle:
```shell
sudo chown -R smbuser:smbgroup /share
sudo chmod -R g+w /share
```
---
# **Struttura**
>Samba non può concedere più permessi di quanto ne consenta il sistema operativo (POSIX)

>La directory che ospita le condivisioni, **/srv/samba**:
>- /srv/samba/pubblica
>- /srv/samba/personale
>- /srv/samba/altra-cartella
>- ecc...

>Ogni cartella dovrà avere la propria configurazione che abilita solo chi di dovere a leggere/scrivere in quello spazio (comprese le sottocartelle).

>Per fare questo sul filesystem Linux usa un permesso speciale chiamato **SGID (Set Group ID)**

---
