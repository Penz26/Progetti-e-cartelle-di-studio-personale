
# Da fare:
 - [x] Aggiungere controllo dell'esistenza della repository aptly
 - [ ] **automazione della configurazione del server aptly con Ansible**
 - [x] Creare DOC How-To per spiegare in modo chiaro il funzionamento e l'utilizzo della pipeline
 - [x] Specificare diversi Dockerfile per ogni versione ISO (pacchetti per la compilazione, comandi di update, ecc...)
 - [x] Velocizzare creazione delle immagini docker per la compilazione
 - [x] Singoli push per ogni pacchetto OPPURE Permettere la compilazione e la pubblicazione di più file alla volta??
# **Gestione del runner:**

## Compiti
>**1 runner su una VM per:** 
>- la compilazione dei pacchetti, 
>- spostamento in scp dei file compilati dalla vm di compilazione a quella di pubblicazione
>- creazione dello snapshot in ssh dentro la VM di pubblicazione
>- Pubblicazione dello snapshot in ssh dentro la VM di pubblicazione

---
## Privilegi e requisiti sulla macchina di compilazione:

>**REQUISITI**
>Il runner sulla macchina di compilazione deve poter usare sudo per:
- docker senza sudo (sudo usermod -aG docker gitlab-runner)
- avere come executor dentro il suo config.toml docker

>**PRIVILEGI**

> - Utente GitLab fa parte del gruppo docker
```shell
sudo usermod -aG docker gitlab-runner
```

>Chiave ssh per autenticarsi alla macchina di pubblicazione
```shell
ssh-keygen -t ed25519 -C "gitlab-runner-deployer"

#Visto che al deployer non si può accedere con password
#Bisogna copiare la chiave PUBBLICA manualmente dentro /home/deployer/.ssh/authorized_keys

```


>Sul container di pubblicazione copiare ed usare questa chiave
>**USARLA ANCHE PER SCP**
```shell
- echo "Creazione directory .ssh"
- mkdir -p ~/.ssh
- chmod 700 ~/.ssh
- echo "Creazione del file con la chiave per accedere allo user APTLY"
- touch ~/.ssh/deployer_key
- chmod 600 ~/.ssh/deployer_key
- echo "${DEPLOYER_SSH_KEY}" | tr -d '\r' > ~/.ssh/deployer_key
- echo "Crea il file di config per entrare in automatico con la chiave giusta"
- |
  cat <<EOF > ~/.ssh/config
  Host ${APTLY_SERVER_IP}
  User ${APTLY_USER}
  IdentityFile ~/.ssh/deployer_key
  IdentitiesOnly yes
  EOF
- ssh-keyscan -H ${APTLY_SERVER_IP} >> ~/.ssh/known_hosts
```
---
## Privilegi e requisiti sulla macchina di pubblicazione:

>**REQUISITI**
>1. Il runner deve accedere in ssh come utente limitato al server-aptly. 
>2. L'utente sotto cui si connette in ssh sul server aptly deve essere abilitato **SOLO** all'esecuzione di comandi aptly come sudo per l'aggiunta dei pacchetti .deb alla repo, creazione e pubblicazione dei pacchetti.

>**PRIVILEGI**
>- Creazione utente sulla VM di Aptly per il runner
```shell
#Creiamo l'utente deployer, togliamo la possibilità di entrare con password in modo che sia accessibile solo via ssh gecos così da precompilare le info dello user
adduser --disabled-password --gecos "GitLab Deployer Account" deployer
```
> - Gestione privilegi come sudo per questo user in /etc/sudoers.d
```shell
deployer ALL = (root) NOPASSWD: /usr/bin/aptly
```

---
# **Variabili su GitLab**

- CHIAVE SSH PER CONNESSIONE AL DEPLOYER
- CHIAVE GPG DELLA REPOSITORY
- PASSPHRASE DELLA CHIAVE GPG

---

**GESTIONE DI CARTELLA DI FILE O DI SINGOLO SCRIPT**
>Nel caso deve essere aggiunta una intera cartella da compilare in formato .deb la variabile PACKAGE_EXT dovrà essere vuota. Mentre se è un singolo file la variabile PACKAGE_EXT dovrà essere uguale a .ext (es. .sh oppure .cpp oppure .py ecc...)

---
# **Gestione della creazione di più immagini per la compilazione**

