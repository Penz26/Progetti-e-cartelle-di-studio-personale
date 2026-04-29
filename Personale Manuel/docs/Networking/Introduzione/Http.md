#Networking 

# **Cos'è l'Http?**
>L' HTTP (HyperText Transfer Protocol) è il protocollo che viene usato quando si visita un sito web.
>Ideato da Tim Berners Lee negli anni 90', stabilisce le regole usate per comunicare i server web per la trasmissione di pagine web, immagini, video, ecc...

# **Cos'è l'Https**
>L'HTTPs è la versione sicura dell'HTTP.
>I dati vengono criptati così bloccano i malintenzionati da vedere i dati che mandi e ricevi e dà anche la conferma che stai parlando con il server web giusto e non qualcosa che lo stia impersonando

---

# **Richieste e Risposte**
>Quando accediamo ad un sito il browser fa delle richieste al server web per valori come HTML, Immagini e risposte di download. Prima di ciò dovrai specificare al browser come e dove accedere alle risorse.
>Qui entra in gioco l'URL.

# **Cos'è un URL ?**
>Un URL (Uniform Resource Locator) è un'istruzione su come accedere ad una risorsa in internet.

![[url.png]]

>**Scheme:** dice che protocollo usare per accedere alle risorse (es. HTTP, HTTPs, FTP (file transfer protocol))

>**User:** certi servizi hanno bisogno di autenticazione per entrare

>**Host:** il nome di dominio o l'indirizzo IP del server che vuoi visitare

>**Port:** la porta a cui ti connetti, solitamente 80 per HTTP, 443 per HTTPs, ma questi valori possono essere cambiati tra 1-65535

>**Path:** il nome del file o la posizione delle risorse a cui si sta cercando di accedere

>**Query String:** informazioni extra che possono essere inviati attraverso il PATH (specifiche)

>**Fragment:** si riferiscono a una specifica posizione di contenuto nella pagina richiesta (evitare di scrollare la pagina a lungo)

---

# **Come fare una richiesta**

>Esempio di richiesta:
```http
GET 7 HTTP/1.1

Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/

```

>Analisi:

>1° riga: Questa richiesta manda il metodo GET alla pagina con / e gli dice che stiamo usando il protocollo HTTP versione 1.1.

>2° riga: Diciamo al web server che vogliamo la pagina tryhackme.com

>3° riga: Diciamo al web server che stiamo utilizzando il browser Firefox versione 87.0

>4° riga: Diciamo al web server che la pagina che ci ha reindirizzato a questa è https://tryhackme.com

>5° riga: DEVE ESSERE VUOTA PER DIRE AL WEB SERVER CHE LA RICHIESTA SI E' CONCLUSA

>Esempio di Risposta:
```http
HTTP/1.1 200 OK

Server: nginx/1.15.8
Date: Fri, 09 Apr 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98


<html>
<head>
    <title>TryHackMe</title>
</head>
<body>
    Welcome To TryHackMe.com
</body>
</html>
```

>Analisi: 

>1° riga: Ci dice che versione di protocollo HTTP il server sta usando, e lo status code (200 = successo)

>2° riga: Ci dice il software del web server e la versione

>3° riga: La data e ora odierna con la relativa Time Zone

>4° riga: Ci dice il tipo di contenuto che verrà inviato

>5° riga: Lunghezza dei dati che verranno passati

>6° riga: Vuota per concludere la risposta HTTP

>7-14° riga: L'informazione che è stata richiesta

---

# **Metodi HTTP**
>I metodi HTTP sono un modo per il client di vedere determinate azioni quando svolgono una HTTP request. Ci sono molti metodi HTTP, qui sotto quelli più importanti:

>**GET Request**
>Usata per ricevere informazioni da un web server

>**POST Request**
>Usata per inserire dati al server web e potenzialmente creare nuove istanze

>**PUT Request**
>Usata per aggiornare dati in un web server

>**DELETE Request**
>Usata per eliminare informazioni/istanze da un web server

---

# **Status Code**
>Quando un server HTTP risponde la prima riga della response contiene sempre lo status code che ci dice il risultato della request e come gestirle.
>Ci sono 5 range differenti di status code:

