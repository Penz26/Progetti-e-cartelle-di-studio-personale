#Lugma

23/05/2026
> 11:00

# **Docker**
>Container sappiamo cosa sono

>Open Container Initiative
>Progetto della Linux Foundation avviato nel giugno 2015 da Docker, CoreOS e dai manutentori di appc per progettare standard aperti per la virtualizzazione a livello sistema operativo

>Principi 3:
>1. a
>2. b
>3. c

>Docker conforme alle specifiche OCI, ha donato il codice di runc, le immagini create con Docker possono eseguite su altri runtime conformi (es. podman).
>I container si basano su feature native del kernel Linux (namespaces, cgroups, union filesystem) è possibile eseguire solo kernel di Linux.


>LXC  container cosa cambia, all'inizio avevano più o meno le stesse specifiche e standard
>Il container lxc prende l'idea della VM ma la standardizza a quella di un Container

>Immagine Docker e Filesystem, stampino dell'oggetto che eseguirò come applicazione (es. apache ecc...) queste immagini sono costituite da più layer aggiuntivo read-write (**IMMAGINE SOLO READ ONLY**) consentendo al container di comportarsi come se stesse utilizzando un filesystem standard

>Container sono fatti per essere distrutti e ripresi

>**Filesystem Docker**
>Come far sì che i Dati del container possano rimanere anche dopo aver ucciso il container?

>Con i Volumes
>(drclone e reclone per storage S3)
>3 tipologie:
- named volume
- bind mount
- anonymous Volume

>Consigli di installazione Docker
>Installare tramite le istruzioni sul loro sito ufficiale
>Una volta installato, Docker autorizza comandi solamente dall' Utente root. Dobbiamo aggiungere il nostro utente al gruppo docker tramite il comando 

```sh
sudo usermod -a -G docker $USER
```

>Le varie immagini Docker vengono create a partire da file chiamati DockerFile

>Parlato di docker images, docker ps, dockerfile, docker compose, docker exec, docker logs

---
12:00

# **HomeLab**
[Dispense e PowerPoint](https://git.sys42.eu/syntaxerrormmm/homelabbing/releases/download/v0.9.4/slides.pdf)

>Definizione e solite cose di hardware ricondizionato

>Ui per Ansible/Terraform scritto in Php
[Semaphore](https://semaphoreui.com/)

>Restic per backups, oppure borg