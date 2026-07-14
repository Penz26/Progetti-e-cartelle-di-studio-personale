#Linux 

# **Cos' è?**
>Ansible è un software open source che permette di  automatizzare la gestione di server remoti e ne controlla lo stato.

---

# **Struttura**
>La sua struttura necessita di **ALMENO** 3 cose:
> 1. Nodo di controllo
>    Un sistema su cui Ansible è installato. Si fanno partire i comandi da qua
> 2. Inventario
>    Una lista di node che verranno gestiti da Ansible. Lo si crea sul nodo di controllo per descrivere i deployment degli hosts
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

>In queste due cartelle Ansible va à cercare per il gruppo/host che gli abbiamo specificato nel playbook al parametro hosts: e troverà le variabili in automatico.

>Esempio di webservers.yml
```yml
ansible_user: manu
ansible_port: 22
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
  ansible.builtin.apt:
    update_cache: yes
  when: ansible_facts['distribution'] == "Ubuntu"

- name: Aggiorna cache pacchetti su RedHat/CentOS
  ansible.builtin.dnf:
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
# **Moduli per i playbook**
>I moduli dei playbook sono i campi che ci permettono di usare comandi all'interno di Ansible in modo che operi sul server che gli abbiamo specificato per quel playbook.

## **apt**
>Sincronizzazione repositories, aggiornamento pacchetti, gestione pacchetti

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

## **service**
>Gestione dei servizi (l'equivalente di systemctl)

---
# **Ruoli**

>Un ruolo è una struttura standardizzata di cartelle in cui Ansible organizza in modo ordinato:
>- Tasks
>- Handlers
>- Variabili
>- Template Jinja2

>Così da non avere un file yaml lunghissimo lo dividiamo in sottoparti più ordinate in base al ruolo (webserver, database, ecc...)

## **Come si crea un ruolo**

```shell
ansible-galaxy role init roles/webserver
```