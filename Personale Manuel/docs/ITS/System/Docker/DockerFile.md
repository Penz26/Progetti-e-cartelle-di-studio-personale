#Docker [[Cos'è Docker]]

# **COS'E' UN DOCKERFILE?**
>Un Dockefile è un documento di testo che contiene delle istruzioni necessarie per assemblare un' immagine Docker.
>Docker legge le istruzione dall'alto verso il basso es esegue ogni comando uno dopo l'altro, creando dei layer sovrapposti che compongono l'immagine finale.

# **PARAMETRI FONDAMENTALI**
>I comandi principali di un dockerfile sono:

## **1. FROM - La Base**
>Ogni dockerfile **deve** iniziare con questa istruzione. Specifica l'immagine di partenza su cui vuoi costruire la tua.

```Dockerfile
FROM python:3.9-slim
```

## **2. WORKDIR - La cartella di Lavoro**
>Imposta la directory di lavoro all'interno del container.
>E' l'equivalente del comando cd.
>Tutti i comandi successivi verrano svolti qui

```Dockerfile
WORKDIR /app
```

## **3. COPY e ADD - Trasferimento File(sorgente dall'host ---> container)**
>Entrambi servono a copiare file dal tuo computer (host) all'interno dell'immagine
>- COPY, copia file o directory
>- ADD, permette di scaricare file da URL o estratte automaticamente file compressi

>Esempio:
>Copia tutto quello che c'è nella cartella attuale nella cartella WORKDIR del container 
```Dockerfile
COPY . . 
```

## **4. RUN - Esecuzione Comandi**
>Viene usato per installare pacchetti aggiornare il sistema o configurare l'ambiente durante la fase di creazione dell'immagine. Ogni RUN crea un nuovo layer

```Dockerfile
RUN apt update && apt install -y git
```

## **5. ENV - Variabili d'ambiente**
>Definisce variabili  che saranno disponibili sia durante la Build che quando il container sarà in esecuzione

```Dockerfile
ENV APP_COLOR=blue
```

## **6. EXPOSE - Documentazione Porta**
>Informa Docker che il container ascolta su una specifica porta di rete.

>[!ATTENTION] Non apre effettivamente la porta verso l'esterno (per quello serve il comando docker run -p) serve come documentazione tra chi crea l'immagine e chi la usa.

```Dockerfile
EXPOSE 8080
```

## **7. CMD e ENTRYPOINT - L'Avvio**
>Indicano quale comando deve essere eseguito quando il container viene avviato
>- CMD: imposta un comando di default che può essere facilmente sovrascritto al momento del docker run
>- ENTRYPOINT: configura il container in modo che venga eseguito come eseguibile. Più difficile da sovrascrivere

>Il 1° elemento è l'eseguibile, ovvero cosa far partire
>Il 2° elemento o tutto quelle che segue sono i suoi argomenti

>Esegue il file app.py usando python
```Dockerfile
CMD ["python", "app.py"]
```

>Avvia il server nginx con delle opzioni specifiche
```Dockerfile
CMD ["nginx", "-g", "daemon off;"]
```

>Elenca i file nella cartella /app in modo long e mostrando anche quelli nascosti, e poi il container li chiude
```Dockerfile
CMD ["ls", "-la", "/app"]
```
---

# **📒 ESEMPIO COMPLETO DI DOCKERFILE**
>Rappresentazione di un dockerfile tipico per una applicazione node.js

```Dockerfile
# 1. Immagine di base
FROM node:18

# 2. Directory di lavoro
WORKDIR /usr/src/app

# 3. Copia i file delle dipendenze
COPY package*.json ./

# 4. Installa le dipendenze
RUN npm install

# 5. Copia il resto del codice
COPY . .

# 6. Esponi la porta 3000
EXPOSE 3000

# 7. Comando di avvio
CMD ["node", "index.js"]
```