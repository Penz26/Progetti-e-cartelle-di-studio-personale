Il modello OSI (open systems interconnection) è stato sviluppato per aiutare la comunicazione tra diversi sistemi.

Ci sono 7 Livelli
-  Layer 1 - FIsico
- Layer 2 - Link dati
- Layer 3 - Network
- Layer 4 - Trasporto
- Layer 5 - Sessione
- Layer 6 - Presentazione
- Layer 7 - Applicazione

La maggior parte di dispositivi funzionano su più livelli del modello OSI.
Quando bisogna capire a che livello specifico operino bisogna determinare quale sia il livello più alto a cui operano, quello sarà il livello specifico.

---
# **Dispositivi Layer 1**

## Modem analogico
>I modem analogici erano stati sviluppati per prendere il segnale digitale proveniente da un nodo digitale (PC) e convertirlo ad un segnale analogo (modulazione) per essere inserito nel cavo.
>Al ritorno accetta un segnale analogo e lo traduce (demodulazione) in un segnale digitale in modo che il nodo possa capirlo.

>Erano stati creati per creare connessioni tra segmenti di rete tramite il (PSTN) usando il vecchio sistema dei telefoni (POTS)

>Provvedevano una singola connessione ad una rete

## **Hub**
>Funziona come un concentratore/ripetitore.
>Non gli interessa da dove arrivi il segnale o verso dove vada.

>Prende il segnale elettrico che arriva a una porta e lo ritrasmette su tutte le altre porte

>Può avere un numero di porte variante
>Sulle reti dei nostri giorni non viene utilizzato per vari motivi.

>Sostituito per la maggior parte dagli Switch

---
# **Dispositivi Layer 2**
## **Switch**
>Uno switch utilizza un circuito integrato applicazione-specifico chip (in inglese ASIC)

>Il chip ASIC permette allo switch di sapere quando uno switch è sulla rete e su che porta è connesso grazie al MAC address (Layer 2)

>Può avere un numero svariato di porte
>Comunica solo con i device della rete locale

## **Wap**
>Un wireless access point è uno specifico tipo di ponte che connette segmenti wireless della rete a segmenti cablati della rete.

>Il più comune tipo di WAP mette in ponte 802.11 segmenti wireless della rete con 802.3 segmenti ethernet della rete

>Comunica solo con device della rete locale

---
# **Dispositivi Layer 3**

## **Multilayer switch (MLS)**
>Un MLS permette normali operazioni di uno switch di layer 2 ma permette anche servizi del layer 3

>Il più comune MLS è uno switch di layer 3

>Non utilizza il chip ASIC solo per fare switching ma permette anche funzioni di routing. Questo permette ai dispositivi della rete locale di comunicare con dispositivi che non sono nella rete locale

>Può avre un numero di porte svariato

## **Router**
>Il router è il dispositivo più comune per connettere diverse reti utilizzando il Layer 3 del modello OSI

>Il router utilizza programmazione software per prendere decisioni, tra cui ricordarsi le varie reti e quale considera la miglior via per instradare verso quella rete

>Un router comunica con dispositivi della rete locale e dispositivi non nella rete locale.

---

# **Dispositivi di sicurezza**

## **Firewall**
>Un firewall può essere dentro un router od un nodo (Software based router) oppure un dispositivo a parte.

>Funziona su diversi layer del modello OSI.
>Specificatamente ai layer 2, 3,4 e 7.

>Blocca pacchetti da entrare o uscire dalla rete.

>Due modus operandi:

1. **Stateless inspection**
   Il firewall esamina ogni pacchetto con una serie di regole. Una volta che il pacchetto rispetta una regola, essa viene applicata al pacchetto e l'azione specificata viene eseguita.
2. **Stateful inspection**
   Il firewall esamina solo lo stato delle connessioni tra le reti.
   Specificamente quando una connessione è fatta da un dispositivo della rete locale verso un dispositivo al di fuori della rete locale il firewall non esaminerà alcun pacchetto proveniente dalla connessione esterna.
   Come regola generale connessioni esterne non hanno il permesso di essere inizializzate con dispositivi della rete interna.

# **IDS (Intrusion detection System)**
>Un IDS è un sistema passivo pensato per identificare quando una rete è sotto attacco. Solitamente pensato per informare un amministratore di rete quando un attacco è in effetto tramite file di log, SMS, email ecc...

>Un IDS non può prevenire o fermare attacchi per contro proprio.

>Riceve una copia di tutto il traffico e la valuta basandosi su degli standard:
- **Signature based:** analizza il traffico per malware conosciuto e strategie di attacco
- **Anomaly based:** analizza il traffico per cambiamenti  sospetti
- **Policy based:** valuta il traffico in base il traffico in base un policy di sicurezza

>Può essere implementato a livello di host (HIDS)


## **IPS (Intrusion prevention systems)**
>Un IPS è un sistema attivo pensato per fermare un attacco che danneggia la rete.
>Esegue un'azione o una serie di azioni per fermare l'attacco.
>Notifica anche l'amministratore di rete

>Tutto il traffico del segmento di rete passa attraverso l'IPS per entrare od uscire da quel segmento di rete. Come l'IDS il traffico è analizzato tramite una serie di standard

>Miglior piazzamento nella rete è tra il router e il segmento di rete di destinazione

>Programmato per una risposta attiva alla situazione:
- bloccare l'IP in attacco
- chiudere le interfacce vulnerabili
- terminare la sessione di rete
- redirezionare l'attacco
- altro...

## **VPN concentrator**
>Il concentrator permetterà tunneling e criptazione dipendente dal tipo di connessione VPN che è permessa. La maggior parte dei concentratori lavora su diversi layer del modello OSI (specificamente layer 2, layer 3 e layer 7). Al di fuori delle connessioni internet (che usano connessioni VPN SSL al layer 7) la maggior parte dei concentrator funzionano al layer di network (3) del modello OSI, provvedendo alla criptazione IPsec attraverso un tunnel sicuro

---

# **Dispositivi di ottimizzazione e performance**

## **Load balancer**
>Un dispositivo/sistema di rete usato per bilanciare  il carico di lavoro tra diversi host che contengono gli stessi dati per migliorare l'efficienza.
>Solitamente usato per distribuire le richieste (carico di lavoro) da un gruppo di server ai vari server in modo da assicurare che nessun server venga sovrautilizzato.

## **Server Proxy**
>Un server Proxy è un dispositivo/sistema che richiede le risorse per carico della macchina client.

>Solitamente utilizzato per ricevere dati da reti esterne non fidate per conto del client richiedente.

>Funzioni:
- Nasconde e protegge il client richiedente
- filtrare l'accesso solamente a fonti abilitate
- permette di velocizzare le performance di rete salvando in cache pagine web comunemente richieste.