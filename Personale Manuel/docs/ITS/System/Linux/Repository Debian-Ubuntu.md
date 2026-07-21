#Linux 

# **Che cos'è una Repository Debian/Ubuntu?**

>Una repository in generale è il magazzino dove sono conservati tutti i software, programmi e gli aggiornamenti per un sistema operativo.
>Quando si prova ad installare un software su debian/ubuntu il nostro package manager funge da commesso che:
>- controlla che noi non abbiamo già questo software
>- controlla e aggiorna la lista degli indirizzi di dove trovare l'oggetto
>- contatta il server che ha il software (verifica che sia autentico con una chiave GPG) e scarica il pacchetto il formato .deb
>- successivamente lo passa al sistema che lo installa e configura le dipendenze necessarie.
 
---

# **La Struttura**
>Una repository è semplicemente un server web (come Apache o nginx) che ospita una struttura di cartelle pubblica e ben definita.

>All'interno troveremo due cartelle principali:
>1. **pool/:** all'interno ci sono i file fisici dei programmi, ovvero i pacchetti .deb. Ogni lettera ha la sua sottocartella in cui ogni programma ha la sua sottocartella con le sue varie versioni disponibili.
>2. **dists/:** Contiene i file indice (metadati). Dice al package manager quali pacchetti sono disponibili, quali sono le loro versioni, le dipendeze e il percorso esatto per trovarli dentro **pool/**.

>Quando si esegue il comando:
```sh
sudo apt update
```
>Non si fa altro che dire al package manager di scaricare la mappa aggiornata della cartella dists/

>Il sistema controlla i suoi file di configurazione locali (/etc/apt/sources.list.d) per vedere dove si trova il magazzino (URL del server)

>Su arch sarebbe un poco diverso (/etc/pacman.d/arch-mirrorlist) e non sono categorizzati in base alla lettera ma ci sono direttamente tutti i file all'interno ammassati

>Esempio organizzazione di una repository debina/ubuntu:

![[repo_ubuntu.png]]

>pool/:
![[pool.png]]

>dists/:
![[dists.png]]

---
# **File all'interno**

>I pacchetti che scarichiamo da queste repositories non sono semplici eseguibili e sono sempre formati da 3 componenti fondamentali:

1. **I File del programma**
   >I binari, i file di configurazione di default, le icone e la documentazione che verranno copiati nelle cartelle del sistema
   
2. **I Metadati**
   >Un file di testo che descrive il pacchetto. Nome, versione, pacchetto e l'elenco delle dipendenze 
  
3. **Script di manutenzione**
   >Piccoli script che vengono eseguiti automaticamente prima o dopo l'installazione o la rimozione del pacchetto

---
## **Sicurezza dei file**
>Linux usa GPG (GNU Privacy Guard) che utilizza la crittografia asimmetrica.

>**Private Key:**
>Serve a noi come amministratore per firmare il file di indice dei pacchetti (dists/)

>**Public key:**
>Serve ai client per verificare che il timbro fatto con la chiave privata sia autentico

>Come generare la chiave GPG:
```sh
gpg --full-generate-key

#Scegliere RSA, 4096 bit, scadenza a scelta (0 per non farla mai scadere), nome dell'organizzazione che sta creando la repository ed infine una passphrase per proteggerla
```

>Vedere la chiave:
```sh
gpg --list-secret-keys --keyid-format LONG

#La chiave sarà nella riga:
sec rsa4096/password_HEX 2026-07-20
```

>Esportare la chiave pubblica in un file di testo (sarà il file che distribuiamo ai client):
```sh
gpg --export --armor password-HEX > my-repo-key.asc
```

---
# **Come possiamo creare la nostra Repo?**
>Dopo aver il timbro GPG installiamo il gestore delle repository

```sh
sudo apt update && sudo apt install aptly -y
```

>Creiamo la struttura locale (nel DB di aptly) prima di operare:
>Questo comando aggiunge i metadati nel database interno (~/.aptly/db/)
```sh
aptly repo create -comment="Repository Interna Manuel Prod" -distribution="noble" -component="main" nome-repo
```

>Aggiungere un file:
>Copia i file .deb in ~/.aptly/pool/
```sh
aptly repo add nome-repo /path/al/software_1.0_amd64.deb
```

>Come rendere la repo pubblica ed accessibile:
>Prende tutto il materiale nel database, genera la mappa e crea la repository reale nella cartella ~/.aptly/public/
```sh
aptly publish repo -gpg-key="password-hex" -distribution="codename-distro" -component="main" nome-repo
```
>Distribution serve a specificare la versione del sistema per dividere gli ambienti nella struttura
>Mentre component rappresenta la categoria del software


>Per aggiornare una pubblicazione esistente dopo aver aggiunto/rimosso nuovi pacchetti .deb:
```sh
aptly publish update <distribution>  #Es. noble per Ubuntu 24.04
									 #oppure stable per pacchetti testati e                                            pronti e testing per in fase di prova
```

>Una volta lanciata la pubblicazione/aggiornamento chiederà la passphrase che si ha usato per la chiave GPG.
>Una volta inserita darà come risultato questo messaggio:

![[aptly-publish.png]]

---
# **Trasformazione del software in pacchetti Debian**
>Nell repositories aptly essendo basate su debian/Ubuntu i pacchetti dovranno essere in formato .deb per farlo useremo il tool **dpkg-deb --build**

>Una volta finito di creare il software in sè dovremo creare questa struttura per far funzionare il comando:
```
nome-software_1.0/                #Nome cartella in cui il tool andrà a cercare
|_DEBIAN/                         #Cartella speciale riservata per i metadati
|       |_control                 #Info generali del file
|
|_usr/                            #Intero percorso in cui verrà installato il sw
     |_local/
            |_bin/
                |_mio-script.sh
```

>Il file control che contiene i metadati del pacchetto dovrà avere una struttura che segue questa:
```
Package: nome-software
Version: 1.0.0
Architecture: tra amd64/86 o arm64/86 (oppure all)
Maintainer: Nome sviluppatore <email>
Description: Descrizione di cosa fa il pacchetto
```

>Ora creiamo il pacchetto .deb:
```sh
dpkg-deb --build nome-software_1.0
```

>Se non ci sono errori creerà un file chiamato mio-script_1.0.deb
---
# **Creazione dei certificati per il sito Nginx e i client**

>Prima di creare i certificati del server web e del client bisogna creare la CA (interna per questo caso) che si preoccupa di rilasciare  e firmarei certificati sia per il server web che per il client.

>[!NOTE] Ricordarsi il campo SAN (Subject Alternative Name) al momento dell'inserimento dei dati del certificato.

>OpenSSL ti apre una procedura guidata nel terminale che ti chiede in sequenza:
1. Country Name (2  lettere IT)
2. State or Province Name (Mantova)
3. Locality Name (Volta Mantovana) 
4. Organization Name (es. Nome Azienda) 
5. Organizational Unit Name (IT)
6. Common Name (e.g. server FQDN or YOUR name) (nome del dominio oppure IP)
7. Email Address


8. **Creare la CA**
```sh
openssl genrsa -aes256 -out ca.key 4096 #Crea la firma con cui la CA firmerà i certificati 
   
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
#Crea il certificato Root pubblico (il template su cui si dovranno basare gli altri)
```
2. **Certificato per il server web**
```sh
#Crea la chiave del server 
openssl genrsa -out server.key 2048 

#Usa la chiave di prima per creare la richiesta di certificato al CA
openssl req -new -key server.key -out server.csr

#Firma del certificato tramite la CA (genera anche il registro della ca, il file si chiamerà ca.srl)
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt
```
3. **Certificato per il client (Se si vuole abilitare la mutua autenticazione)**
```sh

#Crea la chiave per il client
openssl genrsa -out client.key 2048

#Crea la richiesta di certificato al CA firmando con la chiave appena creata
openssl req -new -key client.key -out client.csr

#Firma del certificato del client con la chiave della CA
openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt
```

---
# **Configurazione di Nginx per controllare  i certificati:**

>Per comodità del percorso e ordine abbiamo spostato i certificati nella cartella /etc/nginx/ssl
```.conf
server {
    listen 443 ssl;
    server_name repo.azienda.local;

    # 1. Radice dei file (Punta alla cartella che contiene i file di Aptly)
    root /var/www/apt-repo/public;
    index index.html;

    # __ 2. Configurazione SSL Standard (Il server dimostra chi è)
    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    # __ 3. Configurazione mTLS (Il server pretende di sapere chi è il client)
    ssl_client_certificate /etc/nginx/ssl/ca.crt; # La CA aziendale di cui Nginx si fida
    #ssl_verify_client      on;               # Forza la mutua autenticazione

    # __ 4. Permetti il browsing delle cartelle (APT ne ha bisogno)
    location / {
        autoindex on;
        try_files $uri $uri/ =404;
    }
}
```

>Una volta finita la configurazione linkare/spostare/copiare il .conf ai siti abilitati:
```shell
ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/.
```

>Fare il check della sintassi:
```shell
nginx -t
```

>Se la sintassi è ok allora fare il reload delle configurazioni:
```shell
systemctl reload nginx
```

---
# **Installazione della chiave GPG della repo sul client**
>Nelle nuove versioni di Ubuntu (dalla 22.04) il vecchio comando apt-key add è stato discontinuato per motivi di sicurezza.

>Ora le chiavi gpg non vengono aggiunte ad un unico grande file globale (/etc/apt/trusted.gpg) invece la singola chiave di una repository viene salvata nel proprio file in /etc/apt/keyrings/nome-repo.gpg

## **Sul server aptly**

>Verificare che la chiave si presente:
```shell
gpg --list-keys
```

>Esportare la chiave in formato ASCII/armored (leggbile) per poterla passare ad apt:
```shell
gpg --armor --export password > /tmp/nome-password.pub
```

>Successivamente condividere la chiave al client tramite metodo personale (rsync/scp/ecc...)

## **Sul client**

>Spostare la chiave nel keyrings:
```shell
cp manuel-repo.pub /etc/apt/keyrings/
```

>Dare i giusti permessi:
```shell
chmod 644 /etc/apt/keyrings/manuel-repo.pub
```

---
# **Installazione della CA sui client**
>Per far sì che il client si possa sincronizzare con quella repo dobbiamo aggiungerlo alla lista delle repositories raggiungibili e dargli anche il certificato in modo che si possa fidare di questo

## **Trasferimento del certificato**

>Copiare il certificato della CA aziendale sul client nella cartella:
```sh
cp ca.crt /usr/local/share/ca-certificates/ca-aziendale.crt
```

>Aggiornare il database dei certificati fidati del sistema:
```shell
sudo update-ca-certificates
```


## **Aggiungere la repo ad apt**

>In Debian/Ubuntu, le sorgenti personalizzate non si mettono nel file principale (/etc/apt/sources.list) ma si crea un file dedicato dentro la cartella /etc/apt/sources.list.d

>Creazione del file all'interno della cartella personale:
```shell
sudo nano /etc/apt/sources.list.d/apt-repo.sources
```

>Contenuto del file:
```shell
Types: deb
URIs: https://192.168.1.195/
Suites: noble
Components: main
Signed-By: /etc/apt/keyrings/manuel-repo.pub
```

>- signed-by , indica dove si trova la chiave gpg della repo su questo pc (oppure su un url)
>- https:// , indirizzo dove si trova la repo (sia IP che FQDN)
>- noble, indica il codename (nome-versione) della distribuzione su cui si basa la repo aptly
>- main, indica lo stato della repo e dei packages
