---
date: 2026-11-05
tags:
  - CyberSecurity
subject: Defense
module: Penetration testing
source: https://drive.osaspace.it/index.php/apps/onlyoffice/17988?filePath=%2FITS_SANDBOX%2FSANDBOX%20-%20MATERIALI%20DOCENTI%2FSECONDO%20ANNO%2FCybersecurity%2FLezione05%2FLezione05.pdf
---
# **Cyber Kill-Chain - Mapping con attacchi reali**

1. **Reconnaissance** (OSINT, social profiling, fingerprinting)
   >Studio di Linkedin, email HR, porte
2. **Weaponization** (creazione del file adatto al destinatario)
   >Fake CV, malware all'interno dell PDF
3. **Delivery** (Invio payload)
   >Invio mail
4. **Exploitation** (Trigger della vulnerabilità)
   >Allegato aperto
5. **Installation** (accesso persistente stabilito)
   > Installazione RAT / Keylogger 
6. **Command & control**  (Controllo remote delll'endpoint)
   > Endpoint infetto fa chiamate al server dell'attaccante
7. **Actions on Objectives** (obiettivo raggiunto)
   > Furto di dati, pivot su altri sistemi o uffici interni
   
## **Cyber Kill-Chain - Mapping su controlli e strumenti di difesa**
1. **Reconnaisance**
   >Monitor di external attack surface, OSINT e threat intelligence
2. Weaponization
   > Analisi malware, sandboxing, email security inspection
3. Delivery
   > Email gateway, web filtering, attachment scanning
4. Exploitation
   > Patch management, vulnerability management, EDR
5. Installation
   > endpoint protection, app, allowlist, least privilege
6. Command & control
   > DNS filtering network traffic monitoring, anomaly detection
7. Actions on Objectives
   > DLP backups, incident response, access control
   
   ---
# **Tecniche di deception**

**Honeypot:**
>sistema finto - qualsiasi connessione è sospetta.
>Viene usato come una porta falsa alla propria infrastruttura. Una sorta di dummy che permette di raccogliere dati se qualcuno sta cercando di entrare e su che porta, da che IP, ecc...

**HoneyToken**
>Credenziale/file fake - alert usato

>Queste tecnologie forniscono un **vantaggio difensivo**.
>Zero falsi positivi, nessuno dovrebbe toccarli se buon intenzionato
>Ogni accesso rileva un comportamento malevolo verso i nostri sistemi e risorse.

Esempio di Honeypot:

## [Beelzebub](https://github.com/beelzebub-labs/beelzebub)

```Bash
#installazione

git clone https://github.com/beelzebub-labs/beelzebub.git
cd beelzebub
./install.sh --docker
```

>Test di chiamata HTTP ed ispezione dei log:
```bash
curl -i http://localhost:8080

#per vedere i log delle chiamate e payload che ha ricevuto questa macchina
docker compose logs -f beelzebub

#Per smettere di leggere i logs e fermare l'honeypot
docker compose down
```

>Test di connessione ssh
```bash
ssh root@localhost -p 2222

#Prova password comuni, vengono tutte accettate

$ root@ubuntu

#Una volta dentro la shell è falsa, tutto viene loggato

whoami
id
cat /etc/passwd
ls /home
```

>Leggere i log strutturati e capire cosa è stato catturato
```bash
# Log completi con timestamp
docker compose logs beelzebub | grep "HTTP"
docker compose logs beelzebub | grep "SSH"

# Se vuoi vedere solo i tentativi di login SSH
docker compose logs beelzebub | grep -i "password"

# Quante richieste ha ricevuto l'honeypot?
docker compose logs beelzebub | grep "request" | wc -l
```

---

# **EDR (Endpoint Detection and Response)**

**Rilevamento**
>Behavioral + signature

**Risposta**
>Isola, termina, quarentina

**Forensics**
>Timeline completa eventi

## **Cosa vede?**

**Visibilità**:
> - ogni processo figlio creato (process tree)
> - connessioni di rete avviate da processi
> - modifiche a file critici e chiavi di registro
> - injection di codice in memoria

**Risposta automatica o guidata**
> - ISOLA host dalla rete
> - KILL terminazione immediata del processo sospetto
> - QUARANTINE File spostato in area sicura per analisi

# **XDR - Extended Detection & Response**
>EDR + dati da più fonti. La correlazione avviene su tutto il perimetro, non solo sull'endpoint

![[XDR.png]]

# **SIEM - Security Information & Event Management**
>Raccoglie normalizza e correla log da tutta l'infrastruttura: il cervello del SOC non il braccio.

**Fonti di Log**
- Firewall / IDS / IPS
- Server (Windows / Linux)
- Endpoint (via agente SSH)
- Active Directory / IdP
- Applicazioni web
- Cloud (AWS / Azure / GCP)

>Dal logo grezzo all' alert
```bash
2026-10-15 03:22:41 FAILED LOGIN
user = admin src=185.220.x.x

2026-10-15 03:22:42 FAILED LOGIN
user = admin src=185.220.x.x

#altre 500 volte
```

>==🔴**ALERT -- Credential Stuffing**==
>500 failed login in 120s - stesso IP - 10 host diversi
>SEVERITY: HIGH - Src: 185.220.x.x 

## **Concetti chiave**

>**Normalizzazione**
>Log di vendor diversi, solitamenti in formato comune (CEF, ECS).
>Senza, non si può correlare

>**Tuning continuo**
>Affinare le regole nel tempo: meno falis positivi stessa copertura

>**Retention**
>Quanti giorni conservare? Compliance (es. 1 anno) vs costo storage.

>**Alert fatigue**
>Regola troppo sensibile --> 1000 alert/giorno --> analista smette di guardare --> il vero attacco passa

# **SOAR - Security Orchestration, Automation & Response**