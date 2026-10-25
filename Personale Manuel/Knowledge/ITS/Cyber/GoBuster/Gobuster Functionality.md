#CyberSecurity 

# **Cos'è?**
>Gobuster è un cracker di directory web, viene utilizzato in penetration testing per trovare web directories in siti così da poterli espugnare successivamente con altri password manager (Es. Hydra, John The Ripper, ecc...)

# **Installazione**
>Gobuster è buildato con go, un linguaggio di programmazione pensato per essere sicuro.
>Quindi bisogna prima installare go:
```Bash
sudo apt update 
sudo apt install golang-go
go install github.com/OJ/gobuster/v3@latest

#Una volta installato bisogna aggiungerlo al PATH per poterno far funzionare da qualsiasi directory

nano tilde/.bashrc

#alla fine del file aggiungere
export PATH=$PATH:$HOME/go/bin

#Salvare e uscire e provare
```

---

# **Comandi e flag più importanti**

```Shell
#OBBLIGATORI
-u <URL>   Serve per specificare l''URL del sito che si vuole scansionare

-w <path_wordlist>   Serve per specificare il file che contiene tutte le directory da cercare (tipo seclist)

#Opzionali

-v Verbose

```

```Shell
gobuster -u http://192.168.0.103:1000 -w /usr/share/ecc..
(se non si specifica la porta userà per default la 80)
```