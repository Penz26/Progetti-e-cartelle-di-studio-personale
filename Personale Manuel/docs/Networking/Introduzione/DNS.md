#Networking 

# **Cos'è?**
>Un DNS (Domain Name System) permette un semplice modo per comunicare con altri dispositivi su Internet senza dover ricordare sequenze di numeri complicati (IP address).
>Invece di ricordarsi 104.26.10.229 ci ricordiamo il numero che il DNS gli ha associato, in questo caso tryhackme.com

---

# **Gerarchia dei Domini**

![[gerarchia_domini.png]]

## **TLD (Top Level Domain)**

>Un TLD è la parte più a destra del dominio. Per esempio per tryhackme.com il TLD è .com.
>Ci sono 2 tipi di TLD
>- gTLD (Generic Top Level)
>  usato di solito per indicare il significato del dominio (.com   commerciale. .gov   -governo, ecc...)
>- ccTLD (Country Code Top Level Domain)
>  usato per localizzazione geografica (.it  -italia)

## **Second Level Domain**
>Se il .com è il TLD il resto è il Second Level Domain (es. tryhackme).
>Quando si registra un dominio, il second-level-domain non può superare i 63 caratteri + TLD e può usare solo caratteri da a-z e 0-9.

## **Subdomains**
>Un sottodominio è alla sinistra del second level domain e separato da un . (es. admin.tryhackme.com) la parte admin è il subdomain. 
>Devono seguire gli stessi limiti di caratteri dei subdomain.
>Non ci sono limiti alla quantità di subdomain che si possano creare per il tuo dominio.

---

# **Tipi di record DNS**
>Il DNS non è solo per siti web, e molteplici tipi di record DNS esistono. I più comuni sono:
>- A record
> 	Questi risolvono indirizzi IPv4
>- AAAA record
> 	 Questi risolvono indirizzi IPv6
>- CNAME record
> 	 Questi risolvono altri nomi di dominio, (es. il subdomain store.tryhackme.com ritorna un CNAME record shop.shopify.com)
> 	 Un'altra chiamata DNS sarà fatta all'altro dominio per trovarne l'IP
> - MX record
> 	  Questo risolve l'indirizzo del server che si occupa delle mail per il dominio che si sta cercando (es. una risposta MX per tryhackme.com sarebbe alt1.aspmx.google.com)
> - TXT record
> 	  Sono record con un campo di inserimento libero dove ogni text-based data può essere conservato.

---

# **Cosa succede quando si fa una richiesta DNS ?**

![[DNS_request.png]]

1. Quando si richiede un nome di un dominio il computer prima cerca nella cache locale per vedere se l'avessi cercato prima, se non è così, una richiesta viene mandata al Server DNS ricorsivo
2. Un Server DNS ricorsivo è solitamente dato dal proprio ISP. Questo server ha una cache locale per domini visitati di recente. Se un risultato è trovato localmente questo viene mandato indietro al tuo Pc e la richiesta finisce qui (spesso avviene per siti popolari come Google, Facebook, Twitter, ecc...) Se la richiesta non si trova localmente inizia la ricerca con gli Internet root DNS servers
3. I root servers è la spina dorsale di Internet, il loro compito è quello di indirizzarti al TLD corretto. Se riconosce un .com ti indirizzerà al server che si occupa di indirizzi .com
4. Il server TLD tiene i record per un po' per trovare il server autoritativo per risolvere la richiesta DNS. Il server autoritativo è anche conosciuto come il nameserver del dominio.
5. Il Server autoritativo è responsabile per conservare i record DNS per un dominio particolare e dove gli aggiornamenti di tali DNS record sarebbero fatti. Dipendendo dal tipo di record, il DNS record viene rimandato al Server DNS ricorsivo che mantiene una copia in locale per richieste future e successivamente indietro al client che ha fatto la richiesta. I record DNS hanno un TTL (Time To Live) che rappresenta in secondi quanto tempo dovrebbe essere salvata localmente fino a quando dovresti ricercarla ancora.