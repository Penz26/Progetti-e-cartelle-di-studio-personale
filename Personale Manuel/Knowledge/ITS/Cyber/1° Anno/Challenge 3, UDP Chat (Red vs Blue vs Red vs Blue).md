#CyberSecurity 

# **Blue Team**
>Creare un server UDP (porta a scelta) a cui il blue team si connetterà
>Chattare, aggiungere nickname ed encryption

# **Red Team**
>Sniffare i messaggi della chat del blue team
>Scoprire la relazione nickname -IP

---

# **Server di Chat con ncat**

```shell
# Server
nc -k -u -l PORTA

# Client

nc -u -b IP-SERVER PORTA
```

# **Red Team**

```shell
sudo nmap -sn SUBMASK # scansionamo l'intera submask per vedere
sudo nmap -sU -p- IP
udp.port == PORTA   # filtro su wireshark
```

---

# **Ncat con certificati**

>Server:
```shell
openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt -subj "ChatServer"

# Crea una nuova chiave usando lo standard rsa:2048, un nuovo certificato che scade tra 365 giorni
```

>Server
```shell
ncat --ssl --ssl-cert server.crt --ssl-key server.key -lkv 4444
```