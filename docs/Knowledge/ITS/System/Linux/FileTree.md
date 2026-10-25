 #Linux

# **Filesystem Hierarchy Standard (FHS)**
>La gerarchia del Filesystem linux si articola in varie directories ognuna con la propria funzione,  capire come è strutturato il sistema su Linux renderà possibile una migliore navigazione e comprensione di come si muove il sistema.

---

## **root (/)**
>Tutto inizia da qui.

>All'interno della radice vi è l'intero albero dei file di sistema. Ogni file, ogni dispositivo, ogni punto di mount vive qui sotto.
>A differenza di Windows dove le unità ottengono lettere diverse, Linux monta tutto su un albero unificato. Una seconda unità come una chiavetta USB, una condivisione di rete si attaccano tutti da qualche parte sotto /

---

## **Directory di sistema essenziali**
>**/bin , /sbin , /usr , /etc , /var , /tmp**

## **/bin:** 
>contiene binari essenziali dell'utente: ls, cp, mv, bash, cat, ... il tipo di comandi che deve funzionare anche quando quasi nient'altro lo fa, anche durante la modalità di salvataggio a singolo utente o prima che /usr sia montato

## **/sbin:** 
>è la stessa cosa ma per i binari di amministrazione del sistema: fsck, ip, iptables, reboot, .. i comandi che genericamente vengono usati come root

>[!NOTE] Sulla maggior parte delle distribuzioni moderne /bin e /sbin sono collegamenti simbolici a /usr/bin e /usr/sbin. Su questi sistemi i file vivono fisicamente in /usr. Quindi per avere effettivi cambiamenti bisogna modificare i file dentro a /usr/bin oppure /usr/sbin.


## **/usr:**
>Questa è la directory più grande sulla maggior parte dei sistemi. Contiene la maggior parte del software installato, delle librerie e della documentazione per il normale utilizzo del sistema.

- **/usr/bin:** 
  la maggior parte dei comandi e delle applicazioni rivolte all'utente
  
- **/usr/sbin:**
  strumenti di amministrazione del sistema e non essenziali
  
- **/usr/lib:**
  librerie condivise per programmi in /usr/bin e /usr/sbin
  
- **/usr/local:**
  software compilato e installato manualmente, al di furi del gestore del pacchetto. E' qui che va la tua installazione Nginx o Python personalizzata costruita a mano in modo che non sia in conflitto con i pacchetti gestiti dalla distro
  
- **/usr/share:**
  dati indipendenti dall'architettura: pagine di manuale, file locali, icone e documentazione
  
- **/usr/include:**
  file di intestazione per lo sviluppo C e C++

>[!NOTE] Quando si compila qualcosa da sorgente ed eseguire ./configure && make && make install, si salva quasi sempre dentro /usr/local per impostazione predefinita, in questo il gestore di pacchetti non toccherrà /usr/local quindi le installazioni manuali rimangono pulite e separate

## **/etc:**
>All'interno di questa directory ci sono i file di configurazione a livello di sistema. Ogni servizio ha la sua configurazione qui, esempio(/etc/nginx , /etc/ssh/sshd_config, /etc/fstab , /etc/hosts). Non ci sono i binari ma solo file di testo che fungono da configurazione.

>Alcuni tra i file importanti che vale la pena conoscere:
>- **/etc/fstab:** Definisce i filesystem da montare all'avvio
>- **/etc/hosts:** Nome host statico alle mappature Ip
>- **/etc/passwd e /etc/shadow:** Informazioni sull'account utente
>- **/etc/resolv.conf:** Configurazione del resolver DNS
>- **/etc/sudoers:** Controlla chi può usare il comando sudo e come
>- **/etc/crontab:** Attività programmate a livello di sistema


## **/var**
>Contiene dati variabili: dati che cambiano durante un normale funzionamento del sistema, logs, database dei package manager, cache di applicazioni