>Definiamo un argomento predefinito per l'immagine base
```dockerfile
ARG BASE_IMAGE=ubuntu:24.04
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    dpkg-dev \
    build-essential \
    fakeroot \
    debhelper \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
```

>Adesso quando ci servirà creare una nuova immagine per una diversa versione/release di Debian/Ubuntu ci basterà creare il container passandogli quella come argomento:
>==***Già automatizzato dentro la pipeline***==
```shell
#Per crearla con ubuntu noble
docker build --build-arg BASE_IMAGE=ubuntu:24.04

#Oppure per debian bookwork
docker build --build-arg BASE_IMAGE=debian:bookworm
```

---
# **Compilazione e pubblicazione del pacchetto con diverse versioni di Debian/Ubuntu**

>[!IMPORTANT] Il Dev dovrà modificare solo i campi relativi al pacchetto e alla versione per cui compilare

>==***AGGIUNGERE CONTROLLO SE LA REPOSITORY DI QUELLA VERSIONE ESISTE O MENO***==

```yml
stages:
- build-builder
- build
- publish
variables:
# =========================================================================
# SCHEDA PACCHETTO (Modificabile dallo Sviluppatore)
# =========================================================================
  PACKAGE_NAME: "pipeline"
  PACKAGE_VERSION: "1.0.0"
  PACKAGE_ARCHITECTURE: "amd64"
  PACKAGE_MAINTAINER: "Manuel Bernardelli"
  PACKAGE_DESCRIPTION: "Flusso CI/CD Enterprise per pacchetti Debian"

# =========================================================================
# PARAMETRI APTLY & DESTINAZIONE (VM 2)
# =========================================================================
  NOME_REPO: "Manuel-prod"
  DISTRIBUTION: "noble"
# Prefix di pubblicazione nell'URL (es. "." per root, "dev", "testing")
  PREFIX: "."

# Indirizzo IP e utente Linux dedicato sulla VM 2 (Server Aptly)
  APTLY_SERVER_IP: "192.168.1.50"
  APTLY_USER: "deployer"
  
# =========================================================================
# STAGE 0: AUTOMAZIONE CONTAINER BUILDER (Gira solo se cambia il Dockerfile)
# =========================================================================

build-builder-images:
  stage: build-builder
  image: docker:24.04
  tags:
    - compile-runner
  services:
	- docker:24.04-dind
  rules:
	- changes:
	  - Dockerfile.builder
	  - .gitlab-ci.yml
  before_script:
	- docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY

# ===========================================================================
# PER COMPILARE PER UNA NUOVA IMMAGINE/VERSIONE DI Debian/Ubuntu AGGIUNGERE A QUESTO ELENCO
# LA VERSIONE E IL SUO TAG_NAME
# ===========================================================================
  parallel: #Permette la creazione/aggiornamento in temporanea del registry delle immagini docker
	matrix:
	  - BASE_IMAGE: "ubuntu:24.04"
	    TAG_NAME: "ubuntu-noble"
	  - BASE_IMAGE: "debian:12"
		TAG_NAME: "debian-bookworm"
  script:
	- echo "=== Compilazione e Push Immagine Builder per ${TAG_NAME} ==="
	- docker build --build-arg BASE_IMAGE=${BASE_IMAGE} -t $CI_REGISTRY_IMAGE/deb-builder:${TAG_NAME} -f Dockerfile.builder .
	- docker push $CI_REGISTRY_IMAGE/deb-builder:${TAG_NAME}

# =========================================================================
# STAGE 1: COMPILAZIONE PARALLELA DEL PACCHETTO .DEB
# =========================================================================
build-package:
  stage: build
  tags:
	- compile-runner
# Utilizza l'immagine pre-built dal Registry di GitLab creata dallo Stage 0
  image: $CI_REGISTRY_IMAGE/deb-builder:${TARGET_OS}
# Esegue 2 job paralleli sulla VM 1 usando le 2 immagini pre-compilate
  parallel:
    matrix: 
# ========================================================================
	  - TARGET_OS: ["ubuntu-noble", "debian-bookworm"] # SPECIFICARE PER QUALI VERSIONI COMPILARE CON IL LORO RELATIVO TAG_NAME
# ========================================================================
  script:
	- echo "=== 1. Preparazione struttura del pacchetto per ${TARGET_OS} ==="
	- DEB_FILE="${PACKAGE_NAME}_${PACKAGE_VERSION}_${PACKAGE_ARCHITECTURE}_${TARGET_OS}.deb"
	- mkdir -p ${PACKAGE_NAME}/DEBIAN
	- mkdir -p ${PACKAGE_NAME}/usr/local/bin
	- echo "=== 2. Copia degli eseguibili e permessi ==="
	- cp src/* ${PACKAGE_NAME}/usr/local/bin/
	- chmod +x ${PACKAGE_NAME}/usr/local/bin/*
	- echo "=== 3. Generazione metadati DEBIAN/control ==="
	- |
	  cat <<EOF > ${PACKAGE_NAME}/DEBIAN/control
	  Package: ${PACKAGE_NAME}
	  Version: ${PACKAGE_VERSION}
	  Architecture: ${PACKAGE_ARCHITECTURE}
	  Maintainer: ${PACKAGE_MAINTAINER}
	  Description: ${PACKAGE_DESCRIPTION} (Target: ${TARGET_OS})
	  EOF

	- echo "=== 4. Compilazione pacchetto .deb ==="
	- dpkg-deb --build ${PACKAGE_NAME} ${DEB_FILE}
  artifacts:
	paths:
	  - "*.deb"
	expire_in: 1 day

# =========================================================================
# STAGE 2: PUBBLICAZIONE REMOTA SU APTLY (VM 1 -> VM 2 via SSH)
# =========================================================================

deploy-package:
  stage: publish
  tags:
	- compile-runner
  image: alpine:latest
  needs:
	- job: build-package
  artifacts: true
  before_script:
	- echo "=== Setup Client SSH e Autenticazione ==="
	- apk add --no-cache openssh-client
	- eval $(ssh-agent -s)
	- echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
	- mkdir -p ~/.ssh
	- chmod 700 ~/.ssh
	- ssh-keyscan -H ${APTLY_SERVER_IP} >> ~/.ssh/known_hosts
  script:
	- echo "=== 1. Inizio procedura di deploy per i pacchetti compilati ==="
# ========================================================================================
# SPOSTA OGNI FILE .deb COMPILATO PER OGNI VERSIONE SPECIFICATA PRIMA NEL JOB DI BUILD COME TARGET_OS SUL SERVER APTLY

# ES. 1°PACCHETTO NEL CICLO
# pipeline_1.0.0_amd64_ubuntu-noble.deb è il valore della variabile deb

# poi crea lo snapshot relativo a questo valore (togliendo il .deb alla fine con la regola %)
# pipeline-snap-a1b2c3d4-pipeline_1.0.0_amd64_ubuntu-noble (NOME SNAPSHOT FINALE)

# Dopodichè aggiunge il file alla repo
# sudo aptly repo add -force-replace ${NOME_REPO} /tmp/$deb

# Lo rimuove dai file temporanei
# rm -f /tmp/$deb
  
# CREA LO SNAPSHOT CON IL NOME DICHIARATO PRIMA
  - |
    for deb in *.deb; do
	  echo "--> Trasferimento di $deb sulla VM Aptly..."
	  scp "$deb" ${APTLY_USER}@${APTLY_SERVER_IP}:/tmp/
	  
	  # Generazione ID snapshot univoco per il pacchetto
	  SNAPSHOT_NAME="${PACKAGE_NAME}-snap-${CI_COMMIT_SHORT_SHA}-${deb%.deb}"
	  
	  echo "--> Esecuzione comandi Aptly remoti per $deb..."
	  ssh ${APTLY_USER}@${APTLY_SERVER_IP} "
	  sudo aptly repo add -force-replace ${NOME_REPO} /tmp/$deb && \
	  rm -f /tmp/$deb && \
	  sudo aptly snapshot create ${SNAPSHOT_NAME} from repo ${NOME_REPO} && \
		sudo aptly publish switch -batch -gpg-key=\"\${PERSONAL_APTLY_NOBLE_KEY}\" -passphrase=\"\${PERSONAL_REPO_GPG_KEY}\" ${DISTRIBUTION} ${PREFIX} \"${SNAPSHOT_NAME}\"

"
	done
	- echo "=== 2. Verifica dello stato attuale delle pubblicazioni ==="
	- ssh ${APTLY_USER}@${APTLY_SERVER_IP} "sudo aptly publish list"
```

