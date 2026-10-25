#Networking 

# **Come operano i Siti Web**

>Quando visitiamo un sito web il nostro browser fa una richiesta ad un web server chiedendo per informazioni riguardo la pagina che vogliamo visitare. Questo risponderà con i dati che il browser userà per mostrare la pagina.
>Un Web Server è un computer da qualche parte nel mondo che si occupa di risolvere le tue richieste.

>Ci sono 2 principali componenti di un sito web:
>1. Front-end (Lato Client) il modo in cui il browser visualizza il sito
>2. Back-end (Server Side) il server che processa le richieste e risponde con i dati che il browser usa per mostrare le informazioni.

---

# **Da cosa sono formati i siti web**

>I siti web sono creati usando:
>- HTML, per creare siti e definirne la struttura
>- CSS, per rendere il sito più bello aggiungendo opzioni di stile
>- Javascript, per implementare features interattive alla pagina

## **Html:**
>HyperText Markup Language (HTML) è il linguaggio con cui i siti sono scritti. Gli elementi che compongono la pagina sono chiamati TAG e dicono al browser come mostrare il contenuto della pagina.

>Struttura tipica di una pagina:

```html
<!DOCTYPE html>, definisce che la pagina è un documento HTML5. Aiuta il browser a capire come interpretare la pagina
<html> elemento di root, senza esso non funziona
<head> contiene informazioni riguardo la pagina (es. titolo)
<body> all'interno del body vengono messi tutto quello che deve essere visualizzato dall'utente
<h1> Titoli
<p> paragrafi

Ce ne sono molti altri ecc...
```

>I Tag possono anche contenere delle istruzioni per lo stile degli elementi
>p class="bold-text" , raggruppa degli elementi che avranno stesse configurazioni di stile
>img src="img/cat.jpg" , dice il path dell'immagine
>ecc...

## **JavaScript**

>JavaScript è uno dei linguaggi di programmazione più popolari al mondo e permette alla pagina di diventare interattive.
>L'HTML è usato per creare la struttura mentre javascript viene usato per controllare le funzionalità della pagina. 
>JS può aggiornare dinamicamente la pagina in tempo reale.

>Javascript è aggiunto all'interno del codice della pagina aprendo il tag script e scriverlo direttamente lì, ma ciò crea molto disordine e si preferisce aprire il tag ed aggiungere src="path/dello/script"

>Esempi:

```JS
//Questo script trova un elemento nell'html con l'id demo e ne cambia il contenuto con quello dopo l'uguale
document.getElementById("demo").innerHTML = "Hack the Planet";

//
```

---

# **HTML Injection**

>L'html injection è una vulnerabilità che avviene quando input dell'utente non filtrato viene mostrato sulla pagina.

![[html-injection.png]]

>La regola generale è non fidarsi mai di quello che l'utente possa inserire. 
>Per prevenirlo i dev dovrebbero sanitizzare tutto quello che l'utente inserisce prima di usarlo nella funzione JavaScript, in questo caso l'utente potrebbe rimuovere tag html.

---

# **Load balancing**
>Quando il traffico di un sito web inizia ad essere abbastanza pesante o fa girare una web application che necessita di grande raggiungibilità un solo server web potrebbero essere poco.
>I bilanciatori di traffico (load balancers) ricevono la tua request e successivamente la mandano ad uno dei molteplici web server che esistono per quella task.. Usano diversi algoritmi che aiutano a decidere a che web server reinderizzare la richiesta.
>Esempi:
>**round-robin:** manda la request ad ogni web server a turno
>**weighted:** che controlla quante richieste stia gestendo ogni server e manda la richiesta a quello più  libero.

>I Load balancers inoltre effettuano dei controlli periodici ad ogni server per rassicurare che stiano girando correttamente, questi controlli sono chiamti **health checks**, se il balancer vede che un server non risponde smetterà di reinderizzare il traffico a quel server.


## **CDN (Content Delivery Networks)**
>Un CDN può essere un ottimo modo per tagliare traffico ad un sito molto visitato. Permette di hostare file statici dal tuo sito, come Javascript, Immagini, Video, ecc... e hostarli tra mille altri server nel mondo. Quando un utente fà una richiesta a uno di quei file, il CDN controlla dove sia il server più vicino e gli manda la richiesta.

## **Database**
>Quasi sempre un sito ha bisogno di un modo per conservare informazioni dei loro utenti. I server web possono comunicare con i Database per conservare o richiamare dati da loro. Possono essere semplici file di testo o cluster di molteplici server che aiutano con velocità e resilienza.

## **Waf (Web Application Firewall)**
>Il WAF sta tra il server web e la richiesta dell'utente, la sua principale funzione è quella di proteggere il web server da tentativi di hacking o DOS (denial of service). Analizza la richiesta per attacchi comuni, se la richiesta è fatta da un vero browser o da un bot. Può anche controllare se un eccessiva quantità di richiesta siano fatte attraverso il **rate limiting**, che permetterà solo un determinato numero di richieste al secondo da un IP. Se una richiesta viene interpretata come un potenziale attacco non verrà passata al server.

---
 # **COS'E' UN WEB SERVER**
 >Un server web è software che ascolta per connessioni in arrivo e dopo utilizza il protocollo HTTP per inviare il contenuto del sito al cliente (es. Apache, Nginx, NodeJs, ecc...). 
 
 >Un server web invia i file che sono contenuti nella **root directory**, che è definita nelle impostazioni del software.
 >In Linux (/var/www/html)
 >In Windows (C:\inetpub\wwwroot)
 >Se per esempio si richiede il file https:\\www.esempio.com/picture.jpg, questo manderebbe il file contenuto localmente nel server alla directory /var/www/html/picture.jpg
 
 ## **Virtual Hosts:**
 >Un web server può hostare molteplici siti web con diversi nomi di dominio, per farlo usano i virtual hosts (configurazioni text-based nei file di configurazione).
 >Il server Web controlla per l'hostname che viene richiesto dagli header della richiesta HTTP e lo fa combaciare con i suoi virtual hosts. Se ne trova uno che combacia lo mostra, altrimenti verrà mostrato quello di default.
 
 >I Virtual Hosts possono avere diverse root directory sul disco.
 >Esempio:
 >one.com - /var/www/website_one (con all'interno i relativi file HTML, ec...)
 >two.com - /var/www/website_two
 >Non c'è un limite alla quantità di virtual host che si possono configurare
 
 ---

# **Static vs Dynamic Content**

>Contenuto statico = contenuto che non cambia nulla.
>Immagini, javascript, CSS, HTML che non cambia. Sono file che sono direttamente serviti al client senza cambiamenti

>Contenuto Dinamico = contenuto che cambia in base alle varie richieste. Pagine che cambiano in base ad aggiornamenti, ricerche, ecc...
>Questo viene gestito dal backend.

## **Scripting e linguaggi di Backend**
>Questi linguaggi interagiscono con database, servizi esterni, processare dati dall'utente e molto altro. 
>Si può fare di tutto con essi.
>Esempi di linguaggi backend: PHP, Python, Ruby, NodeJS, Perl, ecc...

