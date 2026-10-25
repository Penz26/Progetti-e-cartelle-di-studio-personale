#Linux #Networking 

# Che cos'è?

>IPTables funge da interfaccia per Netfilter, il framework del kernel Linux dedicato al filtraggio dei pacchetti, alla traduzione degli indirizzi e al tracciamento delle connessioni.

>L'architettura si basa su tre componenti principali:
>1. [Tabelle](#Tables)
>2. [Catene](#Chains)
>3. [Regole](#Rules)

---
# **Tables**

>Le tabelle servono a classificare le regole in base al tipo di operazione o decisione che deve essere presa sul pacchetto

| **Tabella** | **Scopo Principale**                                                       |
| ----------- | -------------------------------------------------------------------------- |
| Filter      | predefinita per il filtraggio del traffico (ACCEPT, DROP, REJECT)          |
| NAT         | Utilizzata per la traduzione degli indirizzi (Network Address Translation) |
| Mangle      | Utilizzata per modifiche specializzate ai pacchetti                        |
| Raw         | Esentare certi pacchetti dal tracciamento della connessione                |
| Security    | utilizzata per hook legati a SELinux                                       |

---

# **Chains**

>Le catena solo elenchi ordinati di regole associati direttamente ai ganci di Netfilter.
>Le catene definiscono quando un pacchetto viene esaminato

>Chains predefinite:
>- **Prerouting:** pacchett in in entrata prima delle decisioni di routing
>- **Input:** pacchetti destinati al server locale
>- **Forward:** pacchetti instradati attraverso il server
>- **Output:** Pacchetti generati dal server locale
>- **Postrouting:** Pacchetti in uscita dopo le decisioni di routing

---
# **Rules**

>All'interno di ciascuna catena, un pacchetto viene confrontato sequenzialmente (dall'alto verso il basso) con le regole inserite.

>Ogni regola contiene:
>1. Un criterio di di corrispondenza (Match): definisce le condizioni che il  pacchetto deve soddisfare
>2. Un'azione (Target): l'operazione da eseguire se il pacchetto soddisfa le condizioni. I target si dividono in:
>   - Terminanti: interrompono l'elaborazione del pacchetto in quella specifica catena (ACCEPT, DROP, REJECT)
>   - Non terminanti: compiono un'azione (come LOG per registrare i log nel syslog o MARK per etichettare il pacchetto) e consentono alla catena di continuare a valutare le regole successive

>Se un pacchetto attraversa l'intera catena senza incontrare alcuna regola corrispondente, verrà applicata la policy predefinita stabilita per quella catena (solitamente configurata su ACCEPT o DROP)

---
# Port Forwarding e NAT

>Il port forwarding è il processo di reinderizzamento di una richiesta da una porta specifica a un altro host o porta.
>Questo processo si basa su due operazioni chiave:
>1. **DNAT (Destination NAT):** riscrive l'indirizzo di destinazione dei pacchetti in entrata. Si configura nella catena PREROUTING della tabella nat.
>2. **SNAT (Source NAT)** Riscrive l'indirizzo sorgente dei pacchetti in uscita affichè le risposte possano tornare correttamente atrraverso il gateway. Si configura nella catena POSTROUTING

>[!IMPORTANT] Affinchè il port forwarding funzioni, inoltre IP deve essere abilitato a livello di kernel tramite il comando:

```shell
sysctl net.ipv4.ip_forward=1
```