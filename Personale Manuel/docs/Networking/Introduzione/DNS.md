#Networking 

# **Cos'è?**
>Un DNS (Domain Name System) permette un semplice modo per comunicare con altri dispositivi su Internet senza dover ricordare sequenze di numeri complicati (IP address).
>Invece di ricordarsi 104.26.10.229 ci ricordiamo il nome che il DNS gli ha associato, in questo caso tryhackme.com

>Funziona sulla porta 53 e utilizza sia UDP che TCP

---

# **Gerarchia dei Domini**

![[gerarchia_domini.png]]

## **Root Domain**
>Omesso nella scrittura comune, la gerarchia parte da un . che indica la radice gestita dai 13 root server globali.

## **TLD (Top Level Domain)**

>Un TLD è la parte più a destra del dominio. Per esempio per tryhackme.com il TLD è .com.
>Ci sono 2 tipi di TLD
>- gTLD (Generic Top Level)
>  usato di solito per indicare il significato del dominio (.com   commerciale. .gov   -governo, ecc...)
>- ccTLD (Country Code Top Level Domain)
>  usato per localizzazione geografica (.it  -italia)

## **Second Level Domain**
>Se il .com è il TLD il resto è il Second Level Domain (es. tryhackme).
>Quando si registra un dominio, l'intero "nome del dominio" (FQDN = Fully Qualified Domain Name) non può superare i 253 caratteri,  il second-level-domain non può superare i 63 caratteri + TLD e può usare solo caratteri da a-z e 0-9 e il - ma non può iniziare o finire con esso.

## **Subdomains**
>Un sottodominio è alla sinistra del second level domain e separato da un . (es. admin.tryhackme.com) la parte admin è il subdomain. 
>Devono seguire gli stessi limiti di caratteri dei subdomain.
>Non ci sono limiti alla quantità di subdomain che si possano creare per il tuo dominio finchè il FQDN non superi i 253 caratteri.

---

# **Tipi di record DNS**
>Il DNS non è solo per siti web, e molteplici tipi di record DNS esistono. I più comuni sono:
>- **A record:**
> 	Questi risolvono indirizzi IPv4
>- **AAAA record:**
> 	 Questi risolvono indirizzi IPv6
>- **CNAME record:** (Canonical Name)
> 	 Mappa un nome alias su un altro nome di dominio, (es. il subdomain store.tryhackme.com ritorna un CNAME record shop.shopify.com)
> 	 Un'altra chiamata DNS sarà fatta all'altro dominio per trovarne l'IP
> - **MX record (Mail Exchanger):**
> 	  Questo risolve l'indirizzo del server che si occupa delle mail per il dominio che si sta cercando (es. una risposta MX per tryhackme.com sarebbe alt1.aspmx.google.com)
> - **TXT record:**
> 	  Sono record con un campo di inserimento libero dove ogni text-based data può essere conservato.
> - **NS record (Name Server):**
> 	  Delega una zona DNS all'utilizzo di specifici server autoritativi. Indica quali server contengono i record effettivi di quel dominio
> - **SOA record (Start of Authority):**
> 	  Contiene informazioni cruciali sulla zona DNS, tra cui il name server primario, l'email dell'amministratore, il numero di serie e timer di refresh
> - **PTR record (Pointer):**
> 	  Il contrario del record A. Risolve un indirizzo IP in un nome di dominio (reverse DNS lookup)

---

# **Cosa succede quando si fa una richiesta DNS ?**

![[DNS_request.png]]

## 1.  **Cache locale e file Hosts**
 Quando si richiede un nome di un dominio il sistema operativo prima cerca nella cache locale e nel file hosts di sistema per vedere se l'avessi cercato prima, se non è così, una richiesta viene mandata al Server DNS ricorsivo.
