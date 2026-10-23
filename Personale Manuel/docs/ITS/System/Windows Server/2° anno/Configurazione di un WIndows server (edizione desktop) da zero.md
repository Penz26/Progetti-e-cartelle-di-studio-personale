
#Windows

# Installazione Windows Server

- Disco Sata prima perchè dobbiamo scaricare i driver VirtIO
- Esperienza Desktop
- riconosciuto il disco windows farà in automatico la partizione.
# Configurazione

Una volta dentro inizializzare il disco.
Poi dobbiamo:
- disabilitare l'indicizzazione su entrambi i volumi
- andare su entrambi i dischi criteri

Cambiare la lettera dei CD/ROM e cambiare la lettera in X

---

Cambiare hostname (Bernardelli_VM)

Performance visive disabilitate, (personalizzate con solo peek abilitato)

Disabilitare IPv6
Mettere IPv4 fisso:

Indirizzo IP: 10.30.21.2XX (xx numero cavo di rete Manuel 10)
Subnet Mask: 255.255.255.0
Gateway_predefinito: 10.30.21.1

DNS: 8.8.8.8

provare ad andare in rete altrimenti niente

---

# Personalizzazione (mettersi comodi per lavorare):

disattivare schede in anteprima/workspace
barra di ricerca
ecc...

---
# Riconfigurazione del disco 

detach del disco di sistema

Bus/devic: VirtIO
Cache: Direct sync
discard: yes
IO thread: yes
Backup: yes
Async IO: native

Riattaccare il disco, riavviare e vedere se funziona

---

# 1° Backup 

Fare un backup sul disco Localbackup modalità snapshot ZSTD.


---

>Una volta fatte le prime configurazioni ed installate le applicazioni necessarie, procedere con:
1. Cambio password Administrator
2. Ingresso nella console e creazione degli utenti amministrativi per Disaster Recovery (SysAdm e Rescue)
3. Modifica indirizzo IP da dinamico (DHCP) a statico
4. Ingresso al sistema come utente D.R. (SysAdm e Rescue)  e creazione del profilo relativo
5. Disabilitazione dell’utente Administrator
6. Personalizzazione del profilo D.R.

>Per la creazione di utenti da riga di comando dare i seguenti comandi sul terminale:
```shell
net user <NOME_UTENTE> <PASSWORD> /ADD
net user <NOME_UTENTE> /expires:never
net localgroup Administrators <NOME_UTENTE> /add
net localgroup "Utenti Desktop Remoto" <NOME_UTENTE> /add
net user <NOME_UTENTE> <PASSWORD> 
```

---

Licenza datacenter
riempire i core del server
massimo licenza datacenter 32core