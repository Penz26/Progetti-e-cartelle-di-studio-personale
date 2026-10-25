#CyberSecurity 

# **Cos'è?**
>Hydra è un password cracker con svariate feature e comodità che lo rendono veloce, flessibile e architettato in modo da effettuare attacchi a dizionario oppure bruteforcing.


# **Installazione**

>Sempre la stessa roba
```Bash
sudo apt update
sudo apt install hydra
```
---

# **Comandi e flag più importanti**

>Attacco basilare, si prova un attacco con un username con una relativa password verso un indirizzo IP verso un protocollo (porta)
```Shell
hydra -l <username> -p <password> <ip_address> <protocollo>
```

>Esempio:
```Shell
hydra -l pippo -p 12345 192.168.1.26 ssh
```

```Shell
-h --help   Mosta tutte le flag e vari esempi per ogni caso

-l <username>   Esegue un attacco usando quel username per il campo username

-p <password>    Esegue un attacco usando quella password per il campo password

-L <nome_file.ext>   Esegue un attacco verso tutti gli username contenuti dentro il file specificato

-P <nome_file.ext>   Esegue un attacco che prende come password tutte le stringhe all''interno del file

-v        Verbosità del programma (descrive quello che sta facendo)

-d        Modalità DEBUG, specifica ogni suo singolo processo

-o <nome_file_salvataggio>      Specifica dove reinderizzare l''output del suo lavoro

-R       RESUME, se la sessione di hydra crasha può riprendere normalmente da dove si era fermato

-s      Permette di specificare una porta (se per esempio qualcuno cambia la porta di ssh in 2222 puoi specificare con -s 2222 la porta)
ESEMPIO:

hydra -L username.txt -P rockyou.txt 192.168.1.55 ssh -s 2222

-M <nome_file.ext>     Permette di attaccare più dispositivi specificando il file in cui si hanno salvati gli IP address
ESEMPIO:

192.168.1.100
192.168.1.101
192.168.1.102

-C <nome_file.ext>    Permette di provare delle combinazioni di username e password specificate nel file.
ESEMPIO:

pippo:12345
giorgio:password
filippo:qwerty
ecc...
```



![[password_spraying.png]]