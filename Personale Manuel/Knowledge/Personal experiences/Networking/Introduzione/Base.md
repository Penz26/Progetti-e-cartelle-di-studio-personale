#Networking 

---
# **DISCLAIMER:
Tutti i dati e le informazioni sono state prese da il corso di tryhackme e tradotte da me in italiano in formato markdown per avere qualcosa di fisico e locale come appunti**

---
# **Cos'è una Network?**
>La risposta più semplice è una rete di dispositivi connessi tra di loro.
>Per essere chiamata tale una network deve essere composta da >= 2 dispositivi connessi tra di loro (es. telefono e router).

# **Qual'è la differenza allora con Internet ?!**
>Beh proprio nulla alla fin dei conti.

>Internet è semplicemente una gigantesca network che consiste di moltissime network più piccole al suo interno.

## **Storia**
>La prima forma di Internet è nata negli anni 60 ed era conosciuta come il progetto **ARPANET**.
>Il progetto era finanziato dal Dipartimento di Difesa degli Stati Uniti ed è stata la prima forma di Network documentata in azione.

>Ma non fu fino al 1989 che l'Internet che conosciamo oggi nacque grazie a Tim Berners-Lee che creò il World Wide Web (www).

>Come detto prima l' Internet è costituito da molti piccoli network collegati tra di loro.
>Questi piccoli NetWork sono chiamati "network privati" mentre i network che connettono questi piccoli network sono chiamati "network pubblici".

![[Internet.png]]

---

# **Riconoscere diversi dispositivi in una Network**

>Per comunicare e mantenere dell'ordine i dispositivi devono essere identificanti e identificabili. I dispositivi sono come gli umani, i quali possono essere identificati per:
>- nome
>- impronta digitale
>Possiamo cambiare nome, ma l'impronta digitale rimane unica.

>I dispositivi pure, hanno 2 identificatori, uno dei quali mutabile:
>- indirizzo IP
>- Indirizzo MAC (Media Access Control)

---

# **IP Address**
>Un indirizzo IP (Internet Protocol) può essere usato per identificare un dispositivo in una network per un periodo di tempo dove quell' IP può essere associato ad un altro dispositio senza che l'IP cambi.

>Vediamo ora come è struttura un indirizzo IP:
![[ip_address.png]]

>Un indirizzo IP è una serie di numeri divisi in 4 otteti. Il valore di ogni otteto si riassumerà all'indirizzo IP del dispositivo nella Network.
>Questo numero è calcolato grazie a una tecnica chiamata indirizzamento IP e subrete.
>Un indirizzo IP può cambiare da dispositivo a dispositivo ma non possono essere attivi allo stesso momento due IP uguali all'interno della stessa Rete.

>Gli indirizzi IP seguono degli standard chiamati Protocolli.
>Questi protocolli sono la spina dorsale delle reti e forzano molti dispositivi a parlare la stessa lingua.
>Come abbiamo detto prima i dispositivi possono essere in una rete pubblica oppure privata. In base alla rete a cui appartengono dipenderà anche il loro indirizzo IP, pubblico oppure privato.
>Uno pubblico è usato per identificare dispositivi in Internet, mentre uno privato sempre a identificare un dispositivo tra gli altri nella stessa rete.


| Nome Dispositivo | Indirizzo IP | Tipo indirizzo Ip |
| ---------------- | ------------ | ----------------- |
| DESKTOP-KJE57FD  | 192.168.1.77 | Privato           |
| DESKTOP-KJE57FD  | 86.157.52.21 | Pubblico          |
| CMNatic-PC       | 192.168.1.74 | Privato           |
| CMNatic-PC       | 86.157.52.21 | Pubblico          |
>I due dispositivi con l'IP privato usano i loro IP privati per comunicare tra di loro.
>Mentre i dati mandati in Internet da uno dei due dispositivi verranno identificati dallo stesso IP pubblico.
>Gli indirizzi IP pubblici vengono affidati dal proprio ISP (Internet Service Provider) dietro il pagamento di un quota.

>All'aumentare dei dispositivi che si connettono tra di loro diventa sempre più difficile avere degli IP pubblici univoci.
>Ci sono 2 versioni di IP
>- IPv4, quello che abbiamo appena visto (86.157.52.21) che arriva a 2^32                      (4 blocchi da 8 bit ciascuno) possibili indirizzi unici.
>- IPv6, una nuova versione del protocollo di indirizzamento IP per sistemare questo problema. Supporta 2^128 possibili indirizzi unici.
>  Esempio:
>  2a00:22c4:a531:c500:425f:cce6:c36b:f64d

---

# **MAC Address**
>I dispositivi su una rete hanno una interfaccia di rete fisica, ovvero una scheda microchip trovata nella scheda madre del dispositivo.
>A questa interfaccia di rete è affidata un unico indirizzo in fabbrica dove è stata costruita, questo indirizzo è chiamato MAC Address.

>L'indirizzo MAC è un codice esadecimale composto da 12 caratteri divisi per 2 da :
>I primi 6 caratteri (3 coppie) rappresentano chi ha creato quell'interfaccia
>Gli ultimi 6 caratteri sono unici per quella interfaccia.

>Un fatto interessante degli indizzi MAC è che possono essere falsificati con una tecnica chiamata spoofing. Ovvero quando un dispositivo sulla rete pretende di essere qualcun'altro con il suo MAC address

---

# **Ping**
>Il ping è uno degli strumenti fondamentali delle reti. Usa pacchetti ICMP (Internet Control Message Protocol) per determinare le performance di una connessione tra dispositivi o per vedere se la connessione esiste. Il tempo trascorso tra passare da un dispositivo all'altro è misurato direttamente da ping in ms.
>Per eseguire un ping basta fare:

```shell
ping IP_address 
#(oppure)
ping website_url
```