---
## Come si deve poter operare con l'automazione in Ansible?

>Variabili Globali

- **all**
```shell
aptly_server_ip: "192.168.1.176"
```


>L'amministratore (credo) deve solo modificare il valore delle variabili dentro group_vars/ per ogni ruolo 

- **aptly_server**
```shell
# 1. Utente di sistema e percorsi per Aptly
aptly_user: "deployer"
aptly_root_dir: "/var/www/apt-repo"

#Variabili per la creazione della firma GPG
gpg_real_name: "Manuel Repository Signing Key" #Nome descrittivo della chiave
gpg_user_email: "deployer@azienda.local"
gpg_key_type: "RSA"
gpg_key_length: 4096
gpg_expire_date: "0" # "0" significa che la chiave non scade mai

#Variabili della repository da Creare
repo_name: "aptly-bookworm"
repo_distribution: "bookworm"
repo_component: "main"
repo_comment: "Repository Interna bookworm"
```

- pki_gpg
```shell
# 1. Cartella sul server in cui salvare tutti i certificati

pki_dir: "/etc/ssl/aptly_pki"

# 2. Parametri della CA (Root Certificate Authority - L'autorità che firma tutto)

ca_common_name: "Azienda Internal Root CA"
ca_valid_days: "+3650d" # Valido 10 anni

# 3. Parametri del Certificato per il Server Web (Nginx)

server_ip: "192.168.1.176"
server_valid_days: "+365d" # Valido 1 anno

# 4. Parametri del Certificato per il Client (mTLS per APT)

client_common_name: "apt-client-node"
client_valid_days: "+365d" # Valido 1 anno

# 5. Robustezza della chiave RSA (4096 bit è lo standard sicuro)

pki_key_size: 4096
```

