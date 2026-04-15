#Docker

# **COS' E' DOCKER?**
>Docker è una piattaforma open-source che rivoluziona il modo di sviluppare, distribuire e gestire applicazioni attraverso la tecnologia dei container.

# **COS'E' UN CONTAINER?**
>I container sono ambientati isolati che includono tutto il necessario per eseguire un applicazione: codice, runtime, librerie e dipendenze di sistema.

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
>**Sistema operativo completo:** ogni VM ha il proprio kernel
>**Pesanti:** dimensioni in GB, richiedono più risorse
>**Avvio lento:** tempi di boot in minuti
>**Minore densità:** decine di VM per host
>**Isolamento hardware:** emulazione completa dell' hardware

>[!NOTE] I container Docker sono ideali per microservizi, sviluppo rapido e deployment agile, mentre le VM eccellono quando è necessario isolamento completo del sistema operativo o compatibilità con applicazioni legacy

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