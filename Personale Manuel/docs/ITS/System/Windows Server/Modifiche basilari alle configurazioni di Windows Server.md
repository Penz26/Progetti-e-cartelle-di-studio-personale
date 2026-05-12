#Windows 

# **Indirizzamento IP**
> - Indirizzo dinamico (DHCP)
> - Indirizzo Statico
> - Indirizzamento DNS
> - Netmask
> - Default gateway
> - Classi di indirizzamenti - Pubblico e Privato

---
# **Prime modifiche al sistema**

1. Cambio password Administrator (Primo profilo creato)
2. Ingresso nella console e creazione degli utenti amministrativi per Disaster Recovery (SysAdm e Rescue)
3. Modifica indirizzo IP da dinamico (DHCP) a Statico
4. Ingresso al sistema come utente (D.R.) SysAdm/Rescue e creazione del profilo relativo
5. Disabilitare utente Administrator
6. Personalizzazione del profilo D.R.
7. Installazione sistema di recovery (Veaam Agent Free) con avvio del programma e analisi del backup effettuato
8. Simulazione CRASH sistema installato e relativo ripristino
9. Analisi del sistema ripristinato

---

# **Creazione utenti**
>Diverse metodologie:

- Tramite GUI (interfaccia grafica)
- Tramite riga di comando (prompt DOS)
```DOS
net user nome_utente password /ADD
net user nome_utente /expires:never
net localgroup Administrators nome_utente /add
net localgroup "Utenti Desktop Remoto" nome_utente /add
net user nome_utente password  
```

>Esempio:
![[DOS_user.png]]

---

# **File-Server (Workgroup)**
>Generalmente utilizzato per condividere aree dischi a più utenti in rete, meno per altri tipi di servizi (printer sharing, WEB services, posta elettronica, ecc...)

>Serve principalmente come archivio digitale di un'organizzazione. 
>Invece di disperdere i documenti su decine di computer individuali, un file server consolida tutto in un unico punto.

---

# **Primary Domain Controller**
>Gestisce diverse centinaia/migliaia di utenti collegati al server, con rigide politiche di sicurezza, condivisione dati, servizi, ecc...