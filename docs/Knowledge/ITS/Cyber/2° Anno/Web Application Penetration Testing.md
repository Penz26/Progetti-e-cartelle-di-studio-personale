---
date: 2026-11-05
tags:
  - CyberSecurity
subject: Attack
module: Penetration testing
source: https://drive.osaspace.it/index.php/apps/onlyoffice/17857?filePath=%2FITS_SANDBOX%2FSANDBOX%20-%20MATERIALI%20DOCENTI%2FSECONDO%20ANNO%2FCybersecurity%2FLezione04%2FLezione04.pdf
---
# **Cosa è un WAPT**
>Il **Web Apllication Penetration Testing** è un processo di valutazione della sicurezza di un sistema informatico rete o applicazione.
>Questo test viene condotto simulando un attacco informatico da parte di un hacker ma in modo controllato e legale.

>[!NOTE] **Obiettivo**
>Identificare e correggere vulnerabilità prima che possano essere sfruttate da attori malevoli

## **Etica e legalità**

- **Autorizzazione obbligatoria**: mai testare un sistema senza permesso
- **Regole d'ingaggio**: limiti e obiettivi concordati con il cliente (rimanere nello scope di questo Pen test)
- **Normative di riferimento**: GDPR, ISO 27001, Computer Fraud and Abuse Act

---
# **Fasi di un WAPT**
1. Raccolta Informazioni
2. Scansione e analisi della vulnerabilità
3. Sfruttamento (exploitation)
4. Reporting e mitigazione

![[fasi_wapt.png]]

---
## **1° Raccolta Informazioni**

>[!NOTE] **Obiettivo**
>Raccogliere il maggior numero di dati possibili sull'obiettivo prima di eseguire un attacco


**Passive Reconnaissance (raccolta indiretta di dati)**
>- OSINT --> Ricerca di informazioni pubbliche su siti web, social media, ecc...
>- Analisi di metadati nei documenti pubblicati
>- Google Dorking --> utilizzo avanzato di Google per trovare dati sensibili

**Active Reconnaissance (interazione diretta con il target)**
>- esecuzione di ping sweep e scansioni di rete
>- identificazione di porte aperte e servizi in esecuzione (Nmap)
>- Rilevamento di versioni software e possibili vulnerabilità

