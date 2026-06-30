#Docker

# **COS' E' DOCKER?**
>Docker è una piattaforma open-source che rivoluziona il modo di sviluppare, distribuire e gestire applicazioni attraverso la tecnologia dei container.

# **COS'E' UN CONTAINER?**
>I container sono ambienti isolati che includono tutto il necessario per eseguire un applicazione: codice, runtime, librerie e dipendenze di sistema.

>Questa tecnologia consente agli sviluppatori di "impacchettare" (containerizzare) un applicazione con tutte le sue dipendenze in un'unità standardizzata, garantendo che funzioni in modo identico su qualsiasi ambiente.

# **CONTAINER vs MACCHINE VIRTUALI**
>Capire le differenze architetturali tra container e macchine virtuali è fondamentale per scegliere la tecnologia più adatta alla situazione.


>***Container Docker***
>- **Kernel** condiviso: tutti i container utilizzano il kernel del sistema host
>- **Leggeri**: dimensioni ridotte (MB), occupano minimo spazio
>- **Avvio istantaneo:** tempi di startup in millisecondi
>- **Maggiore densità:** centinaia di container su un singolo host
>- **Isolamento a livello processo:** utilizzano namespace e cgroups


>***Macchine Virtuali***
>**- Sistema operativo completo:** ogni VM ha il proprio kernel
>**- Pesanti:** dimensioni in GB, richiedono più risorse
>**- Avvio lento:** tempi di boot in minuti
>**- Minore densità:** decine di VM per host
>**- Isolamento hardware:** emulazione completa dell' hardware

>[!NOTE] I container Docker sono ideali per microservizi, sviluppo rapido e deployment agile, mentre le VM eccellono quando è necessario isolamento completo del sistema operativo o compatibilità con applicazioni legacy

---
# **Come installare Docker su Linux**
>Consultare la guida ufficiale della documentazione di Docker dalla loro pagina.

>L'installazione si compone di 5 fasi:

1. Aggiornare il sistema:
```Bash
sudo apt update
sudo apt upgrade
```

2. Installare prerequisiti
```Bash
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt//keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc   
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

3. Aggiungere repository Docker
```Bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update   
```

4. Installare Docker Engine (con i suoi plugin)
```Bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin   

#Il servizio starta automaticamente dopo l'installazione. Per verificare:

sudo systemctl status docker

#Certi sistemi invece potrebbero richiedere un avvio manuale con:

sudo systemctl start docker
```

5. Verifica l'installazione eseguendo il modulo hello-world
```Bash
sudo docker run hello-world   
```

6. Per far girare docker senza usare sudo fare:
```shell
#Aggiunge lo user attuale al gruppo docker
sudo usermod -aG docker $USER

#applica le modifiche ai gruppi
newgrp docker

#verificare che funzioni
docker ps

