#Networking 

# **A cosa serve?**
>Il modello ISO OSI è una mappa concettuale a **7 livelli** creata per standardizzare le comunicazioni in rete. Serve a capire dove vivono i dati e chi gestisce cosa.

# **Layer**

## Layer 1 (Fisico)
>Questo layer si occupa di gestire il mezzo trasmissivo (cavi e segnale). Riguarda lo stato elettrico/ottico del link, la velocità della scheda di rete, il duplex e la negoziazione Hardware.

>**Diagnostica Hardware e Stato fisico**
>Interroghiamo i driver di rete e il chip PHY
```shell
ethtool eth0
```

>Output importante:
>- Speed: X Mb/se Duplex: Full (prestazione del cavo)
>- Link Detected: yes (conferma che il cavo è collegato e c'è segnale elettrico/ottico)
>- Auto-negotation: on (indica se la velocità è stata negoziata automaticamente con lo switch)

---
## Layer 2 (Data Link)
>A questo livello non esistono gli indirizzi IP. La comunicazione avviene esclusivamente tra nodi adiacenti nello stesso dominio di broadcast  utilizzando i **MAC Address**

>Si occupa dell'incapsulamento dei pacchetti in Frame Ethernet, l' assegnazione dei MAC address, la gestione del MTU (Maximum Transmission Unit) e la risoluzion degli indirizzi tramite ARP.

>**Gestione Interfacce e Mac Address**
>Visualizza lo stato dell'interfaccia
```shell
ip link show dev eth0
```

>- **state** (indica lo stato dell'interfaccia UP=attiva DOWN=inattiva)
>- **link/ether** (indica il MAC address es. 52:54:00:12:34:56)

>Come gestire l'interfaccia via software:
```shell
# Attiva l'interfaccia (Administrative UP)
sudo ip link set dev eth0 up

# Disattiva l'interfaccia (Administrative DOWN)
sudo ip link set dev eth0 down

# Modifica il MAC address (utile per test di sicurezza o bypass filtri L2)
sudo ip link set dev eth0 down
sudo ip link set dev eth0 address 00:11:22:33:44:55
sudo ip link set dev eth0 up

# Modifica la MTU (es. per abilitare i Jumbo Frame in reti SAN/Storage)
sudo ip link set dev eth0 mtu 9000
```

>Usare anche dmesg per verificare errori:
```shell
sudo dmesg -T | grep -iE "eth0|link"
```

>Per inviare un pacchetto a un host nella stessa LAN il kernel deve conoscere il suo MAC address
```shell
ip n
```

>**Stati ARP**:
>- **REACHABLE**: l'associazione IP<->MAC è confermata e valida
>- **STALE**: l'associazione è valida ma non usata di recente, verrà verificata al prossimo traffico
>- **FAILED**: il kernel ha inviato richieste ARP ma nessuno ha risposto (nessun host con quell'IP  nella LAN)

>Invia frame ARP request direttamente all'IP specificato (verificare se un host è acceso anche se ha un firewall che blocca i ping)
```shell
arping -I eth0 192.168.x.x
```

---
## Layer 3 (Indirizzamento IP, Subnetting, Routing, Ip Forwarding)

### **Indirizzo IP e NetMask:**
>- Indirizzo IP, identifica univocamente un dispositivo sulla rete.
>- NetMask (/24) serbe al kernel per dividere la porzione di rete (192.168.1) da quella dell'host (.50). Quei 24 indica i numero di bit che identificano l'HOST

### **Tabella di Routing:**
>Quando un processo vuole inviare un pacchetto a un IP target il kernel legge la tabella per capire da quale interfaccia far uscire questo pacchetto e a quale Gateway deve consegnarlo.

### **Default Gateway (0.0.0.0/0)**
>Se la destinazione non appartiene a nessuna delle sottoreti note direttamente al server il pacchetto viene spedito qui. (Solitamente è il router della LAN)

### **IP Forwarding (net.ipv4.ip_forward**
>Di default se una macchina Linux riceve un pacchetto che non è destinato a se stesso lo scarta. Abilitando invece l'IP forwarding gli diciamo di agire da Router, smistando i pacchetti tra interfaccie diverse. Di default è uguale a 0

### **Gestione indirizzi IP**
```shell
#Mostra tutti gli IP configurati con notazione CIDR
ip -c addr show

#Assegna un IP a un'interfaccia (modifica volatile)
sudo ip addr add 10.0.0.5/24 dev ens33

#Rimuove un IP da un'interfaccia
sudo ip addr del 10.0.0.5/24 dev ens33
```

### **Ispezione Tabella routing**
```shell
#Visualizza la tabella di routing principale
ip r
```

>Output tipico del comando:
```shell
default via 10.30.20.1 dev wlan0 proto dhcp src 10.30.20.182 metric 600 
10.30.20.0/24 dev wlan0 proto kernel scope link src 10.30.20.182 metric 600 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
```

>Qualsiasi traffico non mappato va verso il default (10.30.20.1) tramite wlan0

>Aggiunta di una route
```shell
# Aggiungere una rotta statica verso una rete remota raggiungibile tramite un router interno
sudo ip route add 172.16.0.0/16 via 192.168.1.254 dev ens33

# Eliminare una rotta
sudo ip route del 172.16.0.0/16
```

### **Ip Forwarding**
```shell
# Verificare lo stato attuale (0 = disabilitato, 1 = abilitato)
sysctl net.ipv4.ip_forward

# Abilitare temporaneamente in memoria
sudo sysctl -w net.ipv4.ip_forward=1
```

### **Masquerading**
>Quando un pacchetto di un client parte da una rete privata (10.0.0.50) e deve arrivare ad un router in un'altra rete oppure Internet il server linux deve riscrivere l'intestazione del pacchetto in uscita (Masquerade / Source NAT).
>Sostituisce l'IP del client (10.0.0.50) con il proprio IP (192.168.1.100) si segna l'operazione su un registro interno (CTT, Connection Tracking Table) ed invia il pacchetto.
>Al ritorno fa il contrario. Controlla il CTT e cambia il suo IP in quello del client.

```shell
# 1. Ispeziona le regole attive
sudo nft list ruleset

# 2. Crea la tabella e la catena NAT se non presenti
sudo nft add table ip nat
sudo nft add chain ip nat postrouting '{ type nat hook postrouting priority 100 ; }'

# 3. Aggiunge la regola di Masquerade sull'interfaccia WAN
sudo nft add rule ip nat postrouting oifname "ens33" masquerade
```

>Spiegazione:
>- table ip nat: crea lo spazio per la manipolazione degli indirizzi
>- type nat hook postrouting: lega questa catena al momento esatto in cui il pacchetto sta per abbandonare la scheda di rete
>- priority 100: definisce l'ordine di esecuzione rispetto ad altre regole
>- oifname = "ens33": applica la regola solo ai pacchetti che escono tramite l'interfaccia ens33
>- masquerade: sovrascrive l'IP sorgente originale con l'IP attuale di ens33

---
## **Layer 4 (Trasporto TCP, UDP, Socket e Porte)**
>Il Layer 4 garantisce che il traffico arrivi allo specifico programma in esecuzione sul server (Process to Process)

### **Port**
>Un numero compreso tra 1 e 65535 che identifica il punto di accesso per uno specifico servizio software
>- well-known: riservate ai servizi di sistema (ssh 22, http 80, ecc...)
>- registered: usate da servizi applicativi (PostgreSQL 5432, Redis 6379, Docker 2375)
>- Ephemeral: porte temporanee allocate dinamicamente dal kernel per le connessioni

### **Socket**
>E' l'astrazione del software definita dalla combinazione univoca di:
```shell
Socket = IP Sorgente : Porta Sorgente <-> IP Destinazione : Porta Destinazione + Protocollo
```

### **TCP e UDP**

>**TCP**
>Orientato alla connessione. Prima di scambiare dati esegue il 3-Way Handshake:
>1. Client --> **SYN** (Voglio connettermi)
>2. Server --> **SYN ACK** (RIcevuto sono pronto)
>3. Client --> **ACK** (Mi connetto)

>**UDP**
>Non orientato alla connessione. Nessun handshake, zero controlli o garanzia di consegna. Massima velocità


### **Ispezione dei socket attivi**
```shell
sudo ss -tulpn
```
> - t : protocollo TCP
> - u: protoccolo UDP
> - l: mostra soltanto i socket in ascolto
> - p: mostra il nome del processo e il relativo PID
> - n mostra i numeri di porta e IP

---
## **Layer 5 (Sessione)**
>Stabilisce, coordina, sincronizza e termina le sessioni di comunicazione logica tra due processi applicativi.

### **Gestione del Controllo di Dialogo**
>Stabilisce chi può trasmettere e quando all'interno della sessione applicativa

### **Sincronizzazione e Checkpointing**
>Inserisce checkpoint all'interno di un flusso di dati prolungato.

### **Session Persistence e Recovery**
>Mantiene valida l'identità dell'utente o la sessione di lavoro anche quando la connessione di rete cambia (di conseguenza anche l'IP) o va giù.

### **RPC (Remote Protocol Call)**
>Permette a un programma su un server di eseguire codice su un server remoto come se fosse una funzione locale.

### **strace**
>Permette di intercettare le chiamate che un processo fa al kernel per creare e gestire i file descriptor
```shell
sudo strace -e trace=network -p PID
```
>Output tipico:
```shell
accept4(3, {sa_family=AF_INET, sin_port=htons(54321), sin_addr=inet_addr("192.168.1.10")}, ...) = 4
```

---
# **Layer 6 (Presentation)**
>Garantisce che i dati siano formattati, decodificati e cifrati correttamente prima di essere consegnati all'applicazione

### **Cifratura e Decifratura (SSL/TLS)**
>Si assicura che il traffico sia cifrato e verifica l'identità del server tramite certificati digitali.

### **Serializzazione e Formattazione dei dati**
>Converte strutture dati in memoria in un formato idoneo alla trasmissione sulla rete e viceversa

### **Handshake TLS**
![[tls_handshake.png.png]]


### **Ispezione del Handshake TLS e del certificato**
```shell
openssl s_client -connect app.azienda.local:443 -servername app.azienda.local
```

## **Estrazione Data di Scadenza del certificato**
```shell
openssl s_client -connect app.azienda.local:443 -servername app.azienda.local 2>/dev/null | openssl x509 -noout -dates
```

## **Certificati**

>Le CA fidate di sistema risiedono in directory standard:

>Debian/Ubuntu:
```shell
/etc/ssl/certs/
```

>Mentre per le CA private che devono essere riconosciute SOLO da determinati sistemi dovranno depositare i loro certificati all'interno della directory:
```shell
/usr/local/share/ca-certificates/

#E successivamente aggionare la lista delle CA di sistema con:
sudo update-ca-certificates
```

>Quando ci connettiamo ad un sito HTTPS:
1. Il server invia al tuo client il proprio certificato di dominio insieme ai certifiacti intermedi (**fullchain.pem**)
2. Il tuo sistema operativo risale la catena usandone le firme matematiche
   - verifica che il certificato di dominio sia stato firmato dall'intermediate CA
   - verifica che l'intermediate CA sia stato firmato dalla Root CA
   - controlla che la Root CA è presente nel proprio store locale

---
## **Layer 7 (Application, HTTP, DNS,  SSH e log)
>Verifica la logica del software e la sinstassi del protocollo

>A questo layer i software comunicano utilizzando regole definite dalle rispettive RFC.


>**I 3 principali protocolli sono:**

### 1. **HTTP / HTTPs
 >Request - Response

>**REQUESTS:**
>- GET (lettura)
>- POST (creazione)
>- PUT (modifica)
>- DELETE (elimazione)

>**RESPONSE**
>- 2XX (OK)
>- 3XX (REINDIRIZZAMENTO)
>- 4XX (CLIENT ERROR)
>- 5XX (SERVER ERROR)


### **2.  DNS**
>- Mappa i nomi leggibili dagli umani (FQDN) in indirizzi IP
>- Lavora sulla porta 53
>- Records:
>  A (IPv4)
>  AAAA (IPv6)
>  CNAME (Alias)
>  MX (Mail)
>  TXT (SPF/Verifiche)
>  PTR (Reverse DNS)
### **3. SSH**
>Protocollo per l'accesso e la gestione remota sicura.
>Porta 22