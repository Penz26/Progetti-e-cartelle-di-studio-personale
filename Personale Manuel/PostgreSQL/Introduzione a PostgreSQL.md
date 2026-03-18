#Database 

# DOCUMENTAZIONE UTILE:

>Guida ufficiale di PostgreSQL per l'apprendimento
>[PostgreSQL Guide](https://postgres.guide/docs/intro/)

>Videocorso di 4h su Youtube
>[Video Youtube](https://www.youtube.com/watch?v=qw--VYLpxG4&t=653s)

---
# COS' E' POSTGRESQL? 🐘
>E' un ORDBMS (Sistema di base di dati basato su Oggetti-Relazioni ).
>Combina il modello relazionale standard, come MYSQL, con caratteristiche orientate agli oggetti.

## **1.  Caratteristiche Principali:**

- **Conformità SQL:**
  Implementa quasi tutte le funzionalità dello standard SQL:2023
- **Supporto JSONB:**
  anche se è un database relazionale, gestisce i dati non strutturati (NoSQL) in formato binario (JSONB), permettendo ricerche indicizzate velocissime su documenti JSON
- **MVCC:**
  è la magia che permette aa più utenti di leggere e scrivere contemporaneamente senza bloccarsi a vicenda
- **Estensibilità:**
  puoi creare i tuoi tipi di dati, operatori e funzioni personalizzate in vari linguaggi

## **2. I Pregi:**
>Figo! Ma perchè dovrei usarlo invece che Mysql

- **Affidabilità**
  Le transazioni sono Atomiche, Coerenti, Isolate e Durevoli (ACID)
- **Open Source**
  Non è controllata da una singola azienda, come Oracle. Ha una licenza permissiva simile a quella MIT/BSD
- **Performance**
  Eccelle quando le query diventano complicate
- **Ecosistema Geospaziale**
  grazie all'estensione PostGIS, è lo standard per i sistemi informativi geografici (mappe, coordinate, rotte)

---

# **3. Per cosa viene utilizzato?**
>Che ce famo praticamente?

- **Applicazioni Web e Mobile:**
  per app che richiedono integrità dei dati
- **Data Analysis:**
  viene spesso usato come Magazzino Dati grazie alla sua capacità di gestire grandi volumi di dati
- **Sistemi Finanziari:**
  per far sì di non perdere NESSUNA transazione a  causa di un crash
- **Scientific Computing:**
  per gestire dataset complessi con tipi di dati personalizzati