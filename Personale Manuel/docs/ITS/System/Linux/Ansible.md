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
#File con gli Ip dei server che vorremo gestire con Ansible
192.168.1.111
192.168.1.166
ecc...
```

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