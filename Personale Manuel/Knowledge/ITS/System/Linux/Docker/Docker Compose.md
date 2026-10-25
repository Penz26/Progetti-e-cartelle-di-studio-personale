#Docker [[Cos'è Docker]]  

# **COS' E'?**
>Docker Compose è uno strumento per definire e gestire applicazioni Docker multi-container usando un file **YAML** .
>Nato all'inizio come progetto separato (docker-compose) è stato poi integrato all'interno di docker (docker compose)
>E' il ponte tra i container individuali e un'applicazione completa e funzionante.

# **Le sue funzioni principali**:
>- **Orchestrazione semplificata**
	  gestisce più container come un'unica unità logica
>- **Configurazione come codice**
	 la config è versionata insieme al progetto
>  **Riproducibilità totale**
	Stesso ambiente su dev, test e CI/CD senza differenze
>- **Onboarding rapido**
	Un nuovo sviluppatore è subito operativo con un solo comando (docker compose up)


## NON SOSTITUISCE DOCKER, E' UNA SUA ESTENSIONE 
>*Ideale per sviluppo, testing, demo, applicazioni single-host e*
>Il file **YAML** è composto da tre sezioni che descrivono l'intera applicazione:
>- *services (i container)*
>- *volumes (la persistenza)*
>- *networks (la comunicazione)*

---
# **Comandi Essenziali**

## Avvio e Build

```Shell
#Avvia in foreground (vedi i log)
docker compose up

#Avvia in background (detached)
docker compose up -d

#Rebuild delle immagini + avvio
docker compose up --build
```

---

## Aggiornamento Immagini

```shell
#Guarda il docker-compose.yml e controlla sulla repo di docker se sono disponibili nuove versioni delle immagini specificate
docker compose pull
```

---
## Stop e Rimozione

```Shell
#Ferma e rimuove container + network
docker compose down

#Ferma, rimuove e cancella volumi
docker compose down --volumes
```

---
## Monitoring e Debug

>Monitorare e fare debug di uno stack multi-container è semplice con i comandi integrati di compose.

## Stato e risorse

```Shell
docker compose ps  #Lista dei servizi attivi
docker compose ps -a  #Include quelli fermi
docker compose stats  #Uso CPU/RAM in real time
```

---
## Logs

```Shell
docker compose logs  #Tutti i log
docker compose logs -f  #Follow real time
docker compose logs -f api  #Solo servizio API
docker compose logs --tail=50  #Ultime 50 righe
docker compose logs --timestamp  #Con timestamp
```

---
## Accesso ai Container
```Shell
#Shell interattiva (immagini full)
docker compose exec api bash
 
#Shell alpine (immagini lightweight)
docker compose exec api sh

#Esegui comando one-shot
docker compose run api comando

```

---
## Validazione

```Shell
docker compose config  #Valida YAML
docker compose config --service  #Lista servizi
```

---
# **Servizi**

## Image vs build
  >Ogni servizio può usare un immagine già pronta da Docker Hub oppure costruirne una personalizzata partendo da un Dockerfile locale. La scelta dipende dal tipo di servizio da mettere su

## Opzione 1, Immagine pre-costruita
```Shell
services: 
	nginx:
	image: nginx:alpine
	ports:
		-"80:80"
```

>[!ATTENTION] ✅PRO: Veloce e già ottimizzata                                                                                           ❌CONS: Non personalizzabile per la tua logica applicativa

## Opzione 2, Build da DockerFile
```Shell
services:
	api:
		build:
			context: ./api
			dockerfile: DockerFile
			args:
				NODE_VERSION: 20
		ports:
			-"5000:5000"
		
```

>[!ATTENTION] ✅**PRO**: Completamente personalizzabile, controllo totale sull'immagine ❌**CONS**: Richiede tempo di build gestione delle versioni

---
# **Ports: Mappatura delle Porte**
>La mappatura delle porte definisce quali porte del container sono raggiungibili dall'host. 
Il formato è sempre "PORTA-HOST:PORTA-CONTAINER"

```Shell
services:
	web: 
		image: nginx
		ports:
			-"8080:80"   #HOST:CONTAINER
			-"443:443"
			-"127.0.0.1:3000:3000"   #SOLO LOCALHOST
			
```

>Quando il browser richiede localhost:8080, Docker instrada il traffico verso la porta 80 del container Nginx. 

>[!NOTE] L'Host e il container usano porte indipendenti

>[!IMPORTANT] **✅Best Practices:**
>- **Porte non privilegiate**
  usa porte > 1024 sull'host per evitare problemi di permessi
> - **Documenta le porte**
  Tieni aggiornato il README con tutte le porte esposte
> - **Non esporre DB**
  Database e cache devono essere raggiungibili solo internamente - nessun ports!