- web-server
```shell
nginx_port: 443
server_name: 192.168.1.176 #Deve essere o l'ip della macchina su cui viene hostata la repository oppure il FQDN

  
# Percorsi dei certificati PKI generati dal ruolo pki_gpg pki_dir = /etc/ssl/aptly_pki/
ssl_cert_path: "/etc/ssl/aptly_pki/server.crt"
ssl_key_path: "/etc/ssl/aptly_pki/server.key"
ssl_ca_path: "/etc/ssl/aptly_pki/ca.crt"

  
# Root web per Aptly (configurata prima nel role di aptly)
aptly_public_dir: "/var/www/apt-repo/.aptly/public"


# CONFIGURAZIONE BASIC AUTH & RESTRIZIONI IP

htpasswd_path: "/etc/nginx/.htpasswd"

allowed_subnets:
  - "192.168.1.0/24"
  - "127.0.0.1"
```

- **GitLab runner**
```shell
# URL dell'istanza GitLab (può essere gitlab.com o la tua istanza self-hosted)

gitlab_url: "https://gitlab.com/"

# Configurazione dell'esecutore

runner_description: "Build Runner - VM Compilazione DEB"
runner_executor: "docker"
runner_default_image: "ubuntu:noble"
runner_tags: "docker,build-deb,noble"
runner_concurrent_jobs: 4

# Impostazioni di rete e sicurezza SSH per dialogare con Aptly

aptly_server_ip: "192.168.1.176"
aptly_deploy_user: "deployer"

# Parametri Docker Avanzati (DinD / DooD / Privileged)
# Necessari per la compilazione di immaggini docker in docker

runner_privileged: true
runner_network_mode: "host"
runner_volumes:
  - "/cache"
  - "/var/run/docker.sock:/var/run/docker.sock"

runner_dns:
  - "8.8.8.8"
  - "1.1.1.1"
```

- **apt-client**
```shell
# Indirizzo IP o FQDN del server Aptly
repo_server_ip: "192.168.1.176"

# Parametri della repository Debian/Ubuntu

repo_prefix: "prefix"
repo_distribution: "noble"
repo_component: "main"

# Credenziali Basic Auth (è consigliabile sovrascrivere la password tramite Vault)

basic_auth_user: "{{ htpasswd_user }}"
basic_auth_password: "{{ htpasswd_password }}"
```

---

# **Problema coi prefix nuovi**
>Se un developer pubblica su un nuovo prefix il client non ha ancora accesso alla pubblicazione nuova