**Tools**
[Shodan search engine](https://www.shodan.io/)
[censys search engine](https://platform.censys.io/search)
[fofa search engine]()

## **2° Scansione e analisi della vulnerabilità**

>[!NOTE] **Obiettivo**:
>Identificare debolezze sfruttabili nel sistema target

**Mappatura della rete e identificazione dei servizi**
>- scansione delle porte aperte e protocolli in uso (Nmap)
>- identificazione del sistema operativo (OS Fingerprinting)

**Analisi delle vulnerabilità**
>- Utilizzo di scanner automatici come [Nessus](https://www.tenable.com/products/nessus) e [OpenVAS](https://openvas.org/)
>- Controllo di database CVE (Common Vulnerabilities and Exposure)
>- Identificazione di software obsoleti o configurazioni errate


## **3° Sfruttamento (exploitation)**

>[!NOTE] **Obiettivo**:
>Simulare un attacco per ottenere accesso non autorizzato al sistema

**Tecniche di exploit più comuni**
> - attacchi a servizi vulnerabili (buffer overflow, RCE, privilege escalation)
> - SQL injection (accesso a database non protetti)
> - Cross Site Scripting (XSS - attacchi web)
> - Attacco brute force su credenziali deboli

**Strumenti utilizzati**
> - [Metasploit Framework](https://www.metasploit.com/) --> piattaforma per lanciare exploit
> - [Burp Suite](https://portswigger.net/burp/communitydownload) --> Test di sicurezza su applicazioni web


## **4° Reporting e mitigazione**

>[!NOTE] **Obiettivo**:
>Documentare le vulnerabilità scoperte e suggerire misure di sicurezza per eliminarle

**Struttura di un report di Penetration testing**
> - Introduzione --> Obiettivi e scopo di test
> - Metodologia --> Tecniche e strumenti utilizzati
> - Vulnerabilità Trovate --> Descrizione dettagliata con livello di rischio
> - Dimostrazione dell' exploit --> Prova dell'attacco effettuato
> - Raccomandazione di sicurezza --> Soluzioni per mitigare i rischi

**Strumenti per la reportistica**
>- [Dradis](https://dradis.com/ce/) --> Organizzazione delle evidenze
>- [Magic Tree](https://www.gremwell.com/what_is_magictree) --> Creazione di report automatizzati

---
# **Tecniche di Scansione e Raccolta Informazioni [[#**1° Raccolta Informazioni**]]**

## **Ricognizione Passiva**
>Raccolta di informazioni senza interagire direttamente con il target
>Utilizzo di fonti pubbliche per ottenere dati utili

**Tecniche Comuni**
>- OSINT 
>- WHOIS e nslookup per informazioni sui domini
>- Google Dorking per ricerche avanzate
>- Shodan per dispositivi esposti in rete

**WHOIS**
>Le informazioni WHOIS sono un feed di database globale del proprietario del dominio di persone che registrano nomi di dominio

>Ogni volta che viene registrato un nome di dominio viene richiesto di fornire informazioni identificative e di contatto come:
- Nome,
- Indirizzo postale
- Email
- Numero di telefono
- Città
- Codice postale
- Stato
- Paese
```bash
$ whois example.com
   Domain Name: EXAMPLE.COM
   Registry Domain ID: 2336799_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.iana.org
   Registrar URL: http://res-dom.iana.org
   Updated Date: 2026-08-14T08:01:43Z
   Creation Date: 1995-08-14T04:00:00Z
   Registry Expiry Date: 2027-08-13T04:00:00Z
   Registrar: RESERVED-Internet Assigned Numbers Authority
   Registrar IANA ID: 376
   Registrar Abuse Contact Email:
   Registrar Abuse Contact Phone:
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Name Server: ELLIOTT.NS.CLOUDFLARE.COM
   Name Server: HERA.NS.CLOUDFLARE.COM
   DNSSEC: signedDelegation
   DNSSEC DS Data: 2371 13 2 C988EC423E3880EB8DD8A46FE06CA230EE23F35B578D64E78B29C3E1C83D245A
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2026-11-05T09:25:50Z <<<
```

**nslookup**
>(Name Server Lookup) è uno strumento da riga di comando utilizzato per interrogare i server DNS per ottenere la mappatura del nome di dominio o dell'indirizzo IP

```bash
$ nslookup example.com

Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 2606:4700:10::6814:179a
Name:	example.com
Address: 2606:4700:10::ac42:93f3
```

**Google Dorking**
>Tecnica che utilizza operatori di ricerca avanzati per scoprire informazioni su Internet che potrebbero non essere prontamente disponibili tramite query di ricerca standard

>Questa strategia sfrutta le funzionalità degli algoritmi di ricerca di Google per individuare stringhe di testo specifiche nei risultati di ricerca

Le tecniche di Google Dorking prevedono principalmente l'uso di operatori di ricerca specifici. Come:
> - **Filetype**: questo operatore cerca tipi di file specifici. Ad esempio filetype:pdf restituisce file PDF
> - **Inurl**: può essere utilizzato per trovare parole specifiche all'interno dell'URL di una pagina. Ad esempio, inurl:login restituisce pagine con login nell'URL
> - **Intext**: può cercare testo specifico all'interno del contenuto di una pagina web. Ad esempio intext:password resituisce pagine che contengono la parola password
> - **Intitle**: l'operatore viene utilizzato per cercare termini specifici nel titolo di una pagina web. Ad esempio intitle:"index of" rivela server web con elenco directory abilitato
> - **Link**: può essere utilizzato per trovare pagine che rimandano a un URL specifico. Ad esempio link:example.com troverebbe pagine che rimandano a example.com
> - **Site**: l'operatore consente di effettuare ricerche all'interno di un sito specifico. Ad esempio: site:example.com effettua ricerche all'interno di example.com

![[google_dorking.png]]

**Shodan**
>Shodan è un motore di ricerca per oggetti connessi a Internet, tra cui server, router, siti Web, database, telecamere, sistemi di controllo industriale, ecc...

I filtri di ricerca hanno la forma filtername:value

>[!EXAMPLE] Per visualizzare i siti web che sono stati "hackerati" e il cui tag title è impostato per includere la stringa hacked by, cerca http.title:'hacked by'

![[shodan.png]]


## **Ricognizione Attiva**
>Interazione diretta con il target per ottenere informazioni dettagliate
>Può essere rilevata dai sistemi di sicurezza

**Strumenti e tecniche**
> - [Nmap](https://nmap.org/) -->scansioni di porte e servizi
> - [theHarvester](https://github.com/laramies/theHarvester) --> per raccogliere email e nomi di dominio
> - [Masscan]() --> Scansione rapida di grandi intervalli di IP
> - [Netcat]() --> strumento per testare connessioni di rete

**nmap**
```bash
nmap nmap.scanme.nmap.org

#l'output dopo qualche minuto sarà simile a questo:
#Starting Nmap ( https://nmap.org )

Nmap scan report for scanme.nmap.org (64.13.134.52)
Not shown: 994 filtered ports
PORT STATE SERVICE
22/tcp open ssh
25/tcp closed smtp
53/tcp open domain
70/tcp closed gopher
80/tcp open http
113/tcp closed auth

Nmap done: 1 IP address (1 host up) scanned in 4.99 second
```

---
# **Sfruttamento delle vulnerabilità (Exploitation)**

## **OWASP Top 10**
>La OWASP Top 10 è una lista di vulnerabilità di sicurezza più critiche nelle applicazioni web, pubblicata dalla Open Web Application Security Project (OWASP).

>Questo elenco rappresenta una guida fondamentale per sviluppatori, pentester e professionisti della sicurezza informatica per identificare, comprendere e mitigare le minacce più comuni nel panorama della cybersecurity.

>[!NOTE] **Obiettivi OWASP Top 10**:
> - Sensibilizzare gli sviluppatori e le aziende sui principali rischi delle applicazioni web
> - fornire linee guida per proteggere le applicazioni da attacchi informatici
> - aiutare nella conformità a standard di sicurezza come GDPR, ISO 27001 e PCI-DSS



## **Injections**

**Repo**
[Payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings)


[Stile CTF portwigger](https://root-me.org)