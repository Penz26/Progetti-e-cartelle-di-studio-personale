#Networking 

# **Network address translation (NAT)**
>Per conservare lo spazio degli indizizi IPv4 globali sono stati rimossi degli IPv4 dallo spazio pubblico di indirizzi e sono stati resi non instradabili a reti IPv4 pubbliche.

>Essere non instradabili previene l'indirizzo privato IPv4 dal comunicare con reti esterne pubbliche (es. Internet).
>**NAT risolve questo problema**

>Un router in NAT traduce l'indirizzo IPv4 in un IPv4 instradabile. Quando la risposta torna al router, questo la ripasserà indietro al dispositivo che ha fatto la richiesta.

![[NAT.png|551]]

>[!NOTE] Esistono 2 tipologie di NAT:
>NAT statico e NAT dinamico

---
# **NAT statico (SNAT)**
>Ad ogni indirizzo IP privato è assegnato uno specifico Indirizzo IP pubblico. Questa relazione è tenuta dal router.

- quando un dispositivo ha bisogno di accedere a reti esterne, il router prima traduce il suo indirizzo privato nel pubblico che gli è stato assegnato. Quando la risposta torna indietro il router ritraduce l'indirizzo pubblico nel corrispetivo privato
- questo processo non è flessibile

# **NAT dinamico (DNAT)**
>Il router in NAT assegna dinamicamente un indirizzo IP instradabile al dispositivo da una serie di indirizzi IP pubblici disponibili

 - quando un dispositivo locale deve accedere a risorse su reti esterne il router gli assegna l'indirizzo IP pubblico disponibile dalla lista. Quando la connessione con una rete esterna è finita quel indirizzo IP pubblico torna nella lista degli indirizzi disponibili
 - progettato per essere più flessibile di SNAT ma una volta che più reti necessitarono dell' accesso a reti esterne, la lista di indirizzi IP pubblici disponibili sarebbe dovuta ingrandirsi, altrimenti non si sarebbe potuta stabilire la connessione.

## **Port address translation (PAT)**
>PAT è un tipo di DNAT sviluppato per accrescere la scalabilità della NAT

- quando un dispositivo della rete locale necessita dell'accesso a reti esterne, il router in NAT assegna dinamicamente l'indirizzo IP pubblico al dispositivo **con l'aggiunta** di assegnare dinamicamente un numero di porta alla fine dell'indirizzo IP pubblico
- il router tiene traccia degli indirizzi IP e delle porte per assicurare che la connessione sia instradata da e verso il giusto dispositivo
- PAT ha sempre bisogno di una lista di indirizzi IP pubblici, ma la lista può contenere anche solo un indirizzo IP pubblico (o anche di più per una rete privata più larga)

>Grazie a PAT vengono utilizzati meno indirizzi IPv4 pubblici e sono gestibili in modo migliore.

---

# **Terminologia**

>**Indirizzo interno locale:** un indirizzo IP sulla rete locale privata

>**Indirizzo interno globale:** un indirizzo IP pubblico che si riferisce ad un dispositivo interno alla rete locale.
>L'indirizzo IP pubblico assegnato dal router al dispositivo richiedente per stabilire la connessione a reti esterne.

>**Indirizzo esterno globale:** un indirizzo IP pubblico che riferisce ad un dispositivo esterno dalla rete locale

>**Indirizzo esterno locale:** un indirizzo IP privato assegnato ad un dispositivo esterno
>L'indirizzo IP privato assegnato al dispositivo esterno all'interno della rete locale

![[terminologia-NAT.png|642]]