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
## **Sicurezza dei file (GPG Key)**
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
sec rsa4096/ID-Chiave 2026-07-20
```

>Esportare la chiave pubblica in un file di testo (sarà il file che distribuiamo ai client):
```sh
gpg --export --armor ID_Chiave > my-repo-key.pub
```

---
# **Trasformazione del software in pacchetti Debian**
>Nelle repositories aptly essendo basate su debian/Ubuntu i pacchetti dovranno essere in formato .deb per farlo useremo il tool **dpkg-deb --build**

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

>Se non ci sono errori creerà un file chiamato nome-software_1.0.deb

---
# **Come possiamo creare la nostra Repo?**
>Dopo aver il timbro GPG installiamo il gestore delle repository aptly

```sh
sudo apt update && sudo apt install aptly -y
```

## **Crezione della repo con la  sua struttura locale** 
>(nel DB di aptly) prima di operare:
>Questo comando aggiunge i metadati nel database interno (~/.aptly/db/)

>La configurazione di aptly risiede nel file ~/.aptly.conf, dove si possono specificare vari campi tra cui la directory in cui verranno salvati i dati al momento della pubblicazione.

>[!ATTENTION] Ogni distribution (TARGET) deve avere la sua repo
```sh
aptly repo create -comment="Repository Interna Manuel Prod" -distribution="noble" -component="main" nome-repo
```

## **Spiegazione delle flag**
>**- comment** : descrizione della repo
>**- distribution**: release per cui sono compilati i pacchetti (servono come valori predefiniti)
>**- main**: sezione a cui appartengono i pacchetti                 (servono come valori predefiniti)


>**Aggiungere un file:**
>Copia i file .deb in ~/.aptly/pool/
```sh
aptly repo add nome-repo /path/al/software_1.0_amd64.deb
```

---
## **Come rendere la repo pubblica ed accessibile**:

>Ci sono 2 metodi
>- aptly publish repo , veloce ma senza tracciamento nel tempo
>- aptly publish snapshot, immutabile col tempo e rollback facile

>[!ATTENTION] Ogni prefix DEVE avere una pubblicazione
### **Repo normale**

>Prima di tutto aggiungere il pacchetto alla repo
```shell
aptly repo add nome-repo /path/al/software_1.0_amd64.deb
```

>**aptly publish repo**
>Prende tutto il materiale nel database, genera la mappa e crea la repository reale nella cartella ~/.aptly/public/  (**PER LA PRIMA VOLTA E BASTA**)
```sh
aptly publish repo -gpg-key="ID-chiave-gpg" -passphrase="password-repo" -distribution="codename-distro" -component="main" nome-repo .
```

## **Spiegazione delle flag**
>**-gpg-key**: ID (non intera chiave) della chiave GPG
>**- passphrase**: pasphrase che protegge la repo
>**-distribution**: distribuzione/release per cui sono stati compilati i pacchetti
>**-component**: a che sezione devono appartenere i file
>**- .  :** indica il prefisso sotto cui pubblicarla (il punto indica nell'indirizzo principale della repo `http://server-aptly/dists/...`.) 

>Per aggiornare una pubblicazione esistente dopo aver aggiunto/rimosso nuovi pacchetti .deb:
```sh
aptly publish update -gpg-key="ID-chiave-gpg" -passphrase="password-repo" -distribution="noble" .
```

---
### **Snapshot**

>Prima di tutto aggiungere il pacchetto alla repo
```shell
aptly repo add nome-repo /path/al/software_1.0_amd64.deb
```

>Creazione dello snapshot
```shell
#Creazione dello snapshot della repo DOPO aver aggiunto i file
aptly snapshot create <nome-snapshot> from repo <nome-repo>

#Vedere tutti gli snapshot che abbiamo fatto fino ad oggi
aptly snapshot list
```

