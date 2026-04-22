#CyberSecurity 

# **1.1**
>Alice vuole firmare digitalmente un documento. Usa la sua chiave pubblica per
firmarlo. Bob verifica con la chiave privata di Alice. La verifica fallisce. Quanti
errori ci sono e quali?

## **Risposta**
>Due errori:
>1. si firma con la chiave privata, si verifica con la chiave pubblica
>2. Bob non dovrebbe mai avere la chiave privata di Alice

---
# **1.2**
>Un sistema cifra ogni lettera A→1, B→2, … Z→26. 
>Un attaccante intercetta molti messaggi. Dopo 10 minuti ha decifrato tutto senza conoscere la chiave. Come?

## **Risposta**
>Analisi delle frequenze: in italiano/inglese certe lettere appaiono molto più spesso (E, A, I). 
>La sostituzione monoalfabetica non nasconde la distribuzione statistica.

---
# **1.3**
>Due utenti hanno la stessa password '1234'. Nel database i loro hash sono identici. L'attaccante che ha violato il DB capisce subito la password di entrambi. Come si sarebbe potuto evitare?

## **Risposta**
>Salting: aggiungere un valore casuale unico per utente prima di hashare. 
>Hash diversi anche a parità di password.

---
# **1.4**
>Un sito web salva

## **Risposta**
>

---
# **1.5**
>Un attaccante esegue ARP poisoning tra Cliente Gateway. Il client naviga normalmente non si accorge di nulla. Eppure l'attaccante legge tutto il il traffico HTTP.Il traffico HTTPS invece appare cifrato. Perchè?

## **Risposta**
>A causa del TLS Handshake con lo scambio di chiavi
>![[tls_handshake.png.png]]

---
# **1.6**
>Il Blue Team riceve un alert: negli ultimi 5 minuti ci sono stati  50000 tentativi di login falliti sull'account admin da 200 IP diversi. E' brute force classico o qualcos'altro? Come ci si difende in modo diverso nei due casi

## **Risposta**
 >E' un attacco distribuito (distributed brute force / credential stuffing). Un blocco su singolo IP non basta. Servono: rate limiting per account, CAPTCHA, MFA, blocco temporaneo dopo N tentativi, analisi comportamentale.
 
 ---

# **1.7**
>Un sito web implementa il reset della password così invia all'email dell'utente un link del tipo reset.php?user_id=42&admin=0. Un utente malizioso modifica il link in reset.php?user_id=1&admin=1. Cosa è andato storto e cosa non va bene?

## **Risposta**
>Il server si fida ciecamente dei parametri passati dal client (IDOR) combinato con privilege escalation via parameter tampering. Il parametro admin non dovrebbe mai esistere lato client: il ruolo va letto dal database in base alla sessione autenticata. Il user_id va validato as-is. La fix: token monouse opaco (es. **UUID** IDENTIFICATORE UNIVERSALE UNICO generato in modo casuale) memorizzato server-side senza alcun dato sensibile nell'URL

>**TOOL:** auth0 oppure 

>JWT (JSON WEB TOKEN)
>Un Token che permette di scambiare dati in modo sicuro. Composto da 3 parti: Header, Payload e Secret

>Header, un oggetto rappresentato con JSON e codificato in base64 che segue lo schema seguente:
>{
  "alg": "HS256",
  "typ": "JWT"
}
>alg, indica quale algoritmo è stato usato per generare la firma, la proprietà typ indica invece il tipo di token, in questo caso sarà sempre "JWT"

>Payload, contiene i dati chiamati claims, esistono 7 claims registrati e sono i seguenti:
>- `iss`: sta per issuer, dall'inglese emittente, ovvero specifica chi ha emesso il token, è solito specificare l'[hostname](https://it.wikipedia.org/wiki/Hostname "Hostname").
>- `sub`: è solito indicare con `sub` il soggetto che può essere un utente.
>- `aud`: l'audience, ovvero il pubblico, indica a chi è rivolto il token.
>- `exp`: con `exp` si indica la data di scadenza del token.
>- `nbf`: viene indicata la data in cui il token inizierà a valere.
>- `iat`: indica la data di creazione del token.
>- `jti`: viene utilizzato per identificare il token univocamente.

>Firma, serve per confermare la veridicità del token

# **1.8**
>Alice e Bob comunicano su un canale cifrato con TLS. Eve si mette nel mezzo e presenta ad Alice un certificato valido per banca.it, firmato da una CA che Eve ha compromesso. Alice si connette senza ricevere warning. Chi ha fallito e dove?

## **Risposta**
>Se una qualsiasi CA nell'elenco fidato del browser è compromesso, può firmare certificati per qualunque dominio. Eve ha eseguito un MITM su TLS reso possibile da una CA. Le contromisure reali esistono e si chiamano Certificate Transparency (CT logs): ogni certificato emesso deve essere registrato


>**TOOL:** Certbot
>Software Open Source che permette di creare certificati SSL gratuiti

SELECT * FROM users WHERE username='" + input + "'"

>Se l'utente inserisce:
'  OR '1'='1

SELECT * FROM USER WHERE username='"' OR '1'="'1'='1'".

