#Database  [[Introduzione a PostgreSQL]]

# **Cos'è pgAdmin?**
>In parole povere è il PhpMyAdmin di PostgreSQL
>Permette di gestire e interagire con il database attraverso una GUI user-friendly.


## Molto simile a PhpMyAdmin non sembra?
![[pgAdmin DashBoard.png]]

>Si possono fare esattamente le stesse operazioni che si possono fare con PhpMyAdmin, ma ovviamente è più veloce, open source e fatto apposta per PostgreSQL.

## **Per cosa utilizzarlo?**
>Tutte le cose che si possono fare su pgAdmin si possono fare da linea di comando ma senza aiuti, rappresentazioni grafiche

1. **Esplorazione Visiva**
>Invece di digitare comandi hai un albero a sinistra che puoi espandere.                           Puoi vedere subito:
>- Tabelle, Colonne e Indici
>- Funzioni, Trigger e Procedure
>- Utenti e i loro permessi

2. **Query tool facilitata**
>A differenza del terminale qui hai:
   >- Autocompletamento delle tabelle e delle funzioni mentre scrivi
   >- Evidenziazione della sintassi
   >- Esportazione Rapida
>Per accedere alla dashboard per le query fare clic con tasto destro sul nome del database e dal menù a tendina selezionare "Query Tool"

![[Tool Query.png]]

3. **Dashboard di Monitoraggio**
>pgAdmin ti mostra subito dei grafici in tempo reale. Permette di capire:
   >- quante persone sono connesse al database
   >- quante transazioni (scritture/letture) sta facendo il server
   >- se ci sono blocchi o processi che stanno rallentando il sistema

4. **Gestione semplificata**
>Operazioni da linea di comando lunghe diventano istantanee
   >- Backup e Restore con un tasto
   >- Importazione Dati, caricare un file CSV direttamente in una tabella
   >- ERD Tool genera automaticamente uno schema visivo che mostra come le tue tabelle sono collegate tra loro
   
   
```docker-compose.yml
services:
  db:
    image: postgres:latest
    container_name: postgres-container
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: password123 # Cambiala in qualcosa di sicuro!
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin-container
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: adminpassword
    ports:
      - "8080:80" # Accedi via browser su http://localhost:8080
    depends_on:
      - db

volumes:
  postgres_data:   
```
   
