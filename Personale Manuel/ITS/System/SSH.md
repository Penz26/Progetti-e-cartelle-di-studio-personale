SSH (Secure Shell) 

SSH è un protocollo di rete crittografico che consente di accedere in modo sicuro a computer remoti attraverso reti non sicure.

Il protocollo opera sulla porta 22 e garantisce che tutte le comunicazione tra i client e server siano completamente cifrate, proteggendo credenziali, comandi e dati trasmessi da intercettazioni e attacchi man-in-the-middle.

Si basa su un sistema di crittografia asimmetrica basato su coppie di chiavi pubbliche e private per garantire la massima sicurezza nelle connessioni remote.

5 PASSI DA SEGUIRE:

1. Genereazione coppia di chiavi:
Viene creata una chiave privata (mantenuta segreta sul client) e una chiave pubblica (condivisa con il server)

2. Distribuzione della chiave pubblica
La chiave pubblica viene copiata sul server remoto nel file authorized_keys

3. Autenticazione Sicura
Durante la connessione, il server verifica l'identità del client usando la chiave pubblica, senza trasmettere password.

4. Sessione cifrata
Una volta autenticato, tutto il traffico viene crittografato end-to-end con algoritmi simmetrici come AES


Generare chiavi SSH

Comando ssh-keygen crea coppie di chiavi crittografate
Il processo di generazione crea due file:
-id_rsa         -la chiave privata
-id_rsa.pub     -la chiave pubblica

ssh-keygen -t ed25519 -C "PC-fisso-casa" (-C ci permette di dare un nome al computer per identificarlo)

Le chiavi vengono salvate in ~/.ssh/

Ora dobbiamo trasferire la chiave per fare la connesione
si usa il comando:

```Shell
ssh-copy-id nome_utente@ip_macchina
```

Chiederà per l'ultima volta la password della macchina ma dopo ciò si potrà loggare senza dover mettere la password
Per configurare al meglio l' SSH possiamo modificare nei file di configurazione sshd_config in etc/ssh/sshd_config

-Disabilitare accesso root, così da impedire il login diretto come root forzando l'uso di account utente + sudo
PermitRootLogin no

-Disabilitare Password, consentendo solo l'autenticazione a chiave pubblica
PasswordAuthentication no

-Limitare Utenti, restringe l'accesso SSH solo agli utenti specificati
AllowUsers user1 user2

-Cambiare Porta 
Port 2222