>Pubblicazione della repo con metodo snapshot (==**PRIMA VOLTA E BASTA**==):
```shell
aptly publish snapshot -gpg-key="ID-chiave" -passphrase="passphrase" -distribution="noble" -component="main" nome-snapshot internal
```

## **Spiegazione delle flag**
>**-gpg-key**: ID (non intera chiave) della chiave GPG
>**- passphrase**: pasphrase che protegge la repo
>**-distribution**: distribuzione/release per cui sono stati compilati i pacchetti
>**-component**: a che sezione devono appartenere i file
>**- internal  :** indica il prefisso sotto cui pubblicarla (il punto indica nell'indirizzo principale della repo `http://server-aptly/dists/...`., in questo caso `http://server-aptly/internal`) 

>Aggiornamento della repo basata su snapshot
```shell
aptly publish switch -batch -gpg-key="" -passphrase="" noble internal "nome-snapshot"
```
> - aptly publish switch: prende una pubblicazione esistente la fa puntare ad un nuovo snapshot
> - batch, dice a GPG di eseguire la firma in modo non interattivo
> - gpg-key: specifica l'ID della chiave GPG da usare per firmare
> - noble: distribuzione target della pubblicazione
> - internal: è la sottocartella in cui vive il repository
> - nome-snapshot: il nuovo snapshot appena creato che vogliamo pubblicare


>Una volta lanciata la pubblicazione/aggiornamento chiederà la passphrase che si ha usato per la chiave GPG.
>Una volta inserita darà come risultato questo messaggio:

![[aptly-publish.png]]

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

---

1. **Creare la CA**
```sh
#Crea la firma con cui la CA firmerà i certificati 
openssl genrsa -aes256 -out ca.key 4096 

#Crea il certificato Root pubblico (il template su cui si dovranno basare gli altri)   
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
```
2. **Certificato per il server web**
```sh
#Crea la chiave del server 
openssl genrsa -out server.key 4096 

#Usa la chiave di prima per creare la richiesta di certificato al CA
openssl req -new -key server.key -out server.csr

#Firma del certificato tramite la CA (genera anche il registro della ca, il file si chiamerà ca.srl)
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt
```
3. **Certificato per il client (Se si vuole abilitare la mutua autenticazione MTLS)**
   Dentro la cartella /etc/apt/certs/ del CLIENT 
```sh
#Crea la chiave per il client
openssl genrsa -out client.key 4096

#Crea la richiesta di certificato al CA firmando con la chiave appena creata
openssl req -new -key client.key -out client.csr

#Firma del certificato del client con la chiave della CA
openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt
```

---
# **Configurazione di Nginx per controllare  i certificati:**

>Per comodità del percorso e ordine abbiamo spostato i certificati del server e della CA nella cartella /etc/nginx/ssl
```shell
server {
    listen 443 ssl;
    server_name 192.168.1.196;    #IP del server aptly oppure FQDN

    # 1. Radice dei file (Punta alla cartella che contiene i file di Aptly)
    root /var/www/apt-repo/public;
    #index index.html;    di default va a cercare questo file se non lo trova fa vedere il contenuto della cartella

    # 2. Configurazione SSL Standard (Il server dimostra chi è)
    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    # 3. Configurazione mTLS (Il server pretende di sapere chi è il client)
    ssl_client_certificate /etc/nginx/ssl/ca.crt; # La CA aziendale di cui Nginx si fida
    ssl_verify_client      on;               # Forza la mutua autenticazione

    # 4. Permetti il browsing delle cartelle (APT ne ha bisogno)
    location / {
        autoindex on;
        try_files $uri $uri/ =404;
    }
}
```

>[!NOTE] Se si vuole abilitare un autenticazione tramite IP o password ---> [[#**IP allow-list e basic auth**]]

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
# ==***Di cosa necessita il client per poter usare la repository***==

>1. **Chiave GPG della repository** [[#**Installazione della chiave GPG della repo sul client**]]
>2. **Certificato della CA** [[#**Installazione del certificato della CA sui client**]]
>3. **Aggiungere la repository ad APT** [[#**Aggiungere la repo ad apt**]]
>4. **Certificati del client** [[#**Creazione dei certificati per il sito Nginx e i client**]]
>5. **Attivare il MTLS** [[#**Creare il collegamento mTLS tra client e server**]]
>6. **Avere le credenziali per il Basic Auth** [[#**Basic-Auth Lato client**]]

---
# **Installazione della chiave GPG della repo sul client**
>Nelle nuove versioni di Ubuntu (dalla 22.04) il vecchio comando apt-key add è stato discontinuato per motivi di sicurezza.

>Ora le chiavi gpg non vengono aggiunte ad un unico grande file globale (/etc/apt/trusted.gpg) invece la singola chiave di una repository viene salvata nel proprio file in /etc/apt/keyrings/nome-repo.pub

## **Sul server aptly**

>Verificare che la chiave si presente:
```shell
gpg --list-keys
```

>Esportare la chiave in formato ASCII/armored (leggbile) per poterla passare ad apt:
```shell
gpg --armor --export ID-chiave-gpg > /tmp/nome-password.pub
```

>Successivamente condividere la chiave al client tramite metodo personale (rsync/scp/ecc...)

## **Sul client**

>Spostare la chiave nel keyrings:
```shell
cp nome-password.pub /etc/apt/keyrings/manuel-repo.pub
```

>Dare i giusti permessi:
```shell
chmod 644 /etc/apt/keyrings/manuel-repo.pub
```

---
# **Installazione del certificato della CA sui client**
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

---
# **Creare il collegamento mTLS tra client e server**
>Per far in modo che il server si fidi del client quest'ultimo deve mostrare il suo certificato e la chiave al server e verificare che il certificato della CA che mostra il server combaci con quello che ha.

>APT ha una directory dedicata ai suoi metodi da seguire in ordine (**/etc/apt/apt.conf.d**)
>Per farlo ci serve un file per apt che gli specifica la regola per il nostro client e connettersi al server con la nostra repo locale.

>In questo file specifichiamo cosa deve passare al momento della connessione con il server aptly
>- **CAInfo**, indica il path per il certificato della CA in modo che il client si possa fidare del server
>- **SSLCert**, indica il path per il proprio certificato in modo che il server si possa fidare
>- **SLLKey**, indica il path per la propria chiave in modo che il server si possa fidare
>Gli ultimi due forza i controlli
```shell
Acquire::https::IP/FQDN::CAInfo "/usr/local/share/ca-certificates/ca.crt";
Acquire::https::IP/FQDN::SSLCert "/etc/apt/certs/repo-client.crt";
Acquire::https::IP/FQDN::SSLKey "/etc/apt/certs/repo-client.key";
Acquire::https::IP/FQDN::Verify-Peer "true";
Acquire::https::IP/FQDN::Verify-Host "true";
```

>[!IMPORTANT] La chiave del client deve essere decifrata altrimenti apt non riesce a leggerla

>Decifrazione della chiave del client
```shell
cp /etc/apt/certs/repo-client.key /etc/apt/certs/repo-client.key.bak
openssl rsa -in /etc/apt/certs/repo-client.key.bak -out /etc/apt/certs/repo-client.key
```

---
# **Aggiungere la repo ad apt**

>In Debian/Ubuntu, le sorgenti personalizzate non si mettono nel file principale (/etc/apt/sources.list) ma si crea un file dedicato dentro la cartella /etc/apt/sources.list.d.

>**Prima il file era in formato .list ma Debian e Ubuntu hanno detto che questo formato dava problemi di sicurezza quini fino al 2029 sarà uttilizzabile una configurazione su una singola riga, ma successivamente bisgonerà passare ad un formato .sources** 

>Creazione del file all'interno della cartella personale:
```shell
sudo nano /etc/apt/sources.list.d/apt-repo.sources
```

>Contenuto del file:
```shell
Types: deb
URIs: https://192.168.1.196/prefix
Suites: noble
Components: main
Signed-By: /etc/apt/keyrings/manuel-repo.pub
```

>- signed-by , indica dove si trova la chiave gpg della repo su questo pc (oppure su un url)
>- https:// , indirizzo dove si trova la repo (sia IP che FQDN)
>- noble, indica il codename (nome-versione) della distribuzione su cui si basa la repo aptly
>- main, indica lo stato della repo e dei packages

---
# **IP allow-list e basic auth**
>Per ora "basta" avere il certificato della CA che convalida quello che ci mostra il server, una chiave ed un certificato personale firmato dalla CA per entrare.
>Ora vogliamo mettere altri controlli sull' IP, e se questo non combacia ha un'ultima possibilità per autenticarsi grazie ad una password.

```mermaid.js
flowchart TD
A[Server] <--Scambio certificati--> B[Client]
B --> C{I certificati corrispondono?}
C --Sì-->D{Rientra negli IP/Subnet Impostata?}
C --No--> E[X FUORI]
D --Sì-->F[Bene Entra Pure!]
D --No-->G{Conosce la password?}
G --Sì-->H[Ok non sei in sede, ma sappiamo che sei te!]
G --No-->I[Non sappiamo chi tu sia!]
```

## **Basic-Auth Lato server**

>Per fare questa operazione dobbiamo scaricare dei pacchetti:
```shell
apt install apache2-utils
```

>Creazione del file per il login con il nuovo comando:
```shell
htpasswd -c /path/in/cui/salvarla nome-user

#Chiederà la password che si userà per il login
```

>Configurazione Aggiornata del sito nginx **SUL SERVER** (/etc/nginx/sites-enabled/apt-repo.conf)

## **Configurazione Nginx completa**
```shell
server {
    listen 443 ssl;
    server_name 192.168.1.196;

    # 1. Radice dei file (Punta alla cartella pubblica di Aptly)
    root /var/www/apt-repo/public;

    # 2. Configurazione SSL Standard (Il server dimostra chi è)
    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    # 3. Configurazione mTLS (Il server pretende di sapere chi è il client)
    # La CA aziendale di cui Nginx si fida
    ssl_client_certificate /etc/nginx/ssl/ca.crt; 
    ssl_verify_client      on;                 # Forza la mutua autenticazione!

    # 4. Controllo Accessi HTTP (IP Allowlist + Basic Auth)
    location / {
        # Regola di soddisfazione: basta passare l'IP OPPURE la password
        satisfy any;

        # --- IP Allowlist ---
        allow 192.168.1.0/24;  # Consente tutta la subnet locale
        allow 127.0.0.1;       # Consente il loopback del server stesso
        deny all;              # Blocca tutti gli altri IP non esplicitati sopra

        # --- Basic Authentication ---
        auth_basic "Accesso Riservato Repository Aptly";
        auth_basic_user_file /etc/nginx/.htpasswd;

        # --- Permetti il browsing delle cartelle per APT ---
        autoindex on;
        try_files $uri $uri/ =404;
    }
}
```

>Ricaricare la configurazione del server nginx
```shell
systemctl reload nginx
```

---
## **Basic-Auth Lato client**
>Sul client adesso dibbiamo dargli le credenziali che dovrà usare per l'autenticazione base 
>nel caso non rientra nella subnet/IP abilitati.

>Su Debian/Ubuntu c'è una directory creata proprio per questo scopo **(/etc/apt/auth.conf.d)**:
```shell
machine 192.168.1.196 login nome-utente password password_usata_per_.htpasswd
```
> - machine: identifica su che macchina queste credenziali possono esssere utilizzate
> - login: va ad indicare il nome utente specificato al momento della creazione del file .htpasswd
> - password: indica la password specificata per .htpasswd

---
# **Integrazione con GitLab**
[[Esempio pipeline per aptly]]