## 2. **DNS Ricorsivo (Resolver)**
 Un Server DNS ricorsivo è solitamente dato dal proprio ISP. Questo server ha una cache locale per domini visitati di recente. Se un risultato è trovato localmente questo viene mandato indietro al tuo Pc e la richiesta finisce qui (spesso avviene per siti popolari come Google, Facebook, Twitter, ecc...) Se la richiesta non si trova localmente inizia la ricerca con gli Internet root DNS servers
## 3.**Root Servers** 
 I root servers sono la spina dorsale di Internet. Non conoscono l'IP del sito ,il loro compito è quello di indirizzarti al TLD corretto. Se riconosce un .com ti indirizzerà al server che si occupa di indirizzi .com
## 4. **TLD Servers** 
 Mantengono i riferimenti per i server autoritativi di tutti i domini registrati sotto quella specifica estensione. Indirizzeranno il Resolver verso il Name server corretto per quel dominio specifico
## 5. **Server autoritativo (Name Server)**
 Il Server autoritativo è responsabile per conservare i record DNS . Dipendendo dal tipo di record, il DNS record viene rimandato al Server DNS ricorsivo che mantiene una copia in locale per richieste future e successivamente indietro al client che ha fatto la richiesta. I record DNS hanno un TTL (Time To Live) che rappresenta in secondi quanto tempo dovrebbe essere salvata localmente fino a quando dovresti ricercarla ancora.
## **6. Ritorno al client**
 Il DNS ricorsivo memorizza il record nella propria cache per il tempo specificato dal TTL (Time to Live) (espresso in secondi) in modo da velocizzare le richieste future e infine consegna la risposta al client.

---

# **Il comando per interrogare i server DNS**
>Questo comando ci permette di interrogare server DNS e verificare la propagazione o la correttezza dei record

>**Di default risolverà il suo indirizzo IPv4**
>Per altri tipologie di record DNS
## Sintassi comune del comando dig
```sh
dig @[server_dns] [nome_dominio] [tipo_record]
```

---

## Scoprire l'indirizzo IPv4 di un dominio:
```sh
dig example.com
```
>Questo comando restituisce un output completo di varie sezioni (HEADER, QUESTION SECTION, ANSWER SECTION, tempi di risposta, ecc...)

>Per pulire l'output e mostrare esclusivamente la risposta essenziale usiamo
```sh
dig example.com +short
```

>Se vogliamo seguire come un nome viene risolto partendo dal Root server usiamo:
```sh
dig example.com +trace
```
>In questo modo dig bypassa la cache del resolver locale ed effettua una risoluzione partendo dall'alto della gerarchia DNS
>1. Root server
>2. TLD server
>3. Authoritative Server (Name Server)

---

## Interrogare un server DNS in specifico per un dominio
```sh
--- Controllare indirizzo Ipv4 ---
dig @8.8.8.8 example.com 

--- per il server di posta ---
dig @8.8.8.8 example.com MX
```

---
## Reverse DNS (PTR)
>Se abbiamo un indirizzo IP di cui vogliamo sapere il dominio a cui è associato facciamo una richiesta per un record PTR.

>Questa operazione viene eseguita con dig:
```sh
dig -x [ip_da_cercare]
```

---

# **File di Zona**
>Configurazione standard per un dominio in un file di zona:

```sh
$TTL 86400
@   IN   SOA   ns1.example.com admin.example.com (
				2026070901 #Serial Number (YYYYMMDDnn)
				3600       #Refresh
				1800       #Retry
				604800     #Expire
				86400)     #Minimum Time to Live

; --- Server dei Nomi (Nameservers) ---
@       IN   NS   ns1.example.com.
@       IN   NS   ns2.example.com.

; --- Record Principali (IP del dominio) ---
@       IN   A       192.0.2.1
@       IN   A       2001:db8::1
ns1     IN   A       192.0.2.2
ns2     IN   A       192.0.2.3

; --- Alias e Servizi Web ---   
web     IN   CNAME   @
www     IN   CNAME   @
app     IN   A       192.0.2.5
cdn     IN   CNAME   static.provider.net

; --- Gestione Posta Elettronica (Mail server) ---
mail    IN  A       192.0.2.10
@       IN  MX  10  mail.example.com

; --- Sicurezza e Autenticazione ---
@       IN  TXT     "v=spf1 ipv4:192.0.2.10 -all"
_dmarc  IN  TXT     "v=DMARC1; p=reject;"

; --- Sottodomini Complessi ---
staging.dev IN A    192.0.2.99
```

