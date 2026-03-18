#Docker [[Cos'è Docker]]  

# COS' E'?

Docker Compose è uno strumento per definire e gestire applicazioni Docker multi-container usando un file **YAML** .

E' il ponte tra i container individuali e un'applicazione completa e funzionante.

### Le sue funzioni principali:
- **Orchestrazione semplificata**
  gestisce più container come un'unica unità logica
- **Configurazione come codice**
  la config è versionata insieme al progetto
- **Riproducibilità totale**
  Stesso ambiente su dev, test e CI/CD senza differenze
- **Onboarding rapido**
  Un nuovo sviluppatore è subito operativo con un solo comando (docker compose up)


## NON SOSTITUISCE DOCKER, E' UNA SUA ESTENSIONE 

*Ideale per sviluppo, testing, demo, applicazioni single-host e*

Il file **YAML** è composto da tre sezioni che descrivono l'intera applicazione:
- *services (i container)*
- *volumes (la persistenza)*
- *networks (la comunicazione)*

### Comandi Essenziali
Padroneggiare questi comandi significa avere il pieno controllo dello stack

#### Avvio e Build

```SHell
#Avvia in foreground (vedi i log)
docker compose up

#Avvia in background (detached)
docker compose up -d

#Rebuild delle immagini + avvio
docker compose up --build
```

#### Stop e Rimozione

```Shell
#Ferma e rimuove container + network
docker compose down

#Ferma, rimuove e cancella volumi

```

#### Monitoring e Debug

Monitorare e fare debug di uno stack multi-container è semplice con i comandi integrati di compose.

##### Stato e risorse
```Shell
docker compose ps  #Lista dei servizi attivi
docker compose ps -a  #Include quelli fermi
docker compose stats  #Uso CPU/RAM in real time
```

##### Logs
```Shell
docker compose logs  #Tutti i log
docker compose logs -f  #Follow real time
docker compose logs -f api  #Solo servizio API
docker compose logs --tail=50  #Ultime 50 righe
docker compose logs --timestamp  #Con timestamp
```

##### Accesso ai Container

```Shell
 #Shell interattiva (immagini full)
 docker compose exec api bash
 
 #Shell alpine (immagini lightweight)
docker compose exec api sh

#Esegui comando one-shot
docker compose run api comando

```

##### Validazione
```Shell
docker compose config  #Valida YAML
docker compose config --service  #Lista servizi
```


### Servizi

- #### Image vs build
  Ogni servizio può usare un immagine già pronta da Docker Hub oppure costruirne una personalizzata partendo da un Dockerfile locale. La scelta dipende dal tipo di servizio da mettere su

#### Opzione 1, Immagine pre-costruita
```Shell
services: 
	nginx:
	image: nginx:alpine
	ports:
		-"80:80"
```

✅PRO: Veloce e già ottimizzata
❌CONS: Non personalizzabile per la tua logica applicativa

#### Opzione 2, Build da DockerFile
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

✅**PRO**: Completamente personalizzabile, controllo totale sull'immagine
❌**CONS**: Richiede tempo di build gestione delle versioni

### Ports: Mappatura delle Porte
La mappatura delle porte definisce quali porte del container sono raggiungibili dall'host. 
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

Quando il browser richiede localhost:8080, Docker instrada il traffico versoo la porta 80 del container Nginx. 

L'Host e il container usano porte indipendenti

✅**Best Practices:**
- **Porte non privilegiate**
  usa porte > 1024 sull'host per evitare problemi di permessi
- **Documenta le porte**
  Tieni aggiornato il README con tutte le porte esposte
- **Non esporre DB**
  Database e cache devono essere raggiungibili solo internamente - nessun ports!

### Volumes: Persistenza dei Dati

I volumi sono il meccanismo di Docker per conservare i dati oltre il ciclo di vita di un container. Ne esistono **3** tipi, ognuno con scopi specifici:
- ##### Named Volume:
  Gestito Interamente da Docker. 
  Cross-Platform, performance ottimali, sopravvive a docker compose down. Ideale per Database e dati Persistenti
```Shell
  volumes:
	  - pgdata:/var/lib/postgresql/data
```

- ##### Bind Mount:
  Mappa una cartella locale nel container. Accesso diretto ai file, hot reload immediato. Ideale per codice sorgente e configurazioni in sviluppo
```Shell
volumes:
	- ./html:/usr/share/nginx/html
	- ./config:/etc/myapp:ro
```

- ##### Anonymous Volume
  Temporaneo, distrutto al docker compose down. Da usare solo per cache e file temporanei che non devo persistere
```Shell
volumes:
	- /tmp/cache   #Nessun Nome
  
```

### Environment: Configurazione dei Servizi
**Le variabili d'ambiente sono il modo standard per configurare i container senza modificare il codice.  Esistono 3 approcci tra cui scegliere in base alla sensibilità dei dati.**

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
			- .env.local  #Override localee
```

🔒**Best Practice Security**
- **Aggiungi .env al .gitignore**
- **Committa .env.example con valori fake**
- **Mai committare password in Git!**