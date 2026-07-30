
#Linux 
# **Cos' è?**
>Ansible è un software open source che permette di  automatizzare la gestione di server remoti e ne controlla lo stato.

---

# **Struttura**
>La sua struttura necessita di **ALMENO** 3 cose:
> 1. Nodo di controllo
>    Un sistema su cui Ansible è installato. Si fanno partire i comandi da qua
> 2. Inventario
>    Una lista di node che verranno gestiti da Ansible. Lo si crea sul nodo di controllo per descrivere i deployment degli hosts[[#**Per cosa è utile?**]]
> 3. Macchina gestita
>    Un sistema remoto che viene controllato da Ansible

---
# **Per cosa è utile?**

>Ansible può essere usato per automatizzare qualsiasi task ripetitiva di configurazione, di aggiornamento, ecc...

>Usa degli script human-readable in formato .yml chiamati playbook per automatizzare le task. Si dichiara lo stato in cui dovrà essere la macchina sul playbook e successivamente Ansible farà il suo lavoro.


---

>**E' NECESSARIO Openssh** su ogni nodo per Ansible altrimenti non potrà lavorare su quei nodi Ansible
>La prima connessione ssh deve essere fatta manualmente per accettare il fingerprint che Ansible non riesce ad accettare.

>Creare una chiave ssh per Ansible
```sh
ssh-keygen -t ed25519 -C "Ansible"

#cambiare il nome in modo che si riconosca che sia la chiave di Ansible quando lo richiede dopo averla creata
~/.ssh/ansible.pub
#Niente passphrase

ssh-copy-id -i ~/.ssh/ansible.pub IP-Server
```

---
## **Creare la repo git per versionare Ansible successivamente**

>Creare la repository su github e successivamente clonarla sul proprio pc in locale con:
```sh
git clone git@github.com:Nome_Utente/Nome_della_Repo.git
```

---

# **Installazione di Ansible**
>Ci sono diversi modi per installare Ansible:
> 1. Dalla repository github ufficiale
> 2. Con pip install di python
> 3. Dalle repo ufficiali della propria distro

```sh
#1 Ansible Repo

#2 Python pip

python -m venv ansible_venv 
pip install ansible

#3
#Aggiornare sempre le repo dei pacchetti
sudo apt update

#Successivamente installare
sudo apt install ansible
```

## **Creazione del file inventory**
>In questo file inseriamo tutti gli IP dei server che vorremo gestire con Ansible.

```sh
192.168.1.111
192.168.1.166
ecc...
```

>In questi file possiamo raggruppare determinati IP di macchine in modo che facciano parte di un gruppo.

>Per farlo:
```yml
192.168.10.160

[webservers]
192.168.20.174
192.168.10.153

[databases]
192.168.50.10
```

---
## **Creazione del ansible.cfg**
>Creando questo file di configurazione ogni volta che facciamo partire un comando ansible leggerà questo file in modo da prendere in automatico certi dati come:
```sh
[defaults]
inventory = nome_dell_inventario
private_key_file = path/chiave/ssh
remote_user = nome_utente_remoto
ecc...
```

---
## **Comandi Ansible**

>Permette di controllare se tutto va facendo un semplice ping (vede se la chiave è stata autenticata sul server remoto)
```sh
ansible all --key-file ~/.ssh/ansible -i inventory  -u nome_utente -m ping

#--key-file: dice ad Ansible che chiave ssh usare per far la connessione
#-i: gli dice che file inventory usare (in questo caso si chiama inventory)
#-u: per specificare il nome dell'utente remoto sul server
#-m: l'azione (modulo) da svolgere

#Con il file ansible.cfg
ansible all -m ping
```

>Verificare il proprio inventario
```sh
ansible-inventory -i inventory.ini --list
```

>Vedere i propri host gestiti
```sh
ansible all --list-hosts
```

>Fa un report sul terminale delle informazioni che trova sul server
```sh
ansible all -m gather_facts

#se vogliamo limitare il report ad una sola macchina possiamo farlo con --limit
ansible all -m gather_facts --limit IP-Server
```

---
# **Collezioni della Community (Librerie di comandi)**
>In Ansible esistono gli equivalenti delle librerie della programmazione e sono chiamate collezioni.

>Per vedere quali sono installate:
```shell
ansible galaxy collection list
```

>Per leggere la documentazione di questa collezione:
```shell
ansible-doc nome-collection.comando
```

>Per scaricarne una:
```shell
ansible galaxy collection install
```
---
# **Playbooks**
>I playbook sono piani di automazione scritti in yaml che Ansible usa per configurare i nodi gestiti. 
>Sono composti da:
>- plays: una lista ordinata di task che mappa i nodi gestiti in un inventario
>- tasks: un riferimento ad un unico modulo che definisce le operazioni che Ansible esegue
>- modules: un'unita di codice o binario che Ansible esegue su nodi gestiti. I moduli ansible sono raggruppati in collezioni con un nome.

```yml
- name: My first playbook
	hosts: myhosts
	tasks:
	 - name: Ping dei miei Hosts
	   ansible.builtin.ping:
	 - name: Saluto
	   ansible.builtin.debug:
	     msg: "ciao mondo"
```

>Per eseguirlo:
```sh
ansible-playbook -i inventory.ini playbook.yaml
```

>Possiamo notare che dà come risultato :
```yml
PLAY [My first play] ****************************************************************************

TASK [Gathering Facts] **************************************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

TASK [Ping my hosts] ****************************************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

TASK [Print message] ****************************************************************************
ok: [192.0.2.50] => {
    "msg": "Hello world"
}
ok: [192.0.2.51] => {
    "msg": "Hello world"
}
ok: [192.0.2.52] => {
    "msg": "Hello world"
}

PLAY RECAP **************************************************************************************
192.0.2.50: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.51: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.52: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

>Ci dà i nome dei play che sono stati invocati e le loro relative tasks.


>Possiamo inoltre notare che il primo task (Gather Facts) non lo avevamo specificato eppure lo ha fatto lo stesso. Questo perchè viene eseguito implicitamente per impostazione predefinitia.

>Il riepilogo riassume i risultati di tutte le attività, 3 ok (1 Gather, 1 ping, 1 msg)

----
# **Comandi con privilegi elevati**
>Se noi provassimo ad aggiornare il sistema con Ansible questo fallirebbe perchè non ha i privilegi di root. 
>Per farlo dobbiamo far sì che ansible possa essere utente sudo.


>**LA PASSWORD DEVE ESSERE DEL NODO GESTITO NON DEL GESTORE**
 
>Aggiornare le repository dei pacchetti (**sudo apt update**)
```sh
ansible all -m apt -a update_cache=true --become --ask-become-pass

-m apt: #usiamo il modulo apt
-a update_cache=true : #permette di usare un argomento per quel modulo (in questo caso aggiorna gli indici dei pacchetti, stessa cosa di fare sudo apt update)
-become: #ci permette di elevare i privilegi (di default usa sudo per elevare i privilegi)
--ask-become-pass: #chiede la password per il become (di default è sudo)
```

>Installare pacchetti (**sudo apt install**)
```sh
ansible all -m apt -a name=apache2 --become --ask-become--pass
-a name=nome_pacchetto: #installa il pacchetto specificato

#Se il pacchetto è già installato ma non è aggiornato alla latest release possiamo fare:
ansible all -m apt -a "name=apache2 state=latest" ---become --ask-become-pass
```

>Aggiornare il sistema (**sudo apt upgrade**)
```sh
ansible all -m apt -a upgrade=dist --become --ask-become-pass
```

---
# **Variabili**
>Possiamo rendere i nostri playbook più dinamici grazie alle variabili.

>Le variabili possono essere inserite direttamente nel playbook:
```yml
- name: Configurazione server web
  hosts: webservers
  vars:
    porta_web: 8080
    utente_admin: "sistemista"
  tasks:
    - name: Saluto dal server
      ansible.builtin.debug:
	     msg: "ciao mondo io sono {{utente_admin}}"
```

>Altrimenti possiamo specificarle all'interno di una directory chiamata group_vars/nome_gruppo.yml
>Oppure hosts/Ip.yml

```yaml
mio_progetto
|__main.yml
|__group_vars
	|_dbservers.yml
	|_webserver.yml
```

>In queste due cartelle Ansible va à cercare per il gruppo/host che gli abbiamo specificato nel playbook al parametro hosts: e troverà le variabili in automatico.


>Esempio di webservers.yml
```yml
ansible_user: manu
ansible_port: 22
```

## **Gerarchia delle variabili**
>Come vedremo più tardi usando i roles per dividere i vari soggetti del playbook Ansible dobbiamo distingure cosa ha più importanta e cosa invece viene per ultimo

```
[22] Extra Vars da riga di comando (`ansible-playbook -e "port=8080"`)  <-- VINCE SU TUTTO
   ▲
  [15] roles/nginx_server/vars/main.yml                                 <-- MOLTO FORTE (Difficile da sovrascrivere, VARIABILI COSTANTI pacchetti da installare ecc...)
   ▲
  [12] host_vars/server01.yml                                           <-- Specifico per singolo server
   ▲
  [6]  group_vars/aptly_servers.yml                                     <-- Specifico per gruppo     (cose che servono al singolo gruppo)
   ▲
  [3]  group_vars/all.yml                                               <-- Globale del tuo progetto (cose che servono a tutti)
   ▲
  [1]  roles/nginx_server/defaults/main.yml                             <-- DEBOLE (Facile da sovrascrivere, usate in caso lo user si dimentica di definire dei valori dentro group_var/nome_ruolo)
```

---
# **Condizionali**
>I Condizionali servono a rendere i tuoi playbook ancora più dinamici permettendo ad Ansible di eseguire una task solo se quella condizione è rispettata.

>Per farlo usiamo **when**

>In base a variabili od altre informazioni che Ansible prende in automatico con Gather Facts possiamo fare controlli su molti campi.

>Gli operatori logici per fare il confronto sono sempre i soliti:
>- == ;                            uguale a                   ; when: stato == "attivo"
>- != ;                             diverso da                ; when: ambiente != "test"
>- and ;                          e (entrambe vere)   ;  when: ambiente == "prod" and                                                                                                  ansible_facts['distribution'] == "Debian"
>- or ;                       oppure (almeno una vera)  ; when: ansible_facts['distribution'] ==                                                                             "Debian" or ansible_facts['distribution'] == Ubuntu
>- is defined ;                 la variabile esiste   ; when: mia_variabile is defined

>Esempio:
```sh
- name: Aggiorna cache pacchetti su Debian/Ubuntu
  apt:
    update_cache: yes
  when: ansible_facts['distribution'] == "Ubuntu"

- name: Aggiorna cache pacchetti su RedHat/CentOS
  dnf:
    update_cache: yes
  when: ansible_facts['distribution'] == "CentOS"
```

---
## **Register**

>Register ci permette di registrare il risultato di un comando precedente creando una variabile temporanea sul momento contenente tutte le info estratte dal modulo stat

>Esempio:
```yml
tasks:
    # 1. Controlliamo se esiste un certo file di manutenzione
    - name: Verifica presenza file di manutenzione
      ansible.builtin.stat:
        path: /etc/maintenance.lock
      register: file_manutenzione

    # 2. Rimuoviamo un servizio SOLO SE quel file esiste davvero
    - name: Notifica inizio manutenzione
      ansible.builtin.debug:
        msg: "Manutenzione in corso trovata!"
      when: file_manutenzione.stat.exists == true
```

---
# **Tags**
>I Tag sono etichette che si possono identificare delle task sotto un nome, la loro funzione principale è quella di dare controllo su cosa eseguire.

>Esempio:
```YAML
---
- name: Configurazione Server
  hosts: all
  tasks:
    - name: Installa il server web Nginx
      ansible.builtin.apt:
        name: nginx
        state: present
      tags: 
        - install
        - web

    - name: Copia la configurazione di Nginx
      ansible.builtin.template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags: 
        - configure
        - web

    - name: Configura il database MySQL
      ansible.builtin.apt:
        name: mysql-server
        state: present
      tags: 
        - install
        - db
```

>Per eseguire task con solo il tag "web" si usa la flag --tag:
```
ansible-playbook playbook.yml --tags "web"
```

>Per invece saltare task specifiche:
```shell
ansible-playbook playbook.yml --skip-tags "db"
```

>Esistono dei tag specifici:
>- **always:** una task con questo tag verrà eseguito sempre se non viene esclusa esplicitamente
>- **never:** una task con questo tag non verrà mai eseguita se non esplicitamente
>- **tagged:** esegue solo le task che possiedono almeno un tag personalizzato
>- **untagged** esegue solo le task che non hanno alcun tag associato

---
# **Moduli per i playbook**
>I moduli dei playbook sono i campi che ci permettono di usare comandi all'interno di Ansible in modo che operi sul server che gli abbiamo specificato per quel playbook.

## **apt**
>Sincronizzazione repositories, aggiornamento pacchetti, gestione pacchetti
>==***PER DISTRO BASATE SU DEBIAN***==


```yaml
- name: Install apache httpd (state=present is optional)
  ansible.builtin.apt:
	name: apache2             #specifica il pacchetto da installare
    state: present            #indica lo stato del pacchetto da installare

- name: Update repositories cache and install "foo" package
  ansible.builtin.apt:
    name: foo
    update_cache: yes         #sincronizza con le repo 

- name: Remove "foo" package
  ansible.builtin.apt:
    name: foo
    state: absent             #rimuove il pacchetto specificato

- name: Install the package "foo"
  ansible.builtin.apt:
    name: foo

- name: Install a list of packages
  ansible.builtin.apt:
    pkg:
    - foo
    - foo-tools

- name: Install the version '1.00' of package "foo"
  ansible.builtin.apt:
    name: foo=1.00

- name: Update the repository cache and update package "nginx" to latest version using default release squeeze-backport
  ansible.builtin.apt:
    name: nginx
    state: latest
    default_release: squeeze-backports
    update_cache: yes

- name: Install the version '1.18.0' of package "nginx" and allow potential downgrades
  ansible.builtin.apt:
    name: nginx=1.18.0          #Installa una versione specifica del pacchetto
    state: present
    allow_downgrade: yes

- name: Install zfsutils-linux with ensuring conflicted packages (e.g. zfs-fuse) will not be removed.
  ansible.builtin.apt:
    name: zfsutils-linux
    state: latest
    fail_on_autoremove: yes

- name: Install latest version of "openjdk-6-jdk" ignoring "install-recommends"
  ansible.builtin.apt:
    name: openjdk-6-jdk
    state: latest
    install_recommends: no

- name: Update all packages to their latest version
  ansible.builtin.apt:
    name: "*"
    state: latest

- name: Upgrade the OS (apt-get dist-upgrade)
  ansible.builtin.apt:
	upgrade: dist              #aggiorna il sistema

- name: Run the equivalent of "apt-get update" as a separate step
  ansible.builtin.apt:
    update_cache: yes

- name: Only run "update_cache=yes" if the last one is more than 3600 seconds ago
  ansible.builtin.apt:
    update_cache: yes
    cache_valid_time: 3600

- name: Pass options to dpkg on run
  ansible.builtin.apt:
    upgrade: dist
    update_cache: yes
    dpkg_options: 'force-confold,force-confdef'

- name: Install a .deb package
  ansible.builtin.apt:
    deb: /tmp/mypackage.deb

- name: Install the build dependencies for package "foo"
  ansible.builtin.apt:
    pkg: foo
    state: build-dep

- name: Install a .deb package from the internet
  ansible.builtin.apt:
    deb: https://example.com/python-ppq_0.1-1_all.deb

- name: Remove useless packages from the cache
  ansible.builtin.apt:
    autoclean: yes

- name: Remove dependencies that are no longer required
  ansible.builtin.apt:
    autoremove: yes

- name: Remove dependencies that are no longer required and purge their configuration files
  ansible.builtin.apt:
    autoremove: yes
    purge: true

- name: Run the equivalent of "apt-get clean" as a separate step
  ansible.builtin.apt:
    clean: yes
```

## **packages**
>Permette ad Ansible di rilevare in automatico il package manager utilizzato dalla macchina su cui opera.

>(Sono un po' gli stessi comandi di apt. )
## **service**
>Gestione dei servizi (l'equivalente di systemctl)

```yml
- name: Fa partire il servizio httpd se non era già avviato
  ansible.builtin.service:
    name: httpd
    state: started

- name: Ferma il servizio httpd se in funzione
  ansible.builtin.service:
    name: httpd
    state: stopped

- name: Riavvia il servixe httpd in ogni caso 
    ansible.builtin.service:
    name: httpd
    state: restarted

- name: Ricarica le configurazioni del servizio in ogni caso  httpd
  ansible.builtin.service:
    name: httpd
    state: reloaded

- name: Abilita il servizio httpd, non tocca attuale stato
  ansible.builtin.service:
    name: httpd
    enabled: yes

- name: Start service foo, based on running process /usr/bin/foo
  ansible.builtin.service:
    name: foo
    pattern: /usr/bin/foo
    state: started

- name: Restart network service for interface eth0
  ansible.builtin.service:
    name: network
    state: restarted
    args: eth0
```

## **Copy**

>Permette di copiare un file dalla macchina host di Ansible al client su cui stiamo facendo agire il playbook
```yml
- hosts: webservers
  become: true
  tag: apache2
  - name: Copiare file predefinito di index.html
    copy:
	  src: path/al/nuovo/file
	  dest: /var/www/html/index.html
	  owner: root          #opzionali
	  group: root          #opzionali
	  mode: 0644           #opzionali
```

## **unarchive**

>Permette di unzippare


## **assert**

>Funziona come un if della programmazione
```yml
- name: Verifica se la VM esiste su NetBox
	ansible.builtin.assert: #ansible.builtin.assert funziona come un if nella programmazione
		that:
			- netbox_api_response.json.results | length > 0 #condizione da controllare
		fail_msg: "ERRORE: La VM '{{ target_vm_name }}' non è stata trovata su NetBox!" #Risposta di errore
		success_msg: "Sincronizzazione completata: VM trovata con successo su NetBox." #Risposta di successo
```
## **uri**

>Permette di fare richieste HTTP
```yml
- name: Recupera i dettagli della VM da NetBox tramite API REST
	ansible.builtin.uri: #Con questo modulo possiamo fare delle richieste HTTP alla nostra dashboard di Netbox
		url: "{{ netbox_api_url }}/api/virtualization/virtual-machines/?name={{ target_vm_name }}" #specifichiamo l'url del nostro menù con la nostra variabile, e poi passiamo anche il PATH
#in cui va a cercare la nostra vm con ?name={{ target_vm_name }}
		method: GET
		headers:
			Authorization: "Token {{ netbox_token }}" #Qui diamo i parametri per poter accedere a questo PATH
			Accept: "application/json" #Bash Specifichiamo il tipo di formato che richiediamo
		status_code: 200
	register: netbox_api_response #Salva TUTTA la risposta JSON in questa variabile
```
## **set_fact**

>Crea o modifica una variabile
```yml
- name: Estrai e salva i dati utili della VM
	ansible.builtin.set_fact: #Crea o aggiorna una variabile (in questo caso crea)
		vm_details: "{{ netbox_api_response.json.results[0] }}"
```

---
# **Template**
>Un template in Ansible non è altro che un file di configurazione (es. .conf .ini .html) che contiene delle variabili e delle logiche

## **Cosa fa?**
1. Legge il file di partenza sul computer locale (il file ha l'estensione .j2)
2. Sostituisce le variabili con i valori reali specificati per quel determinato server o gruppo
3. Invia il file "compilato" e personalizzato sul server remoto

## **Sintassi**

>Le {{}}  servono a inserire il valore di una variabile definita in group_vars/ , nei /defaults del ruolo o estratta dai facts di Ansible
```yml
Port {{ ansible_port }}
ListenAddress {{ ansible_default_ipv4.address }}
```

>Le {%  ...  %} servono a introdurre della logica
```yml
{% if ambiente == "produzione" %}
LogLevel ERROR
{% else %}
LogLevel DEBUG
{% endif %}
```

## **Come si usano nei task**

```yml
- name: Genera il file di configurazione
  ansible.builtin.template:
    src: site.conf.j2                 # Nome del file di origine (nella cartella templates/)
    dest: /etc/nginx/sites-available/default  # Percorso di destinazione sul server remoto
    owner: root                       # Proprietario del file (opzionale)
    group: root                       # Gruppo del file (opzionale)
    mode: '0644'                      # Permessi del file (opzionale)
  notify: Riavvia Nginx               
```


---
# **Ruoli**

>Un ruolo è una struttura standardizzata di cartelle in cui Ansible organizza in modo ordinato:
>- Tasks
>- Handlers
>- Variabili
>- Template Jinja2

>Così da non avere un file yaml lunghissimo e dividderlo in sottoparti più ordinate in base al ruolo (webserver, database, ecc...)

>La struttura che andrà a creare Ansible sarà:
```
roles/
└── webserver/
    ├── tasks/
    │   └── main.yml      # I task principali da eseguire
    ├── handlers/
    │   └── main.yml      # Gli handler (es. restart di Nginx)
    ├── templates/
    │   └── site.conf.j2  # I file Jinja2 da elaborare
    ├── vars/
    │   └── main.yml      # Variabili ad alta priorità per il ruolo
    ├── defaults/
    │   └── main.yml      # Variabili di default (a bassa priorità, sovrascrivibili)
    └── meta/
        └── main.yml      # Dipendenze del ruolo e metadati
```


## **Come si crea un ruolo**

```shell
ansible-galaxy role init roles/webserver
```

>Quando si esegue un playbook come:
```
- name: Deploy dell'infrastruttura web
  hosts: webservers
  become: true
  roles:
    - webserver
```

>Ansible va nella cartella roles/webserver/tasks/main.yml esegue i task, prende le variabili da defaults/main.yml  e gestisce gli handers/main.yml in automatico.

---
# **Vault Ansible**

>Un vault di Ansible ci permette di crittografare dati sensibili (es. become-pass per uno dei nostri nodi gestiti ,ansible_user, ecc...)

>Quando cifriamo un file con un vault il suo contenuto diventa illegibile a noi ma per Ansible è chiara. All' esecuzione di un playbook che necessita una delle variabili all'interno del vault li decifra al volo **chiedendo però la password del vault**.

## **Come si usa:**

>[!IMPORTANT] Alla creazione di un nuovo vault oppure della cifratura di un file già esistente chiederà un password per tale cifratura**

>Creare un file cifrato:
```shell
ansible-vault create group_vars/nome_gruppo/vault.yml
```

>Cifrare un file già esistente:
```sh
ansible-vault encrypt group_vars/all/secrets.yml
```

>Modificare un file criptato usando neovim:
```sh
EDITOR=nvim ansible-vault edit group_vars/all/secrets.yml
```

>Eseguire un playbook che richiede delle variabili protette da un vault:
```
ansible-playbook playbook.yml --ask-vault-pass
```

>Se non si vuole dover inserire la password del vault ogni volta si può far leggere ad Ansible la password del vault in 2 modi:

1. Eseguire il playbook con:
```sh
ansible-playbook -i inventory.ini playbook.yml --vault-password-file ~/.ansible_vault_pass   
```
2. **VERA AUTOMAZIONE (dentro ansible.cfg)**
```shell
[defaults]
inventory = inventory.ini
vault_password_file = ~/.ansible_vault_pass   
```
>In questo modo Ansible leggendo la sua configurazione troverà il percorso del file con la password e la potrà leggere direttamente da lì.
>E si potrà eseguire semplicemente:
```shell
ansible-playbook playbook.yml
```

>[!ATTENTION] Se il file con la Password è all'interno di una repo github includere il file dentro il .gitignore