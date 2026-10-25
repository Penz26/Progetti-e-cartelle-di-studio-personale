#CyberSecurity 

# Triade CIA

1. Confidentiality (riservatezza)
2. Integrity(integrità)
3. Availability(disponibilità)

---

## **Confidentiality (riservatezza)**
>Garantire che le informazioni che stiamo trasmettendo siano segrete e private
>Le informazioni devono essere accessibili solamente a chi di interesse.
>Solitamente si parte da zero trust, nessuno ha accesso tranne quando viene esplicitamente dato accesso.

**Compromissioni**
- MITM

---
## **Integrity (integrità)**
>Assicurarsi che i dati siano affidabili e privi di manomissioni

>Integrità si mantiene se i dati sono:
>- autentici, 
>- accurati 
>- affidabili

**Compromissioni**
- alterazione configurazioni
- alterazione dati e log di sistema
---

## **Disponibilità**
>I dati devono essere disponibili a coloro a cui servono
>Sistemi, reti e applicazione devono funzionare come e quando dovrebbero
>Le persone che hanno accesso a informazioni specifiche devono essere abilitate a farlo in qualsiasi momento

**Compromissioni**
- interruzioni di corrente / internet
- eventi natuali
- atti di sabotaggio

**Contromisure**
- ridondanza
- mantenere pacchetti e software aggiornati
- backup e plan di disaster recovery
---

# **Governance e framework riferimento**

## **ISO/IEC 27001**
>Standard internazionale certificabile per la gestione della sicurezza delle informazioni attraverso un ISMS 

>Definisce un approccio strutturato basato su **rischio, processi, controlli e miglioramento continuo**

---
## **NIST Cybersecurity Framework (CSF)**
>Framework per organizzare e migliorare la gestione del rischio cyber.

>Si articola nelle funzioni:
>- Identify
>- Protect
>- Detect
>- Respond
>- Recover

---

## **NIS2 Direttiva UE 2022/2555**
>Introduce requisiti di cybersecurity e gestione del rischio per organizzazioni appartenenti a settori critici, distinguendo tra soggetti essenziali e importanti


---
 **Cifrari DES**
**Cifrasio AES**
>Algoritmo simmetrico, stessa chiave

Generazione chiave AES con openssl
```bash
openssl
```

---
## **Crittografia asimmetrica (doppia chiave)**
>Nella crittografia asimmetrica ogni utente ha una coppia di chiavi, costituita da una chiave pubblica e una chiave privata

>La chiave pubblica viene resa nota quella privata no.

>Il messaggio viene mandato con la chiave pubblica del destinatario e il destinatario la decifra con la propria chiave privata.

**Requisiti**


## RSA
>Si basa sulla scomposizione di un numero nei suoi fattori primi

n=p*q
z = (p-1)*(q-1)

rsa_ez

---
## **ECC**
>Sicurezza equivalente a RSA con dimensione di chiave significamente oiù piccole
>Calcoli più veloci, le dimensioni più piccole facilitano il calcolo di conseguenza la creazione

---

## **Catena IAA**

- Identification: dichiari chi sei
- Authentication lo dimostri
- Authorization: cossa puoi
- Account/audit: traccia

| Stage Catena   | **Modello** | **Chi decide**       | **Esempio**            |
| -------------- | ----------- | -------------------- | ---------------------- |
| Identification | DAC         | Proprietario risorsa | Chmod linux            |
| Authentication | MAC         | Sistema (etichette)  | SeLinux, Bell-LaPadula |
| Authorization  | RBAC        | Ruoli                | Admin, Editor, Viewer  |
| Account/audit  | ABAC        | Attributi + consenso | IP, ora ,dispositivo   |

---

## **Autenticazione**

**3 fattori:**
- Qualcosa che sai: password, pin, domanda segreta
- Qualcosa che hai: Token Hardware, app, TOTP, SMS OTP
- Qualcosa che sei: Impronta digitale, volto, iride
