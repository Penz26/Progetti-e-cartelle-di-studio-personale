#Ret-ITS -ITS
3 Classi di Indirizzo IPv4 [Classi](https://it.wikipedia.org/wiki/Indirizzo_IP_privato)

![[IPv4_classi.png]]

Usare altri indirizzi IP fuori da queste classi CREA problemi nella rete, certi dispositivi di rete non lo consentono direttamente.

IL DNS se trova degli indirizzi Pubblici dentro la rete privata non reinderizzerà il pacchetto in rete ma rimarrà all'interno della rete privata

---
## DHCP
>Il dhcp rilascia e gestisce:
- IP di rete
- Subnet Mask
- default gateway


>L'HyperVisor (server principale) è meglio dividerlo in una VLAN separata. Dobbiamo fare arrivare il traffico solo alle VM con i servizi a cui si devono collegare i colleghi. Ma non devono collegarsi al Server direttamente altrimenti ci potrebbero essere problemi di sicurezza.

>La VLAN del server è 1, chiamata anche di Management

>Le Varie VLAN sono diverse strade,
>I server sono collegati tramite Switch e le sue varie porte con i loro vari TAG 1, 10, 20, 30, ecc.. riesce a far passare i pacchetti solo se specificato.

>Se un attaccante entra in un PC di un collega tramite la sua rete, quel PC è collegato alla VLAN 20 NON quella MANAGEMENT 1, quindi sarà più difficile per lui escalare al server di virtualizzazione

---

# Firewall e DHCP

>Il Firewall server per filtrare le pagine con un web filter alle pagine che l'utente possa visitare, oppure sulle app da bloccare da andare in rete (es. outlook).
>Il firewall funziona perimetralmente e si possono configurare più WAN

>Prima del firewall c'è il modem che permette di collegarsi ad Internet
>La fibra essendo segnale luce deve essere tradotta in segnale ethernet (elettrico), quindi entra in WAN ma viene tradotto dall' ONT (Optical Network Terminal)

--- 

Proxmox no RAID
Windows Server si RAID con i controller

Tipi di raid usati 0,1,5,6,10

Synologi