## **SOA (Start of Authority)**
>Indica  il server dns autoritativo, chi è l'amministratore (admin.example.com sarebbe admin@example.com solo che non si può mettere @ per problemi). Il resto dei numeri sono la configurazione dei vari tempi tranne il primo che è il seriale.

>Spiegati di seguito:
>$TTL 86400 = definisce il TTL di default per tutti i record che non ne specificano uno proprio
>**IN:** classe del record (INTERNET)
>**SOA:** Indica il tipo di record
>**ns1.example.com.:** Il server DNS primario e autoritativo per questo dominio
>**admin.example.com:** Indirizzo email dell'amministratore responsabiile. La @ viene sostituita da un punto per evitare errori di sintassi

>All' interno delle parentesi () troviamo i parametri:
>**Serial:** la versione del file che avverte i server dns secondari se la versione che hanno è aggiornata o meno
>**Refresh:** Ogni quanto i server secondari controllano se il Serial è cambiato
>**Retry:** Quanto aspettare prima di riprovare se il primario non risponde
>**Expire:** Dopo quanto tempo di assenza del primario il secondario smette di di rispondere
>**Minimum TTL:** Il tempo di cache per le risposte negative

---
## **Record di Risorsa**
>Elencano le risorse che dovranno essere risulti dai DNS server

# **NS**

```D
@   IN   NS   ns1.example.com
```
>Dice che ns1.example.com è il NameServer per il dominio principale (example.com)

```D
@   IN   NS   ns2.example.com
```
>In pratica questi due record dicono che:
>example.com viene gestito dai server ns1.example.com e ns2.example.com.

---
## **A e AAAA**

```D
@       IN  A       192.0.2.1 
```
>Dice che example.com. corrisponde all' IPv4 192.0.2.1

```D
@       IN  AAAA    2001:db8::1
```
>Dice che example.com. corrisponde all' IPv6 2001:db8::1


```D
ns1     IN  A       192.0.2.2
```
>Dice che ns1.example.com. corrisponde all' IPv4 192.0.2.2

---
## **CNAME (Alias)**

```D
web     IN  CNAME   @
```
>Dice che web.example.com è un alias di example.com



```D
cdn     IN  CNAME   static.provider.net.
```
>Dice che cdn.example.com è un alias di static.provider.net


---
## **MX (Mail Exchanger)**

```D
@        IN  MX   10   mail.example.com.
```
>La posta diretta a example.com deve essere inviata a mail.example.com. con priorità 10

>Quando qualcuno scrive info@example.com, il suo server postale cerca il record MX example.com per sapere quale server consegnare la lettera. 
>Il numero 10 indica la priorità (**numeri più bassi = priorità più alta**)

---
# **TXT (Testo, SPF e DMARC)**

```D
@       IN  TXT     "v=spf1 ip4:192.0.2.10 -all"
```

>Dice che example.com ha questo testo associato "v=spf1 ipv4:192.0.2.10 -all"

>SPF dice al mondo "solo il server con IP 192.0.2.10" può inviare email a nome @example.com. Se le ricevi da altri IP, sono false (-all)

```D
_dmarc  IN  TXT     "v=DMARC1; p=reject;"
```

>DMARC dice al server riceventi (come Gmail) cosa fare se l'SPF fallisce (in questo caso p=reject ovvero di bloccare ed eliminare l'email sospetta) 

---
## **Sottodomini di Terzo livello**

