[[Introduzione a PostgreSQL]]

# **Come Installarlo?**
>Di seguito riporto l'installazione attraverso l'installer ufficiale di PostgreSQL per Windows mentre Linux attraverso un container

# **1. Windows:**

1. Visitare la pagina [PostrgreSQL Installation](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) e installare la versione più recente per Windows
2. Eseguire l'installer e seguire i vari step:
   - specificare il percorso in cui installare il servizio
   - selezionare i componenti che si vogliono installare
   - *Opzionale:* scegliere dove immagazzinare i dati (di default saranno nella directory data di PostgreSQL) 
   - inserire la password per il superutente (postgres)
   - selezionare la porta di ascolto del server (deafult: 5432)
   - selezionare la posizione geografica del DB

Una volta fatto ciò procedere con l'installazione

# **2. Container Docker su Linux:**
>Tralascerò l'installazione dell'Engine di Docker visto che lo stiamo giù usando nel corso di Sistemi

1. Pulliamo l'immagine di PostgreSQL da Docker Hub
   
```Shell
docker pull postgres

#Per una versione in specifico:
docker pull postgres:16
```

2. Facciamo partire un container con variabili d'ambiente per user, password, porte e nome database
   
```Shell
docker run -d \  
  --name postgres-container \  
  -e POSTGRES_USER=admin \  
  -e POSTGRES_PASSWORD=secret \  
  -e POSTGRES_DB=mydatabase \  
  -p 5432:5432 \  
  postgres

#Check se è partito

docker ps
```

3. Connessione al container
   
```Shell
docker exec -it postgres-container psql -U admin -d mydatabase

#postgres-container = nome del container
#psql = interfaccia a riga di comando ufficiale di PostgreSQL, serve per scrivere query SQL e gestire il database
#-U admin = indica l'utente con cui vuoi loggarti
#-d mydatabase = specifica il database a cui vuoi connetterti inizialmente

#Bisognerebbe vedere apparire nella shell
mydatabase=#
```

4. Eseguire le querys che si vogliono fare
   
```SQL
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

INSERT INTO users (name, email) VALUES ('Manuel', 'manuel@esempio.com');

SELECT * FROM users;
```


>Come sappiamo i container Docker quando fermati cancellano i dati, quindi usiamo i volumi in modo che i container possano archiviare i dati al loro esterno così che anche se il container muore i dati rimangono.

```Shell
docker run -d \
  --name postgres-container \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres
  
  #Check del volume
  docker volume ls
```

### Come sempre detto un Docker Compose torna sempre utile quando dobbiamo setuppare più cose allo stesso tempo (es. database, php, codice, ecc...)
>Di seguito un docker-compose.yml come esempio per il servizio db di PostgreSQL 
>==**(NIENTE) [[pgAdmin 4]]:**==

```Shell
version: '3.8'

services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
  
#Usciti dall'edit dalla cartella eseguiamo
docker compose up -d
```