```
---
# **ARCHITETTURA DI DOCKER**

**Docker Daemon:**
>Il demone (dockerd) è un processo che continua a essere eseguito in background e attende i comandi dal client. Il demone è in grado di gestire vari oggetti Docker.

**Docker Client:**
>Il client (docker) è un'interfaccia da riga di comando principalmente responsabile del trasporto dei comandi lanciati dagli utenti.

**REST API:**
> L'API REST agisce come un ponte tra il demone e il client. Ogni comando lanciato usando il client passa per l'API per raggiungere il demone alla fine predefinito per Docker. Un altro registro di immagini molto popolare è Quay di Red Hat.


---
# **COMANDI DOCKER BASE**

## Docker Pull
>Il comando docker pull scarica immagini Docker da repository remoti, tipicamente Docker Hub, il registro pubblico principale che ospita migliaia di immagini pronte all'uso.

- Sintassi e Utilizzo
>**Scaricare immagine ufficiale (ultima versione)
```d
docker pull nginx
```

>**Scaricare versione specifica**
```D
docker pull nginx:1.25.3
```

>**Scaricare da registro alternativo**
```D
docker pull ghrc.io/organization/image:tag
```

>**Scaricare tutte le versioni (tag)**
```D
docker pull -a nginx
```

- Struttura Tag Immagini (la parte dopo i : )
>latest -tag predefinito, ultima versione stabile
>version -tag specifico (es: 1.25, 20.04)
>alpine -variante leggera basata su Alpine Linux (lightweight)
>slim -versione ridotta con meno componenti

---
## Docker Run
>Il comando docker run è il cuore dell'utilizzo di Docker: crea e avvia un container basato su un immagine specificata. Questo comando combina diverse operazioni in un singolo passaggio.

-Esempi Pratici

>Esecuzione base
```D
docker run nginx
```

>Container in background (detached)
```D
docker run -d nginx
```

>Mapping porte (prima host e poi container (**host:container**))
```D
docker run -d -p 8080:80 nginx
```

>Assegnare un nome al container
```D
docker run -d --name webserver nginx
```

>Variabili d'ambiente
```D
docker run -e MYSQL_ROOT_PASSWORD=secret_password
```

>Montare Volume (prima host e poi container (**host:container**))
```D
docker run -v /host/data:/container/data nginx
```

- Opzioni Comuni

| **-d**     | esegui in background                        |
| ---------- | ------------------------------------------- |
| **-p**     | pubblica le porte                           |
| **--name** | assegna un nome personalizzato              |
| **-v**     | monta un volume per la persistenza dei dati |
| **-e**     | imposta variabili d'ambiente                |
| **--rm**   | rimuovi container dopo l'arresto            |
| **-it**    | modalità interattiva con terminale          |

---

## Docker ps
>Il comando docker ps visualizza informazioni sui container in esecuzione, fornendo una panoramica dello stato del sistema Docker. E' uno degli strumenti più utilizzati per il monitoraggio dei container

>Container Attivi
>- Mostra solo i container attualmente in esecuzione con informazioni essenziali
```D
docker ps
```

>Tutti i Container
>- Include anche container fermati, in pausa o terminati con errori
```D
docker ps -a
```

>Ultimi creati
>- Mostra gli ultimi N container creati, utile per debug recenti
```D
docker ps -n 5
```

>Solo ID
>- Output solo degli ID container, perfetto per scripting e automazione
```D
docker ps -q
```

--- 

## Gestire ciclo di vita dei container

1. Fermare
```D
docker stop <container>   
```
2. Terminare
```D
docker kill <container>   
```
3. Rimuovere
```D
docker rm <container>   
```
4. Riavviare
```D
docker restart <docker>   
```

- Comandi di Pulizia

>Rimuovere container fermato
```D
docker rm nome_container
```

>Rimuovere con forza (anche in esecuzione)
```D
docker rm -f nome_container
```

>Rimuovere tutti i container fermati
```D
docker containe prune
```

>Rimuovere container e volume
```D
docker rm -v nome_container
```

- Operazioni di Massa

>Fermare tutti i container in esecuzione
```D
docker stop $(docker ps -q)
```

>Rimuovere tutti i container
```D
docker rm $(docker ps -aq)
```

>Pulizia completa sistema
```D
docker system prune -a
```

---

## Gestione delle immagini Docker
>Le immagini Docker sono template immutabili utilizzati per creare container. Comprendere come gestirle efficacemente è fondamentale per ottimizzare spazio disco e workflow di sviluppo.

>Ogni immagine è composta da layer sovrapposti che rappresentano modifiche incrementali. 

![Descrizione](layer_image.png)

>Questo sistema a layer permette di condividere componenti comuni tra immagini diverse, riducendo duplicazioni e spazio utilizzato.

- Elencare Immagini (visualizza tutte le immagini disponibili localmente con dimensioni e tag)
```D
docker image ls
```

- Rimuovere le Immagini (Elimina immagini non più necessarie per liberare spazio disco)
```D
docker rmi nginx:alpine
docker image rm <image-id>
```

- Ispezionare Immagini (Ottieni informazioni dettagliate su configurazione e layer dell'immagine)
```D
docker inspect nginx
docker history nginx
```

- Pulizia Immagini (Rimuovere immagini dangling o tutte quelle non utilizzate dai container)
```D
docker image prune
docker image prune -a
```

---
## **Docker exec**
>Per entrare all'interno di un container e lanciare comandi usiamo il comando
```sh
docker exec -it nome_container bash
```

>In questo modo entriamo come root nel container e avviamo una bash interattiva (-it) da cui possiamo vedere tutto ciò che vi è all'interno del container docker

---
## **Docker logs
>Permette di consultare i log del container. Utili i parametri -f e --since (stesso significato di journalctl)
```sh
docker log -f nome_container
```