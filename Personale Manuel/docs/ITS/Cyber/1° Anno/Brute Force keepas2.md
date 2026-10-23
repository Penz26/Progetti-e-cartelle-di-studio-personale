#CyberSecurity 

# **Contesto**
>Abbiamo un password manager (keepass2) di cui conosciamo il file del database e parte della password dell'utente.

>Strumenti utilizzati:
>- hashcat
>- keepass2john

---

# **Hashcat**
>Hashcat permette sia di creare una wordlist di tutte le possibili password e anche di effettivamente provare a vedere quale di queste funzioni, e quindi ci permetta di entrare nel database con le password.

>Come si usa:
```bash
hashcat -a 3 --stdout DF6h4%?s?d17K74 > candidates.txt

# -a: indica il modo di operare (brute force = 3)
# --stdout: invece di tentare di crackare la password stampa a schermo tutte le possibili varianti
# DF6h4%?s?d17K74: è la password che conosciamo
#                  i caratteri preceduti da un ? indicano che quei caraterri non sono conosciuti e di mettere tutte le possibili lettere e numeri
# ?l = lettera minuscola , ?u = lettera maiuscola , ?d = numeri , ?s = simboli , ?a tutti i precedenti
# > candidates.txt: reinderizza il risultato in un file chiamato candidates.txt
```

---

# **Keepass2john.py**
>E' uno script Python che analizza il file del database (.kdbx) e ne estrae l'hash in un formato comprensibile ai tool di cracking

>Come si usa:
```shell
python3 keepass2john.py hahaha.kdbx > hash

# hahaha.kdbx è il file del database contenente l'hash
# > hash: reinderizza il risultato in un file chiamato hash
```

---

# **Effettivo tentativo di Crack usando hashcat**

```shell
hashcat -m 13400 -a 0 -o cracked_password.txt hash candidates.txt --status --status-timer=2 --potfile-disable

# -m 13400: specifica ad hashcat il tipo di hash da trattare (13400 è il codice per keepass)
# -a: imposta la metodologia di attacco (dizionario)
# -o cracked_password.txt: indica il file in cui verrà scritta la password una volta trovata
# hash candidates.txt: indica il file contenente l'hash e il file con la lista di password
# status --status-timer=2: mostra lo stato di avanzamento ogni 2 secondi
# --potfile-disable: disabilita l'uso del potfile, forzando hashcat a ricalcolare l'attacco senza attingere da sessioni precedenti
```