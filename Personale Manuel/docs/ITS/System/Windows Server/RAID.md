#Windows 

# **Cos' è un RAID**
 >RAID stà per "Redundant Array of Independent Disks" ovvero insieme ridondante di dischi indipendenti.

>Permette di gestire in diversi modi (diverse tipologie di RAID) il metodo di installazione tra vari dischi rigidi in un computer in modo che essi appaiono al sistema come u unico volume di memorizzazione.

>Principali scopi:
>- aumentare performance
>- rendere resiliente il sistema in caso di perdita di uno o più dischi
>- aumentare capacità di memorizzazione
>- migliorare tolleranze ai guasti

# **Come funziona? (Sezionamento dei dati)**
>I dati vengono suddivisi in sezioni di lunghezza uguale e vengono scritti su dischi differenti

---
# **Tipologie**
>Ne esistono varie tipologie ma per la maggior parte si usano RAID 0 , 1 , 5 e 10:

>[!NOTE] C = storage del disco più piccolo

>[!NOTE] N = numero di dischi

>[!NOTE] P = dischi di parità


## **RAID 0 (Almeno 2 dischi)**
>Il sistema RAID 0 divide i dati in piccoli frammenti (Stripes) e li distribuisce equamente su due o più dischi.
>- Come funziona
>  >se si deve salvare (scrivere sul disco) un file, questi viene diviso in 2 parti, metà file finisce sul disco A e l'altra metà sul disco B **contemporaneamente**
>- Prestazioni
>  >Estremamente veloce perchè i dischi lavorano in parallelo
>- Sicurezza
>  >Non  c'è ridondanza quindi anche se solo un disco si guasta l'intero array fallisce e tutti i dati vengono persi visto che rimarrebbe solo metà.

![[raid_0.png]]
## Storage totale = C x N
## Numero massimo dischi guasti = 0
---
## **RAID 1 (Almeno 2 dischi)**
>Il sistema RAID 1 scrive gli stessi dati su 2 dischi differenti (Mirroring) contemporaneamente.
>- **Dati duplicati**
>  >Ogni informazione viene scritta in entrambi i dischi
>- **Tolleranza ai guasti**
>  >Se un disco si rompe fisicamente il sistema continua a funzionare usando l'altro. **Nessuna perdita di file**
>- **Efficienza spazio**
>  >I dati essendo duplicati portano via metà dell'intero spazio totale tra i due dischi. (2TB + 2TB)/2

![[RAID_1.png]]
## Storage totale = C 
## Numero massimo dischi guasti = N -1
---
## **RAID 5 (Almeno 3 dischi)**
>Il sistema RAID 5 fraziona i dati su tutti i dischi **MA** viene aggiunto un elemento fondamentale chiamato parità dal quale si può ricostruire matematicamente i dati.

>[!IMPORTANT] La parità di ogni dato viene distribuita a rotazione su tutti i dischi

>- **Lettura diretta**
>  >Se il sistema deve leggere l'informazione A e sa che i dati sono sui dischi 1 e 2 e chiederà solo a loro di lavorare
> - **Lettura a scacchi**
>   >Il sistema non legge l'intero disco se deve cercare i dati di un file ma legge solo il settore specifico di quei dati
>- **Carico Bilanciato**
>  >Tutti i dischi lavorano la stessa quantità di tempo
>- **Velocità**
>  >Il sistema può leggere i dati da più dischi contemporaneamente senza che un singolo disco dedicato alla parità faccia da freno


>Esempio: 
>Disco 1: dato A
>Disco 2: dato B
>Disco 3: Parità (A+B)
>Se il disco 1 si rompe diventa
>x + B = P
>Quindi riuscirebbe a ricostruire ma se si rompono 2 dischi non riuscirebbe

![[RAID_5.png]]
## Storage totale = C x (N -1)
## Numero massimo dischi guasti = 1

---
## **RAID 10 (1 + 0) (Almeno 4 dischi)**
>Il sistema raid 10 (anche chiamato 1+0) è una combinazione intelligente di questi 2 metodi.
>**Crea 2 coppie (RAID 1):** Disco A e B hanno lo stesso contenuto, C e D hanno lo stesso contenuto
>**Unisce le coppie (RAID 0):** il sistema scrive i dati distribuendoli tra la "coppia 1" e la "coppia 2" contemporaneamente

![[RAID_10.png]]
## Storage totale = C x (N/2)
## Numero massimo dischi guasti = 1 per coppia

---

# **Raid Hardware e Software**
>Esistono sia RAID Hardware che Software

>I RAID Hardware sono gestiti direttamente da un controller installato sul sistema
>- **PRO**
>  >Sono più veloci rispetto a quelli Software
>  >Scalabili nel tempo
>  >Meno problemi di sostituzione dei dischi in caso di default
>  >Gestione del rischio di fault di uno o più dischi preventivo con eventuali allarmi
>- **CONTRO**
>  >Costosi
>  >Necessitano di Hardware dedicato
>  >Il sistema che viene installato è Hardware Dependent


>I RAID Software sono gestiti direttamente dal sistema operativo e non necessitano di controller dedicati
>- **PRO**
>  >Non necessitano di Hardware dedicato
>  >Sistema installato Hardware Independent
>- **CONTRO**
>  >Più lenti rispetto a quelli Hardware
>  >Non sempre scalabili col tempo
>  >Sostituzione dischi più complessa
>  >Nessuna gestione del rischio

