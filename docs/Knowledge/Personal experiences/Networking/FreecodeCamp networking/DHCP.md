#Networking 

# **Come fa un computer a sapere quale Ip avere?**
>Un computer riceve la sua configurazione IP da un **DHCP** (Dynamic Host Configuration Protocol) server. Non solo questo ma dice anche al PC qual'è il default gateway e anche come trovare il server DNS.

Un computer può ricevere la sua configurazione IP in  2 modi:
1. **Staticamente** (ovvero settato manualmente)
2. **Dinamicamente** (tramite un servizio come un DHCP)

---
## **Assegnazione IP Statica**
>L'amministratore assegna un IP e subnet mask ad ogni host nella rete.
>
>Assegna anche un gateway predefinito e un server DNS ad ogni host.
>Necessari se è richiesto l'accesso a reti esterne (gateway predefinito) e una nominazione delle risorse in rete è configurata (DNS server)

>[!NOTE] Ogni volta che una modifica è stata fatta ogni configurazione dovrà essere aggiornata.

## **Assegnazione IP Dinamica**
>L'amministratore configura un server DHCP per gestire il processo si assegnazione.
>Il server DHCP ascolta su una specifica porta per informazioni di richiesta IP.
>Una volta che riceve la richieste il server risponde con l'informazione richiesta.

---
# **Processo assegnazione Dinamica (DHCP)**

1. All'avvio un PC configurato per richiedere un IP manda un **pacchetto di scoperta (discovery packet)** all'indirizzo di broadcast **(255.255.255.255:67)**
2. Il server DHCP riceve il pacchetto di scoperta e risponde con un **pacchetto d'offerta (offer packet)** . Questo viene inviato al indirizzo MAC del richiedente usando la porta **UDP 68**
3. Il computer lo riceve il pacchetto d'offerta dal server DHCP e gli manda un **pacchetto di richiesta (request packet)** che gli permette di richiederela giusta configurazione IP al server DHCP
4. Una volta che il server DHCP riceve il pacchetto di richiesta manda al computer il **pacchetto di riconoscimento(acknowledgement packet)** che contiene la configurazione IP richiesta.
5. Una volta ricevuto il pacchetto di riconoscimento il PC cambia la sua configurazione per riflettere le informazioni ricevute

![](http://neptunet.fr/intro-dhcp/http://neptunet.fr/intro-dhcp/http://neptunet.fr/intro-dhcp/http://neptunet.fr/intro-dhcp/http://neptunet.fr/intro-dhcp/)
![[DHCP-procedure.png]]

## Componenti del processo

>**Porte Usate**:
- PC manda il **discovery packet** in broadcast 255.255.255.255:67 (Porta 67 UDP)
- Server DHCP manda **offer packet** all'indirizzo MAC del PC sulla porta 68

>**Range degli Indirizzi**:

L'amministratore configura il range di indirizzi IP che possono essere dati

>**Prenotazione d'indirizzo**:

L'amministratore riserva specifici indirizzi IP da essere dati **SOLAMENTE** a determinati indirizzi MAC.

>Questi sono usati da dispositivi che dovrebbero sempre avere lo stesso indirizzo IP (es. server e routers)
>Permette di cambiare questi indirizzi da un centro di controllo unico invece che dover entrare in ognuno dei singoli dispositivi.

>**Periodo di tempo valido**:

I parametri di configurazione valgono solo per un determinato periodo di tempo. Questo periodo di tempo è configurato dagli amministratori.

>**Opzioni**:

- Indirizzo del gateway predefinito
- Indirizzi dei server DNS da utilizzare (ce ne possono essere più di uno)
- indirizzi dei Time server
- altre opzioni...

>**Configurazioni Ip preferiti**:

Un pc può avere un indirizzo IP preferito
L'amministratore può configurare il server DHCP per rispettare la preferenza oppure ignorarla.

---
>Sotto determinate circostanze un server DHCP può non essere sul segmento di rete locale:

Trasmissioni di tipo broadcast non possono passare attraverso un router. Se non c'è un server DHCP sul segmento della rete locale il router può essere configurato per diventare un **ripetitore DHCP (DHCP relay)**.

Quando un relay DHCP riceve un **discovery packet** da un PC, manderà questo pacchetto al segmento di rete in cui esiste il server DHCP

Questo permette di avere meno server DHCP configurati in una rete.