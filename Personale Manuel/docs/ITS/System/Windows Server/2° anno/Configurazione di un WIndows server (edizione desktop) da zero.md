
#Windows
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