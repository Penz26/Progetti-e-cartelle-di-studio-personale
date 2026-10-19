>Una vpn è usata da un host remoto per accedere a una rete private tramite un tunnel criptato attraverso una rete pubblica.

Una volta che la connessione VPN è stata eseguita l' host non viene più considerato remoto, viene visto dalla rete privata come un host locale.

Anche se la connesione passa attraverso diversi router e sistemi viene visto da entrambe le parti come una connessione diretta.

---
## **Tipi di VPN**

1. **Site-to-site VPN**
   Permette alla rete di un sito remoto di connettersi al sito principale e venir visto come un segmento di rete locale.
   Concentratori VPN da entrambe le parti della VPN controlleranno la connessione
2. **Remote-access VPN (host-to-site VPN)**
   Permette allo user remoto di accedere alla rete locale
   Un concentrator VPN nella rete locale controllerà la connessione proveniente dallo user remoto
   Il sistema remoto che crea la connessione usa un software speciale, chiamato VPN client software, per creare la connessione.
3. **Host-to-host VPN (SSL VPN)**
   Permette una connessione sicura tra 2 sistemi senzaa l'utilizzo di un VPN client software
   Un concentratore VPN nella rete locale controlla la connesione
   L' host che cerca di connettersi usa un web browser che supporta la corretta tecnologia di criptazione (SSL o TLS) per la connessione al concentratore VPN

---

# **Protoccli utilizzati da una VPN**

## **Internet Protoccol security (IPsec)**
>Lavora al layer 3 del modello OSI e sopra

Può essere usato con il protocollo **Authentication Header (AH)**
>[!NOTE] Garantisce solo l'autenticazione non la criptazione

Può essere usato con il protocollo **Encapsulating Security Payload (ESP)**
>[!NOTE] ESP garantisce sia l'autenticazione che la criptazione dei pacchetti (metodo più popolare)

>Sia AH che ESP possono operare in due modi:
1. Può essere usato in **transport mode** tra due dispositivi (host-to-host VPN)
2. Può essere usato in **tunner mode** tra due endpoints (site-to-site VPN)

>IPSec implementa **Internet Security Association and Key Management (ISAKMP)** di default

>ISAKMP provvisiona un metodo per trasmettere chiavi di sicurezza e dati di autenticazione tra due sistemi, al di fuori del processo di generazione di chiave sicura.


## **Generic Routing Encapsulation (GRE)**
>GRE è un protocollo di tunneling capace di incapsulare una grande varietà di protocolli al layer network

>Usato spesso per creare un sub-tunnel con una connessione IPSec

>IPSec trasmette pacchetti unicast (comunicazione 1 a 1). 
>In molti casi c'è bisogno di trasmettere pacchetti multicast (comunicazione 1 a qualche communicazione) oppure broadcast (comunicazione 1 a molti) pacchetti attraverso connessioni IPsec.
>Utilizzando GRE questo può essere fatto.

## **Point-to-Point Tunneling Protocol (PPTP)**
>Versione più vecchia che supportava connessioni VPN dial-up. 


---
## **Trasport Layer Security (TLS) Protocol**
>TLS è un protocollo di criptazione usato per creare connessioni criptati sicure tra 2 dispositivi o applicazioni.

Usa la crittografia asimmetrica per autenticare gli endpoint e successivamente negozia una chiave simmetrica di sicurezza usata per criptare la connessione.


>TLS ha sostituito il protocollo Secure Socket Layer
>Lavora al layer 5 del modello OSI

>Utilizzo più comune creare una sessione ad Internet criptata (SSL VPN)

## **Secure Socket Layer (SSL) Protocol**
>Protocollo crittografario simile ma più vecchio di TLS

>Utilizzo più comune nelle transazioni via Internet