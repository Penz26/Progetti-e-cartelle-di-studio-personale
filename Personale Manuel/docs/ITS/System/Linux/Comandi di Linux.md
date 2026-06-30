#Linux 
```Bash
echo("Messaggio") # printa il messaggio nel terminale
whoami # printa a schermo il nome dell utente

python3 nome_file.py # esegue un file in Python

man  #COMANDO PIU IMPORTANTE DI LINUX, PERMETTE DI LEGGERE LA DOCUMENTAZIONE DI UN COMANDO PERMETTENDO DI CAPIRE L UTILIZZO E VARIE FEATURE

expr 12346 + 7890 # permette di calcolare delle espression matematiche

name  "Manuel" # possiamo anche creare delle variabili

echo $name  #per printare la variabile mettiamo il $ davanti
echo Hello $name

history  #con history possiamo vedere la storia dei comandi che abbiamo inserito nel terminale

clear  #pulisce la shell da tutto quello che abbiamo scritto

pwd  #"print working directory" mostra la directory(cartella) in cui stiamo lavorando

ls  #list , mostra il contenuto della directory in cui siamo ora (working directory)
    -l  #mostra i permessi di ogni file e directory per esteso
    -a  #mostra i file nascosti

cd nome_directory #change directory, cambia la directory in cui si sta lavorando (working directory)

cd ..  #torniamo indietro alla parent directory

ls nome_directory  # mostra cosa c'è all'interno della directory specificata

cat  #concatenate, mostra il contenuto di un file

head -n numero_scelto file.txt # printa n righe del file partendo dall'inizio del file (header)

tail -n numero_scelto file.txt # printa n righe del file partendo dalla fine del file (tailer)


less file.txt #fa vedere il contenuto di un file una pagina, o una linea alla volta
    -N # mostra less ma con le righe numerate

touch file.txt # aggiorna la data di modifica e di accesso di un file, di default se il file specificato non esiste lo crea

mkdir nome_scelto # crea una directory ( cartella di windows) 

mv # sposta un file/directory da un posto all'altro, il posto in cui vuoi spostare il file non può essere la tua working directory #può anche rinominare un file

#per spostare un file è necessario specificare tutto il percorso di origine e poi quello di arrivo
        #esempio: mv worldbanc/public/products/credit_cards/tbills.txt worldbanc/public/products/investments

rm # cancella un file o una directory
    -r #cancella in modo ricorsivo (cancella la directory e quello che vi è  all' interno)

cp # copia un file da un posto a un altro
    -r #copia in modo ricorsivo il contenuto di un' intera directory

cd ~  #sposta alla home directory, 
#Home directory = directory dove ci sono i propri file personali, è anche la directory da dove si inizia

grep  #cerca una stringa in un file, è case sensitive quindi cercherà solo l'esatta stringa
        ESEMPIO: grep "CRITICAL"  2024-01-10.log
	    #può anche cercare una stringa in più file alla volta (grep "hello" hello.txt hello2.txt)
        -r #può anche cercare nella cartella corrente e le subcartelle (grep -r "hello" .) (mentre con il . cerca nella directory in cui siamo
		-o #cerca e mostra in base ad una cosa in specifico
		ESEMPIO: ip addr | grep -o "192.*" #cerca le cose dal 192 in poi e con .* mostra tutto quello che c'è dopo
find  #cerca files e directory attraverso il nome
        #esempi: 
        find some_directory -name "hello.txt"
        #cerca anche in base al tipo di file, 
        find some_directory -name "*.txt"
        #può anche cercare il file in base a una parola 
        find some_directory -name "*chad*"
        
        #ESEMPIO: 
        find public/products -name "*joint*"

wc  #comando che permette di contare quante e mostrare quante parole o byte sono presenti in un file
    #esempio: 
        wc worldbanc/public/pr_ideas.txt

systemctl  #permette di controllare lo stato dei servizi attraverso:
        start  #avvia un servizio
        #esempio: 
        sudo systemctl start apache2

        stop  #interrompe l'esecuzione del servizio in modo pulito

        status #permette di vedere lo stato del servizio specificato successivamente

        enable #configura l'avvio automatico al boot

        disable #toglie l'avvio automatico al boot
        
awk #comando che permette di filtrare in modo intelligente una riga data in input tramite | . Divide la riga in colonne e ti permette di manipolare quei dati con estrema precisione. Di default considera lo spazio come separatore tra una colonna e l'altra.
	"{print $1}" #stampa la prima colonna
	"{print $0}" #stampa l'intera riga
	"{print $NF}" #stampa il contenuto dell'ultima colonna
	"NR==1 {print $0}" #stampa esattamente il numero di riga che si specifica
			
	-F "value" #permette di cambiare il separatore
	#può anche accettare più di un divisore con:
	[valori]
	#esempio
	[/ :] #questo userà anche come divisori / lo spazio e i due punti
	
	#awk può anche avere delle condizioni per cui cercare seguendo questa sintassi /condizione/
	#esempio:
	ip addr | awk '/inet / {print $2}'
	
----------------------------------------------------------------------------

VISUALIZZAZIONE E CONTROLLI PROCESSI 


ps #mostra i processi attivi nel sistema
    ps aux #mostra tutti i processi del sistema con dettagli completi: utente, proprietario, utilizzo percentuale di CPU e memoria
    ps -ef

top #mostra i processi in esecuzione con aggiornamenti continui in tempo reale (Gestione Attività di Windows)

#AGGIUNGENDO & ALLA FINE DI UN COMANDO ESEGUIAMO IN BACKGROUND L'ESECUTIVO

jobs #mostra tutti i processi in background e quelli sospesi che sono stati lanciati dalla shell corrente

fg %numero_job #porta in primo piano dei programmi eseguiti 

bg #riavviare un processo stavolta in background

kill PID #specificando il PID (kill PID) termina il processo con il relativo PID
#esempio:
#abbiamo startato un processo e non possiamo fermarlo
# ps aux --- troviamo il pid del processo e facciamo
#kill PID

pkill nome_processo #termina processi cercando per nome 

killall nome_processo #termina tutti i processi che corrispondono esattamente al nome specificato.

nohup comando & #esegue un processo rendendolo immune alla chiusura della shell. Il processo continuerà anche dopo il logout

disown %job_number #scollega un job già avviato dalla shell corrente
----------------------------------------------------------------------------

COME IMPOSTARE ALIAS PER IL TERMINALE

#vedere i file di configurazione della bash

cd ~/.bashrc #in .bashrc sono contenuti i file di configurazione della bash

#aggiungere alla fine del file alias come

alias ll='ls -l'

#Questo alias "creerà" il comando ll che avrà la stessa funzione di ls -l
#Quindi per creare un alias la sintassi è

alias nome_nuovo_alias='comando con relative flag da sostituire'
alias  #fa vedere che alias siano attivi

----------------------------------------------------------------------------

COMANDI AGGIORNAMENTO DEL SISTEMA

sudo apt update #scarica le informazioni più recenti sui pacchetti disponibili dai repository configurati ma non installa nulla

sudo apt upgrade #installa le versioni più recenti di tutti i pacchetti già presenti sul sistema

sudo apt install nome_pacchetto #installa un nuovo software. APT scarica automaticamente il pacchetto richiesto insieme a tutte le sue dipendenze dai repository configurati

sudo apt remove nome_pacchetto #rimuove il pacchetto specificato ma mantiene i file di configurazione per un eventuale reinstallazione futura

sudo apt purge nome_pacchetto #elimina completamente il pacchetto includendo tutti i file di configurazione associati

sudo apt autoremove #rimuove automaticamente i pacchetti installati come dipendenze che non sono più richiesti da alcun programma attivo

apt search parola_chiave #cerca nei repository Debian/Ubuntu tutti i pacchetti che contengono la parola chiave nel nome o nella descrizione

apt show nome_pacchetto #visualizza la descrizione completa, versione, dimensione, dipendenze e homepage del progetto

sudo apt install --only upgrade nome_pacchetto #questo comando aggiorna solamente il pacchetto specificato senza toccare gli altri programmi installati.

----------------------------------------------------------------------------

PERMESSI DI CONTROLLO:

#vengono rappresentati attraverso una stringa di 10 caratteri, esempio:
#drwxrwxrwx
    "Reading, Writing and Executing"

    #rwx: tutti i permessi
    #rw-: leggere e scrivere ma non eseguire
    #r-x: leggere ed eseguire ma non scrivere

'''Questa è divisa in 4 parti:
    -il primo carattere ci fa capire se stiamo guardando un file (-) o una directory (d)
    -il primo set da 3 rappresenta i permessi del creatore,
    -il secondo set da 3 rappresenta i permessi del gruppo, in una sistema unix i file e le directory sono assegnati a gruppi
    -il terzo set da 3 rappresenta i permessi degli "altri"
'''
sudo #parola chiave che permette di eseguire un comando come superuser, sudo = superuser do,praticamente come amministratore

chmod #comando che permette di cambiare i permessi di un file o di una directory
        #Esempio: 
        chmod -r u=rwx,g=,o= NOME_DIRECTORY/FILE
                    #u: user "owner" imposta i permessi per il creatore
                    #g: group imposta i permessi per il gruppo
                    #o: others, imposta i permessi per gli altri
            
        #con la flag -x possiamo rimuovere i permessi di essere eseguito al file
        #Esempio: 
        chmod u-x prova.txt

	#Si puà anche esprimere con dei numeri (oct)
	# r = 4
	# w = 2
	# x = 1
	#Esempio:
	#owner: legge, scrive ed esegue (4 + 2 +1 = 7)
	#group: legge ed esegue
	#other; legge ed esegue
	chmod 755 script.sh 
	
	
#RICORDARSI CHE PER CAMBIARE I PERMESSI E SPOSTARE FILE LA CARTELLA IN CUI STIAMO CAMBIANDO/SPOSTANDO PERMESSI E FILE NON DEVE ESSERE LA NOSTRA WORKING DIRECTORY

#L'user root è un amministratore, ha accesso a tutto nel sistema e può fare tutto, quando usiamo sudo agiamo come se fossimo la root

chown #"change owner" permette di cambiare il proprietario del file o della directory, e ha bisogno dei permessi di root
	#Esempio: 
	sudo chown -R root contacts
	
    #sudo: esegue il comando come root
    #chown: cambia il proprietario
    #-R: recursive, cambia anche per le sottocartelle e tutto quello che vi è all' interno
    #root: il nome del nuovo proprietario
    #contacts: la directory a cui vogliamo cambiare il proprietario
----------------------------------------------------------------------------

FILE ESEGUIBILI

#File che finiscono con .sh sono script della shell e possono essere eseguiti con

mydir/program.sh

#Se invece siamo già nella cartella in cui si trova il file eseguibile dovremo fare

./program.sh

----------------------------------------------------------------------------

DIFFERENZA TRA PROGRAMMI COMPILATI E PRORAMMI INTERPRETATI

#I PROGRAMMI COMPILATI COME I FILE IN C, SONO PROGRAHMI CHE PER ESSERE ESEGUITI VENGONO PRIMA TRASFORMATI IN CODICE BINARIO, QUINDI SONO ANCHE PIU' VELOCI SULLA MACCHINA 

#I PROGRAMMI INTERPRETATI, COME I FILE DI PYTHON, PER ESSERE ESEGUITI VENGONO INTERPRETATI DA UN INTERPRETE MENTRE VENGONO ESEGUITI CHE POI LI TRASFORMA IN CODICE BINARIO CHE LA MACCHINA PUÒ CAPIRE

which #comando che permette di trovare dove sono localizzati determinati tipi di file 
    #Esempio: which sh which py

#! interpreter (Shebang) = linea di codice speciale che dice al terminale che programma usare per eseguire 1l f1le, usato per file interpretati, per file compilati non serve 
    ESEMPIO: #!/usr/bin/pythonn3 ------> questo servirà per eseguire un file python attraverso l'interprete di pythor 

----------------------------------------------------------------------------

TIPI DI SHELL

#1. sh: La shell Bourne, la shell originale del sistema Unix ed è POSIX-compliant, molto basica e non ha molte funzion: sulla qualità di vita

#2, bash: La "Bourne Again s shell, è la shell più popolare su Linux, è costruita sulle basi di sh ma ha anche moolte altre funzioni extra

#3. zsh: E' la shell più popolare sui sistemi Mac0s, come bash fa le stesse cose di sh ma con delle migliorie

#ENTRAMBE le shell bash e zsh sono "sh-compatible" quindi vuol dire che possono eseguire script .sh ma hanno anche molte altre funzionni che le rendono più piacevoli e utili da usare.

#Sia Bash che Zsh dispongono di file di configurazione che vengono eseguiti automaticamente ogni volta che si avvia una nuova sessione di shell. Questi file vengono utilizzati per impostare alias, funzioni e variabili d'ambiente

#Questi file si trovano nella directory home (~) e sono nascosti per impostazione predefinita ls ha una flag -a che mostra i file nascosti

----------------------------------------------------------------------------

VARIABILI DI AMBIENTE E PATH

#Sono variabili a disposizione di tutti i programmi che vengono eseguiti nella shell

#Per inizializzare una variabiile d'ambiente usiamo il comando:

EXPORT
	Esempio:   
		export NAME="Lane" 
		#(solitamente le variabili d'ambiente vengono scritte in CAPS)

#UNA DELLE VARIABILI D'AMBIENTE PIU' IMPORTANTE E' IL PATH

#Nel Path sono listate le directory in cui sono conservati i comandi principali della shell come ls, cd, ecc..

#Esempio di PATH:
	echo $PATH #printa il contenuto di PATH:
	
#/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/local/sbin:/usr/sbin:/sbin:/home/manuel/worldbanc/private/bin

#Tutte le directory sono divise da :

#Quando installiamo dei nuovi programmi sulla macchina molto probabilmente il percoso di questi non sarà presente nel PATH e quindi ci darà degli errori come:

#$ my-new-program="
#-bash: my-new-program: command not found

#Quindi per farli funzionare dovremo metterli nel PATH
#Per farlo importiamo nella variabile d'ambiente PATH, che esiste di predefinito, la directory assoluta (si ottiene con pwd)

#Esempio:
	export PATH="$PATH:/home/manuel/worldbanc/private/bin"

#QUESTO PERO' VARRA' SOLO PER LA SHELL ATTUALE, SE LA CHIUDI VERRA' RESETTATO
#PER RENDERLO PERMANENTE METTIAMO NEL FILE DI CONFIGURAZIONE IL COMANDO CHE ABBIAMO USATO PRIMA PER INSERIRE LA DIRECTORY NEL PATH

sudo nano .bashrc

#Alla fine del file aggiungiamo:
export PATH="$PATH:/home/manuel/worldbanc/private/bin"

----------------------------------------------------------------------------
REINDIRIZZAMENTO DI STRINGHE

#Possiamo ridirezionare delle stringhe per essere salvate in altri file con >

#Reindirizzamento di "standard output" (stdout) ad un file   >
echo "Hello World" > Hello.txt 
#metterà Hello World nel file Hello.txt


#Reidirizzamento di "standard error" (stderr) ad un file     2>
cat doesnotexist.txt 2> error.txt 
#Visto che il file doesnotexist.txt appunto non esiste, il suo errore viene salvato in un file chiamato error.txt CHE INVECE ESISTE


#ESEMPIO PRATICO:
#Abbiamo uno script che legge file csv, printa in standard output le transazioni dall' anno 2000 in poi
#Mentre le transazioni prima degli anni 2000 in standard output.

#Vogliamo stampare le transazioni di standard output (quelle che sono conformi al parametro dell' anno) a schermo mentre quelle in standard error (quelle che sono prima degli anni 2000) in un file di log

process_transactions.sh worldbanc/private/transactions/2020.csv 2> /tmp/worldbanc.log

#Con questo comando usiamo lo script che legge e stampa le transazioni E QUELLE CHE NON RISPETTANO IL FILTRO (QUINDI SONO IN STANDARD ERROR) IN UN FILE DI LOG ATTRAVERSO 2> che direziona SOLO gli standard error al file nella directory specificata


#Reinderizzamento standard input (stdin)
#Posto di default in cui i programmi leggono l'input
#Dalla bash in uno script usa il comando:

read

#Piping
#Permette di passare l'output di un comando/programma in input ad un altro comando/programma in modo da automatizzare funzioni

| = simbolo di pipe
#esempio:

echo "Ciao mi chiamo Manuel" | wc -w

#Il testo che viene printato con echo viene reinderizzato in input al comando wc che attraverso la flag -w conra quante parole (words) ci sono all'interno di quello che gli abbiamo passato (4).

#ESEMPIO PRATICO:
#Vogliamo vedere il numero di transazioni di un nostro cliente nella directory che contiene tutte le transazioni dei nostro clienti senza però le transazioni salvate nella cartella backup all' interno di transazioni

grep -R worldbanc/private/transaction --exclude-dir="backups" | wc -l
#	-R cerca in modo ricorsivo in tutti i file della cartella e dei file all'interno delle cartelle della nostra attuale directory
#   --exclude-dir= ci permette di lasciar stare una directory all'interno in cui stiamo cercando, in questo caso backups


```
----------------------------------------------------------------------


