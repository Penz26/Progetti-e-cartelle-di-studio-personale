#Linux 

# **Cos' è nmcli?**
>nmcli è l' "applicazione da terminale" di network manager.
>Permette di gestire tutta la parte di Networking sulla tua macchina:
>- connessioni wifi,
>- ip (manuale o DHCP),
>- DNS,
>- ed altre informazioni

---
# **Gestione del Wi-FI**

### **Scan della rete per reti Wifi-disponibili**
```bash
nmcli device wifi list
```

>Mostra una tabella dettagliata con SSID, canalae, velocità massima, intensità del segnale e tipo di sicurezza


### **Connettersi a una nuova rete Wi-Fi**
```shell
nmcli device wifi connect "Nome_rete" password "password_wi-fi"
```

>Crea un profilo di connessione salvato e si collega alla rete

### **Genera un QR Code della rete a cui si è connessi**
```Shell
nmcli device wifi show-password
```

>Mostra una riga di testo e un codice QR direttamente nel terminale


---
# **Stato dell' Hardware e dei Dispositivi**

## **Controllo dello stato di tutte le schede di rete**
```Shell
nmcli device status
```

>Dice quali interfacce sono connesse, quali sono disconnesse e quali sono gestite o ignorate da NetworkManager

## **Mostrare i dettagli Hardware di una specifica interfaccia**
```shell
nmcli device show wlan0
```

>Mostra l'indirizzo MAC, i server DNS correnti, l'IP assegnato, la subnet mask e i percorsi di routing attivi

## **Spegnere/Accendere completamente il Wi-Fi**
```Shell
nmcli radio wifi off
nmcli radio wifi on
```

---

# **Configurazione Avanzata dei Profili**

## **Vedere ogni singolo parametro di una connessione**
```Shell
nmcli connection show "Nome_Rete"
```

>Genera un output che elenca tutte le impostazioni nascoste dell'attuale profilo di rete

## **Configurare un IP Statico**
```Shell
sudo nmcli connection modify "Nome_Rete" ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual
```

>Per rimetterlo in DHCP:
```Shell
sudo nmcli connection modify "Nome_Rete" ipv4.method auto
```

## **Modificare il DNS**
```shell
sudo nmcli connection modify "Nome_Rete" ipv4.dns "1.1.1.1 1.0.0.1"
```

>Successivamente ignorare automaticamente la prossima volta il dns automatico
```shell
sudo nmcli connection modify "Nome_Rete" ipv4.ignore-auto-dns yes

#Rilegge la configurazione aggiornata del profilo di rete
sudo nmcli connection up "Nome_Rete"
```

## **Impostare la priorità di una connessione (Autoconnect priority)**
```Shell
#Il numero più alto indica una priorità più alta

nmcli connection modify "Nome_Rete" connection.autoconnect-priority 10

nmcli connection modify "Nome_Rete" connection.autoconnect.priority 5
```

---
# **Monitoraggio e Debugging**
```shell
nmcli monitor
```

>Rimane aperto nel terminale e stampa una riga ogni volta che un'interfaccia si disconnette, cambia IP, si collega ad  un altro hotspot o quando NetWorkManager modifica il suo stato.