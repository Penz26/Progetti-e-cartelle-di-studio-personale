#CyberSecurity 

# **1. Creare una connessione con un'allow list**
>Limitare chi può connettersi al nostro server ci permette di sapere senza preoccupazioni chi posso collegarsi e chi no.

```Shell
ncat -lkv --allow IP_macchina_abilitata
#Con la flag --allow permettiamo solo a gli ip specificati di connettersi a tale server
```

- Possiamo anche creare dei file txt che permettono di essere letti e usati come parametro per specificare chi può entrare e chi no
```Shell
ncat -lkv --denyfile deny.txt
#Tutti gli IP scritti al suo interno NON potranno entrare

ncat --lkv --allowfile allow.txt

```

# **2. Avere dei Log di tutto quello che è stato passato sul server**
>Permette di direzionare gli output ricevuti da un server su un file

```Shell
ncat -lkv -o output.txt
```

# **3. Criptare le comunicazioni e usare i certificati per evitare MITM**

```Shell

#Server
ncat -lkv --ssl --ssl-cert cert.pem --ssl-key key.pem

#Client (anche lui con certificati SSL)
#Usa i certificati per assicurarsi che si stia connettendo al server corretto
ncat nome_server -v --ssl-verify --ssl-trustfile cert.pem

```

# **4. Far girare degli script tramite Ncat**

```Shell
ncat -lkv --exec percorso_script

#Il client quando si connetterrà al server avrà subito in esecuzione lo script

```

# **5. Fare richieste HTTP tramite file**

```Shell
#Creiamo un file con dentro questi parametri

RICHIESTA HTTP 
Host: NOME-SERVER

#Esempio:

GET /ip HTTP/1.1
Host: ipinfo.io

#Buttiamo in pasto a Ncat il file attraverso il |

cat nome_file | ncat --ssl ipinfo.io 443 #porta utilizzata per HTTPS

```