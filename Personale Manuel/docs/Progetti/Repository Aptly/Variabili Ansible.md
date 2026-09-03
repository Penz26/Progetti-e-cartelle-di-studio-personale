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