---
# **Volumes: Persistenza dei Dati**

>I volumi sono il meccanismo di Docker per conservare i dati oltre il ciclo di vita di un container. Ne esistono **3** tipi, ognuno con scopi specifici:

## Named Volume:
>Gestito Interamente da Docker. 
>Docker crea una directory dentro /var/lib/docker/volumes/ con il nome specificato, sulla macchina HOST. E docker se la gestisce da sola la directory.
  Cross-Platform, performance ottimali, sopravvive a docker compose down. Ideale per Database e dati Persistenti

```Shell
volumes:
	- pgdata:/var/lib/postgresql/data
```

## Bind Mount:
>Mappa una cartella locale nel container. Accesso diretto ai file, hot reload immediato. Ideale per codice sorgente e configurazioni in sviluppo

```Shell
volumes:
	- ./html:/usr/share/nginx/html
	- ./config:/etc/myapp:ro
```

## Anonymous Volume
>Temporaneo, distrutto al docker compose down. Da usare solo per cache e file temporanei che non devo persistere

```Shell
volumes:
	- /tmp/cache   #Nessun Nome
  
```

---
# **Environment: Configurazione dei Servizi**
>**Le variabili d'ambiente sono il modo standard per configurare i container senza modificare il codice.  Esistono 3 approcci tra cui scegliere in base alla sensibilità dei dati.**

1. **Inline nel file YAML**:
   ✅*Semplice e leggibile*
   ❌*Non usare per Password*
   
```Shell
services:
	api:
		environment:
			NODE_ENV: production
			DB_HOST: db
			DB_PORT: 5432
   
```

2. **Da file .env**
   ✅*Informazioni sensibili separati e git-ignorati, supporta ambienti diversi*
```Shell
#Nel file .env
DB_PASSWORD=password_sicura
```

```Shell
#Nel file docker-compose.yml
environment:
	DB_PASSWORD:${DB_PASSWORD}
```

3. **Carica tutto il file .env**
   ✅*Carica tutte le variabili automaticamente, supporta più file in merge progressivo*

```Shell
services:
	api:
		env_file:
			- .env
			- .env.local  #Override locale
```

>[!IMPORTANT] **🔒Best Practice Security:**                                 
>- **Aggiungi .env al .gitignore**          
>- **Committa .env.example con valori fake**  
>- **Mai committare password in Git!**

---

# **depends_on**
>Ordine di avvio

>depends_on garantisce che i container vengano avviati nell'ordine corretto. Aspetta che il servizio sia UP, non che il servizio sia pronto ad accettare connessioni

>Esempio:
```d
services:
	api:
		depends_on:
		db:
			condition: service_healthy
		
	db:
		image: postgres:latest
		healthcheck:
			test["CMD", "pg_is_ready"]
			interval: 10s
			timeout: 5s
			retries: 5
```

>[!NOTE] Con condition: service_healthy l'API parte solo quando il DB è veramente pronto ad accettare connessioni - nessun errore di connessione al primo avvio

---

# **Networks**
>Comunicazione tra Servizi

>Docker compose crea automaticamente una rete per tutti i servizi. Ogni servizio è raggiungibile dagli altri usando il nome del servizio come hostname DNS.

>[!NOTE] Crea le Network ma su una ipv4 2^16-2 quindi per creare un collegamento tra due container crea una rete che poi potrebbe creare problemi di overlapping di rete



>[!IMPORTANT] Se non si specifica nulla tutti i servizi saranno collegati tra di loro perche docker compose crea automaticamente una rete default: 
>nomeprogetto_default

>[!IMPORTANT] Le reti custom permettono l'isolamento

>Esempio:
```yaml
services:
  web-app:
    image: nginx
    networks:
      - mia-rete

  api-service:
    image: my-api-image
    networks:
      - mia-rete

networks:
  mia-rete:
    driver: bridge
```

---
# **Esempio di uno stack completo con Docker compose**

```d
services:
	api:
		build: ./api
		depends_on:
			db:
				condition: service_healthy
			redis:
				condition: service_healthy
		ports:
			- "5000:5000"
		environment:
			DB_HOST: db
			REDIS_HOST: redis
		networks: [app-network]
	db:
		image: postgres:16-alpine
		volumes:
			- pgdata:/var/lib/postgresql/data
		environment:
			POSTGRES_PASSWORD: ${DB_PASSWORD}			
		healthcheck:
			test: ["CMD", "pg_isready"]
			interval: 10s
			networks: [app-network]
	redis:
		image: redis:7-alpine
		volumes:
			- redisdata:/data //named volume
		healthcheck:
			test: ["CMD", "redis-cli", "ping"]
		networks: [app-network]
volumes:
	pgdata:
	redisdata:

networks:
	app-network:
	driver: bridge
```