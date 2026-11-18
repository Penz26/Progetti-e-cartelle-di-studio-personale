---
date: 2026-11-18
tags:
  - CyberSecurity
  - Proxmox
subject: Sistemi
module: Fail2ban
source: https://www.youtube.com/watch?v=kgdoVeyoO2E
---
## **Che cos'è?**
>E' un programma che guardando i log generati da altre applicazioni/sistemi permette di localizzare e bannare l'IP che eseguono tentativi di autenticazione.
>Può controllare diversi servizi allo stesso momento
>Permette di prevenire attacchi di brute-force

>Crea regole sul firewall per bloccare gli IP seguendo determinate regole:
>(Es. dopo 7 tentativi di autenticazione falliti viene bannato l'IP)

## **Installazione**
>Semplicissimo pacchetto su debian

```bash
apt update && apt install fail2ban
```

---
# **Configurazione**
>I file di configurazione risiedono nella directory:
>**/etc/fail2ban**

## fail2ban.conf
>Configurazione del servizio failban

>[!IMPORTANT] NON modificare direttamente questo file invece creare una copia terminante in .local

## **jail.conf**
>**File di configurazione più importante** (regole di ban, ignore, ecc)

>[!IMPORTANT] NON modificare direttamente questo file invece creare una copia terminante in .local

Permette di specificare campi come:
- IP da ignorare (es. IP della macchina da cui ci collegheremo in SSH)
  ```bash
  #"ignoreip" can be a list of IP addresses, ecc...
  ignoreip = <lista di Ip da ignorare>
  ```
- Per quanto tempo l'host che ha provato a connettersi debba essere bannato
  ```bash
  # "bantime" is the number of seconds that a host is banned
  bantime = 10m
  ```
- In quanto tempo l'host deve fare il numero di tentativi stabilito per essere bannato (se in 10 minuti fa 5 tentativi falliti allora lo banna **SE** invece in 10 minuti ne fa solo 4 all'11 minuto si resetta il counter)
  ```bash
  # A host is banned if it has generated "maxretry" during the last findtime seconds
  findtime = 10m
  ```
- Numero massimo di tentativi falliti dopo il quale l'host viene bannato
  ```bash
  # "maxretry" is the number of failures before a host get banned
  maxretry = 5
  ```

## **Jails**
>Le jail sono una forma di combinazione tra un filtro e un azione

>[!NOTE] Attivare le jail solamente per i servizi che si hanno scaricati e che vengono utilizzati.
>Risulterebbe inutile per fail2ban cercare e controllare log di servizi che non ci sono nemmeno sul sistema

>Sezione dei Jails in fondo in base ad ogni servizio da proteggere
```bash
[sshd]
#Per attivare una jail per un servizio mettere
enabled = true (solitamente per sshd è abilitato di default)
port = ssh
logpath = %(sshd_log)s
backend = %(sshd_backend)s
```

>Comando per vedere che jail sono attive:
```bash
fail2ban-client status
```
### **Configurazione di alert**
>In fondo al file si possono anche configurare i canali di notifica mail in modo che l'amministratore possa essere al corrente di quando un IP venga bannato

```bash
# Destination email address used solely for the interpolation in jail.{conf,local,d/*} configuration files
destemail = root@localhost

# Sender email address used solely for some actions
sender = root@<fq-hostname>
```