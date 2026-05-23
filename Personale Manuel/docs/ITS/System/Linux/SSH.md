#Linux 

# **SSH (Secure Shell)** 
>SSH è un protocollo di rete crittografico che consente di accedere in modo sicuro a computer remoti attraverso reti non sicure.

>Il protocollo opera sulla porta 22 e garantisce che tutte le comunicazione tra i client e server siano completamente cifrate, proteggendo credenziali, comandi e dati trasmessi da intercettazioni e attacchi man-in-the-middle.

>Si basa su un sistema di crittografia asimmetrica basato su coppie di chiavi pubbliche e private per garantire la massima sicurezza nelle connessioni remote.

# **4 PASSI DA SEGUIRE:**

1. Genereazione coppia di chiavi:
	Viene creata una chiave privata (mantenuta segreta sul client) e una chiave pubblica (condivisa con il server)
	Le Chiavi verrano salvate in tilde/.ssh/
```Shell
ssh-keygen -t ED25519 -C "Nome identificativo"
#(-C ci permette di dare un nome al computer per identificarlo)
```

2. Distribuzione della chiave pubblica
	La chiave pubblica viene copiata sul server remoto nel file authorized_keys
```Shell
#Di default ssh gira sulla porta 22 quindi quando non si specifica userà quella
ssh-copyid nomeUtenteServer@IP

#Se si vuole cambiare la porta fare
ssh-copy-id -p 2222 nomeUtenteServer@IP
```

3. Autenticazione Sicura
	Durante la connessione, il server verifica l'identità del client usando la chiave pubblica, senza trasmettere password.
```Shell
ssh nomeUtenteServer@IP 	
```

4. Sessione cifrata
	Una volta autenticato, tutto il traffico viene crittografato end-to-end con algoritmi simmetrici come AES

--- 

>Per configurare al meglio l' SSH possiamo modificare nei file di configurazione sshd_config in:
>etc/ssh/sshd_config

- -Disabilitare accesso root, così da impedire il login diretto come root forzando l'uso di account utente + sudo
```Shell
PermitRootLogin no
```

- Disabilitare Password, consentendo solo l'autenticazione a chiave pubblica
```Shell
PasswordAuthentication no
```

- Limitare Utenti, restringe l'accesso SSH solo agli utenti specificati
```Shell
AllowUsers user1 user2
```

- Cambiare Porta 
```Shell
Port 2222
```

>**Possiamo inoltre evitare di scriver ogni volta nomepc@IP facendo:
```Shell
#All'interno di tilde/ssh
#Creare o aprire il file config e al suo interno scrivere:

Host mioserver
    HostName 192.168.1.50 (IP della macchina)
    User iltuonomeutente  (Nome dell''utente della macchina)
	Port 22               (Porta da usare)

```

---

# Se si cambia PC o si vuole aggiungere un altro Pc:

>Generare ssh-key per verificare che siamo noi a github
```
ssh-keygen -t ed25519
```

>Successivamente andare nella directory di .ssh e trovare la public key
>~/.ssh/id----.pub

>Incollare questa chiave nelle impostazioni di chiavi ssh per il proprio profilo github