```d
staging.dev   IN   A   192.0.2.99
```

>Dice che staging.dev.example.com. corrisponde all' IP 192.0.2.99

---
# **BIND e PowerDNS**
>Sono due Software server DNS autoritativi. Hanno lo stesso compito, tradurre i nomi di dominio nei rispettivi IP per permettere ai computer di trovarsi tra loro.

## **BIND (Berkeley Internet Name Domain)**
>E' il software più vecchio e utilizzato al mondo (ancora in costante aggiornamento).

>E' file-based. Ogni configurazione e ogni record di ogni zona sono file di testo statici

>Quando si modifica qualcosa bisogna far ricaricare il servizio con:
```sh
rdnc reload

--- oppure ---

systemctl reload named
```

## **Configurazione**
>Il server DNS si configura tramite un singolo file chiamato named.conf situato in /etc/bind/

>Esempio di configurazione:
```
options {
    directory "/var/cache/bind";

    // Su quali interfacce di rete ascoltare (es. tutte)
    listen-on port 53 { any; };
    listen-on-v6 { any; };

    //Chi può fare domande a questo server?
    allow-query { any; }; 

    // I Forwarders (Inoltratori) 
    forwarders {
        1.1.1.1;   // Cloudflare
        8.8.8.8;   // Google
    };

    dnssec-validation auto;
};

--- Definizione della zona come Primario (MASTER) ---
zone "example.com" {
    type master;
    file "/etc/bind/db.example.com"; # Il file .txt di configurazione della zona
    allow-transfer { 192.0.2.3; };    # IP del server secondario (sicurezza)
};

--- Se fosse stato un server dns secondario (SLAVE)---

zone "example.com" {
    type slave;
    file "/var/cache/bind/db.example.com.slave";
    masters { 192.0.2.2; };          # IP del server primario da cui copiare
};


```
---
## **PowerDNS**
>E' la soluzione moderna progettata per la scalabilità, l'automazione e l'integrazione con il cloud

>E' Database driven. Non usa file di testo bensì usa Database SQL

>Quando si modifica qualcosa (direttamente dal terminale del server oppure con interfaccia web o API ) il DNS risponde immediatamente con il nuovo dato

## **Configurazione**
>PowerDNS concentra tutte le sue configurazioni in un unico file principale situato in /etc/powerdns/pdns.conf

>PowerDNS non crea da solo il DB quindi prima di configurare bisogna creare il database con:
>- utente che si specifica nel conf
>- password che si specifica nel conf
>- nome del db che si specifica nel conf

>Inoltre PowerDNS ha bisogno di tabelle specifiche chiamate:
>- domains
>- records
>- cryptokeys
>- ecc...
>Fortunatamente quando si installa il pachetto PowerDNS su Linux il sistema fornisce già il file SQL pronto con tutta la struttura
```sh
mysql -u pdns_user -p powerdns_db < /usr/share/doc/pdns-backend-mysql/schema.mysql.sql
```

>Esempio di una configurazione:
```TOML
#################################
# Configurazione Rete e Identità
#################################
# IP su cui il server si mette in ascolto (0.0.0.0 = tutte le interfacce)
local-address=0.0.0.0
local-port=53

# Diventa primario (Master) per inviare i NOTIFY ai secondari
master=yes
slave=no

#################################
# Configurazione del Backend (Database)
#################################
# Diciamo a PowerDNS di usare il motore MySQL/MariaDB
launch=gmysql

# Coordinate per connettersi al database dove risiedono le zone
gmysql-host=127.0.0.1
gmysql-user=pdns_user
gmysql-password=PasswordSicura123!
gmysql-dbname=powerdns_db

#################################
# Sicurezza e Performance
#################################
# Utente non privilegiato con cui gira il servizio dopo l'avvio
setuid=pdns
setgid=pdns

# Per quanti secondi tenere in cache le risposte nel server stesso
cache-ttl=20
```