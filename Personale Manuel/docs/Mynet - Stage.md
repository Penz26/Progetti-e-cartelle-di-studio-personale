
# ==***07/07/2026***==
## Imap e Smtp

>Imap (Internet Message Access Protocol):
>protocollo per gestire la ricezione e la sincronizzazione della posta su più dispositivi

>Smtp (Simple Mail Transfer Protocol):
>protocollo standard utilizzato dai client di posta per inviare


## Samba file server
>Samba è un software open source che permette di condividere file e stampanti all'interno di una stessa rete


## Ansible
>Ansible è un tool di automazione IT open source che semplifica la configurazione dei server, il deployment delle applicazione e la gestione dell'infrastruttura.

>Sulla macchina principale (nodo) risiede il software mentre le macchine remote non necessitano di agenti dedicati. La comunicazione avviene tramite canali sicuri e standard come SSH.
>
>Tramite i **playbook** Ansible stabilisce lo stato desiderato dell'infrastruttura. E' idempotente, ovvero ripete l'azione solo se necessario per evitare modifiche accidentali o indesiderate.

- inventario
- playbook
- ruoli

---
# ==***08/07/2026***==
# Aggiornamento server mail
>E' stata rilasciata una nuova versione di un client web  che patcha determinate vulnerabilità

1. Controllare le CVE e cosa effettivamente veniva fixato
2. Entrati ssh sulla vm con il servermail
3. controllata versione installata e su cosa si girasse e su che webserver (apache o ngnix) sudo apt policy nome_pacchetto
4. Entrati nelle configurazione /etc/nginx/sites-enabled che ci diceva il path dove sono contenuti il software
5. Scaricato ed estratto il pacchetto
6. FATTO BACKUP dell'attuale database e dei file della versione precedente del software
```sh
   pg_dump nome_database > path/file/di/salvataggio
   stessa roba per altri db
   
   --- Oppure se fosse stato un altro DB ci sarebbero comandi come: ---
   mysqldump
   
   cp -Ra html html_1.6.16
```
7.  Controllare che sia andato tutto liscio

# **Pulizia dischi rigidi e ssd**

## **shred (dischi HDD)**
>Sovrascrive il disco più volte con dati casuali per rendere impossibile il recupero magnetico ed infine scrive una passata finale di zeri per nascondere il processo
```sh
sudo shred -v -n 3 -z /dev/sdX
-v: verbose
-n 3: esegue 3 passaggi di sovrascrittura con dati casuali
-z: esegue un ultima passata scrivendo solo zeri
/dev/sdX: HDD di cui eseguire la sovrascrittura
```

**blkdiscard (SSD)**
>Ripulisce velocemente senza passare dai controller. Questo comando invia un segnale TRIM a ogni blocco del disco dicendo al controller che tutte le celle sono vuote. In questo modo (visto che blkdiscard non esegue cicli di scrittura) preserviamo anche l'integrità dei dischi
```sh
sudo blkdiscard -v /dev/sdX
```

## **dmesg**
>Legge le chiamate del kernel

## **dd**
>Riempe l'intero disco di zeri
```sh
sudo dd if=/dev/zero of=/dev/sdX bs=4M status=progress

if=/dev/zero : #la sorgente dei dati
of=/dev/sdX : #il disco di destinazione
bs=4M : #scrive in blocchi da 4 Megabyte per velocizzare il processo
status=progress : #mostra la velocità e il tempo rimanente
```

>Può anche essere usato per flashare delle  ISO su una chiavetta
```sh
sudo dd if=percorso/file.iso of=/dev/sdX bs=4M status=progress conv=fdatasync

if=percorso/file.iso : #è la sorgente (il file ISO che si ha scaricato)
of=/dev/sdX #la destinazione (chiavetta USB)
bs=4M #velocità di scrittura
status=progress #mostra in tempo reale quanti dati sono stati scritti e la velocità di trasferimento
conv=fdatasync : #costringe linux a svuotare la cache e scrivere fisicamente l'ultimo bit prima di chiudere il comando
```

---
# ==***09/07/2026***==

dns autoritativi, record dns, tipi di dns

generari chiavi ssh, usare passphrase per la chiave per proteggerla

## Fatta procedura esplicativa di come applicare la firma digitale (file .htm)

>1. Entrato con remmina in una VM Windows10 per fare le prove con Outlook.
>2. Scaricato il file in estensione .htm della firma digitale dell'azienda
>3. Inserito il file nella cartella "%AppData%\Microsoft\Signatures\"
>4. Andare in File, Options, Mail, SIgnatures, e mettere come firma di ricezione e risposta

## **Aggiornamento di Zone dns sul server dns Mynet**
>Abbiamo dovuto cambiare le configurazioni delle zone DNS di alcuni clienti.

==**Fatto un snapshot del server dns in caso venga cambiato qualcosa in modo errato**==
- Procedura 
1. Sanificato campi TXT che non erano conformi agli standard (il testo andava messo tra "")
2. Cambiato il SOA (Start of Authority) per far sì che d'ora in poi il dominio principale venga risolto dal dns autoritativo di Mynet con il suo TTL, Serial, Refresh, Retry, Expiry e Minimum TTL
3. Cambiati i due record dns (record NS) così che il dominio venga gestito dal server dns di Mynet
4. Controllati eventuali errori
5. Entrare nel server dns in ssh (con utente abilitato a usare solo determinati comandi come sudo)
6. Usati comandi:
```sh
--- zona = dominio principale ---
--- zona.txt = file di configurazione dns ---

pdnsutil load-zone <zona> <zona.txt> 
#Importa tutti i record direttamente nel database di PowerDNS assegnandoli al dominio <zona>

pdnsutil check-zone <zona>
#Fa la stessa identica cosa di named-checkzone in BIND. Analizza la zona importata nel database per verificare che non ci siano errori sintattici

pdnsutil set-kind <zona> master
#Dice a PowerDNS che questo server dns dove attualmente si è loggati è il master ovvero il primario, significa che se ci sono altri server DNS dovranno recuperare le info da lui

pdnsutil set-meta <zona> SOA-EDIT-API-DEFAULT
#Questa regola dice a PowerDNS che ogni volta che si cambia un record tramite API aggiorna e incrementa il Serial del SOA in automatico
```