[[Introduzione a PostgreSQL]]

# **Come e dove inseriamo i dati?**

## **1. Dove scriviamo le queries?**
>Possiamo accedere e gestire il nostro DB attraverso il terminale oppure attraverso pgAdmin come abbiamo visto.

>Da Terminale su Windows:
-  Da windows avviamo la SQL Shell (psql) installata con l'installer in automatico e ci assicuriamo che le variabili impostate siano quelle giuste (nome_database, porta, username e relativa password)
- Vedremo apparire sulla linea di comando
  nome_database=#
  Questo ci dirà che siamo effettivamente dentro quel database

>Da terminale su container Docker basterà eseguire il comando:

```Shell
docker exec -it <nome_container> psql -U <utente> -d <nome_db>
```

## **2. Come inseriamo le queries?**
>Una volta entrati nella gestione del DB attraverso linea di comando, oppure attraverso pgAdmin potremo scrivere le nostre queries.

## **CRUD**
>Sono sempre le solite query SQL, ma metterò di seguito degli esempi per rinfrescare la memoria

- **Creazione Database**

```SQL
CREATE DATABASE officina_db;
```

- **Creazione Utente con Password e assegnazione permessi**

```SQL
CREATE USER meccanico WITH PASSWORD 'topsecret';

GRANT ALL PRIVILEGES ON DATABASE officina_db TO meccanico;
```

- **Creazione di una tabella**

```SQL
CREATE TABLE proprietari (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE veicoli (
    id SERIAL PRIMARY KEY,
    targa VARCHAR(10) UNIQUE NOT NULL,
    modello TEXT,
    proprietario_id INTEGER REFERENCES proprietari(id) ON DELETE CASCADE
);
```

---

## **Operazioni CRUD**

1. Inserimento Dati
   
```SQL
INSERT INTO veicoli (targa, modello, anno) 
VALUES ('AA123BB', 'Fiat Panda', 2022),
       ('CC456DD', 'Tesla Model 3', 2023);   

-- Ci dirà (significa che 2 righe sono state inserite):
INSERT 0 2
```

2. Lettura Dati

```SQL
SELECT * FROM veicoli;                -- Leggi tutto
SELECT modello FROM veicoli WHERE anno > 2022; -- Filtra per anno
```

3. Aggiornamento Dati

```SQL
UPDATE veicoli 
SET modello = 'Fiat Panda Hybrid' 
WHERE targa = 'AA123BB';
```

4. Cancellazione Dati

```SQL
DELETE FROM veicoli WHERE targa = 'CC456DD';
```

---

- **Modifica colonne e record**

1. Aggiungere colonne

```SQL
ALTER TABLE veicoli
ADD color VARCHAR(255)
```

2. **Modificare record in una tabella**

```SQL
UPDATE veicoli  
SET color = 'red'  
WHERE brand = 'Volvo';

-- SENZA LA CLAUSA WHERE VERREBBE MESSO "red" COME COLORE PER TUTTI VEICOLI
```

3. **Modificare i campi di inserimento**

```SQL
ALTER TABLE veicoli
ALTER COLUMN colon TYPE VARCHAR(50);
```

4. **Rimuovere colonne**

```SQL
ALTER TABLE veicolo
DROP COLUMN color;
```

5. **Rimuovere record dalla tabella**

```SQL
DELETE FROM veicoli  
WHERE brand = 'Volvo';

--Per cancellare TUTTI i record di una tabella:

DELETE FROM veicoli;
--Oppure
TRUNCATE TABLE veicoli;
```

- **ELIMINARE INTERE TABELLE**
> Sappiamo già per cosa ci servirà questo bel comandino innocuo
  
```SQL
DROP TABLE cars;
```

## **Comandi di Ispezione (Meta-Comandi)**
>Nonostante ci sia scritto Meta non stiamo parlando di Zuckerberg e della sua schifosa impresa.
>Sono comandi per controllare la struttura dei database, tabelle, utenti

|      **Comando**      |                         **Descrizione**                         |
| :-------------------: | :-------------------------------------------------------------: |
|       **`\l`**        |              Elenca tutti i database disponibili.               |
|   **`\c nome_db`**    |            Ti connette (passa) a un altro database.             |
|       **`\dt`**       |         Elenca tutte le tabelle nel database corrente.          |
| **`\d nome_tabella`** | Descrive la struttura di una tabella (colonne, indici, chiavi). |
|       **`\du`**       |       Elenca tutti gli utenti (ruoli) e i loro permessi.        |
|       **`\df`**       |          Elenca tutte le funzioni memorizzate nel DB.           |
|       **`\dn`**       |         Elenca gli "Schemi" (i namespace del database).         |
|       **`\dx`**       |         Elenca le estensioni installate (es. PostGIS).          |
|    **`\copy ...`**    |  Importa o esporta dati da/verso un file CSV (molto potente).   |
|   **`\! comando`**    |   Esegue un comando shell (es. `\! ls`) senza uscire da psql.   |
|       **`\q`**        |                          Esci da psql.                          |