| **Intervallo Codici** | **Categoria**        | **Descrizione**                                                                                                                                                          |
| --------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **100-199**           | Risposta Informativa | Inviati per comunicare al client che la prima parte della richiesta è stata accettata e che deve continuare a inviare il resto. Questi codici non sono più molto comuni. |
| **200-299**           | Successo             | Questo intervallo di codici viene utilizzato per comunicare al client che la sua richiesta è andata a buon fine.                                                         |
| **300-399**           | Reindirizzamento     | Utilizzati per reindirizzare la richiesta del client verso un'altra risorsa. Può trattarsi di una pagina diversa o di un sito web completamente differente.              |
| **400-499**           | Errori del Client    | Utilizzati per informare il client che si è verificato un errore nella sua richiesta.                                                                                    |
| **500-599**           | Errori del Server    | Riservati agli errori che si verificano lato server; solitamente indicano un problema piuttosto grave nel modo in cui il server gestisce la richiesta.                   |

>Quelli più comuni sono:

| **Codice** | **Nome**                   | **Descrizione**                                                                                                                                                    |
| ---------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **200**    | OK                         | La richiesta è stata completata con successo.                                                                                                                      |
| **201**    | Creato                     | Una risorsa è stata creata (ad esempio un nuovo utente o un nuovo post sul blog).                                                                                  |
| **301**    | Trasferito Permanentemente | Reindirizza il browser del client a una nuova pagina o comunica ai motori di ricerca che la pagina si è spostata altrove e di cercarla lì.                         |
| **302**    | Trovato                    | Simile al reindirizzamento permanente, ma come suggerisce il nome, si tratta di un cambiamento solo temporaneo che potrebbe cambiare di nuovo nel prossimo futuro. |
| **400**    | Richiesta Errata           | Comunica al browser che qualcosa nella richiesta era sbagliato o mancante. Può essere usato se il server si aspettava un parametro che il client non ha inviato.   |
| **401**    | Non Autorizzato            | Non sei autorizzato a visualizzare questa risorsa finché non ti autentichi con l'applicazione web, solitamente tramite username e password.                        |
| **403**    | Proibito                   | Non hai il permesso di visualizzare questa risorsa, a prescindere che tu abbia effettuato l'accesso o meno.                                                        |
| **404**    | Pagina Non Trovata         | La pagina o la risorsa richiesta non esiste.                                                                                                                       |
| **405**    | Metodo Non Consentito      | La risorsa non permette il metodo di richiesta utilizzato; ad esempio, invii una richiesta `GET` a `/create-account` quando il server si aspetta una `POST`.       |
| **500**    | Errore Interno del Server  | Il server ha riscontrato un errore con la tua richiesta che non sa come gestire correttamente.                                                                     |
| **503**    | Servizio Non Disponibile   | Il server non può gestire la richiesta perché è sovraccarico o in manutenzione.                                                                                    |

---

# **Headers**
>Gli headers sono pezzi di dati extra che puoi mandare al web server per fare requests.

## Headers di request più comuni:

>**Host:** Certi Web server hostano più siti web, quindi specificandone uno gli puoi dire quale vuoi altrimenti riceveresti quella di default

>**User-agent:** Specifichiamo il nostro browser e la sua versione per formattare la pagina propriamente

>**Content-Length:** Quando si mandano dei dati ad un server web, come nei form, possiamo specificarlo al server quanti dati si deve aspettare. In modo che sia sicuro di non perdere dati

>**Accept Encoding:** Dice al web server che tipo di compressione supporta il browser così da comprimere i dati per trasmetterli via Internet

>**Cookie:** Dati mandati al server per ricordarsi le nostre informazioni

## Headers di risposta più comuni:

>**Set-Cookie:** Informazione conservata che viene reinviata al web server ad ogni richiesta

>**Cache-control:** Quanto tempo deve conservare il contenuto della risposta nella cache del browser prima di richiederla ancora

>**Content-Type:** Questo dice al client che tipo di dati è stato ritornato (HTML, CSS, Js, ecc...)

>**Content-Encoding:** Che metodo è stato usato per comprimere i dati per renderli più piccoli quando si mandano via Internet

---

# **Cosa sono i Cookie ?**
>I cookie sono piccoli pezzi di dati che vengono conservati sul tuo computer. I cookier vengono salvati quando si riceve un Header "Set-Cookie" da un web server.
>Così ogni altra request che fai, manderà i cookie al web server, che altrimenti non si ricorderebbe di chi sei. I cookie vengono utilizzati per ricordare impostazioni, preferenze, e se si ha mai visitato la pagina prima d'ora.