>- **/var/log:** log di sistema e di applicazioni, prima tappa da visitare quando si fa debug di problemi (/var/log/syslog, /var/log/auth.log , /var/log/nginx)
>-  **/var/lib:** dati persistenti di applicazioni. Mysql memorizza i suoi database sotto /var/lib/mysql , docker memorizza le immagini e container dentro /var/lib/docker
>-  **/var/cache:** dati cache delle applicazioni (/var/cache/pacman/archives)
>-  **/var/spool:** dati in coda per l'elaborazione: stampa, posta, ecc
>-  **/var/tmp:** file temporanei che dovrebbero persistere attraverso riavvi (a differenza di tmp)

## **/tmp**
>Contiene file temporanei, su certi sistemi è un mount tmpfs in ram quindi ad ogni riavvio si azzera

---

# **Directories di avvio e del Kernel**

## **/dev**
>File dei dispositivi.
>Su linux ogni dispositivo viene rappresentato come file qui. Il tuo disco è /dev/sda o /dev/nvme0n1. Il terminale è /dev/tty.
>/dev/null è un buco nero elimina tutto quello che gli viene dato in pasto, ed è per questo che in degli script quello che non vogliamo processare viene reinderizzato qua.

>/dev è controllato da udev all'avvio. Quando inserisci una USB udev crea in automatico il rispettivo file.

>Alcuni utili sono:
>- **/dev/sda , /dev/sdb:** dischi SCSI/SATA 
>- **/dev/nvme0n1:** drive NVMe
>- **/dev/null:** elimina l'output
>- **/dev/zero:** fonte di byte null, utili per azzerrare dischi o creare file di test
>- **/dev/random , /dev/urandom:** fonti di dati casuali per crittografia ecc...
>- **/dev/ttyS0:** prima porta seriale

## **/proc**
>Un filesystem virtuale che esiste solo in memoria. Espone la visione del kernel di eseguire i processi e stato di sistema come file. Niente in /proc viene memorizzato su disco
>top, htop, uptime e altri comandi come questi prendono i loro dati da /proc

>Alcuni file interessanti:
>- **/proc/cpuinfo:** dettagli della CPU
>-  **/proc/meminfo:** disaggregazione dell'utilizzo della memoria
>-  **/proc/loadavg:** commissioni di carico e conteggio dei processi in esecuzione
>-  **/proc/uptime:** tempo di attività del sistema in pochi secondi
>-  **/proc/net/dev:** statistiche dell'interfaccia di rete
>-  **/proc/[PID]/:** Informazioni per processo per qualsiasi processo in esecuzione da parte del suo PID

## **/sys**
>Un altro filesystem virtuale come /proc ma più strutturato. Espone il modello di dispositivo del kernel: i dispositivi hardware, i driver e i sottosistemi del kernel

## **/run**
>Un tmpfs mount per dati che devono persistere tra il riavvio di applicazioni ma non tra reboot del pc. PID files, sockets

---

# **Directories Utente ed Home**

## **/home**
>Directory personale per gli utenti normali. Ogni utente ha la sua subdirectory, qui vivono le config personali degli utenti, documenti, ecc...

## **/root**
>La home directory dell'utente root in specifico. Rimane separata in modo che root abbia sempre una directory home funzionante anche quando /home non è montata o piena

---

# **Directory di mount ed opzionali**


## **/opt:**
>Software di terze parti che non seguono lo standard FHS vengono installate qua. Ogni pacchetto ha la sua subdirectory (es. chrome, zen, ecc...)

 ## **/srv**
 >Dati serviti dal sistema, ci andrebbero le radici dei documenti del server Web, dati FTP e contenuti simili sono pensati per andare qui secondo lo standard FHS ma su molti sistemi utilizzano /var/www per i contenuti web
 
 ## **/mnt**
 >E' un punto di montaggio generico per il montaggio temporaneo di filesystem manualmente. 

