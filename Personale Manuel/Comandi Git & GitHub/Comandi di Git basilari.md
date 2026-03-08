#Git [[Git & GitHub]]

# Comando di aiuto
**git nome_comando --help**
```Shell
#1
#Preparazione (Setup) all'interno della GitBash, o qualsiasi terminale che si stia usando per Git

#Questi due comandi permettono di capire chi "FIRMA" i salvataggi

- git config --global user.name "Il tuo nome"
- git config --global user.email "la tua mai.com"
  
---------------------------------------------------------------

#2
#Iniziare un progetto

- git init #crea una nuova repository Git locale NELLA CARTELLA IN CUI TI TROVI

- git clone URL #scarica un progetto esistente da GitHub sul tuo computer
  
---------------------------------------------------------------

#3
#Il ciclo di lavoro quotidiano (Salvataggio)

#Questo è il flusso che ripeterai continuamente: Modifica → Aggiungi → Salva.

- git status 
  #Il comando più importante. Ti dice quali file hai modificato e cosa sta succedendo.
    
- git add [nome-file] 
  #Prepara il file per il salvataggio (lo mette nella "Staging Area").
    
    - Trucco: git add . aggiunge tutti i file modificati in una volta sola.
     
- git rm --cached nome_file
  #rimuove un file dalla Staging Area ma lo mantiene nella cartella locale
  #si usa quando si ha aggiunto un file alla repo che non dovrebbe esserci
  
- git rm "nome-file"
  #Cancella il file dalla repository 
  #Se si vuole cancellarlo definitivamente bisogna fare un    git commit successivamente
  
- git restore "nome-file"
  #Permette di recuperare il file cancellato, affinchè non sia stato già fatto il commit, recupera il file originale non modificato
	--staged #permette di spostare il file dalla staging area alla working directory senza perdere le modifiche 
	#si usa quando si ha inserito il file nella staging area quando non si aveva ancora finito di modificarlo
  
- git commit -m "Messaggio descrittivo" 
  #Scatta l'istantanea definitiva. Il messaggio (-m) spiega cosa hai cambiato (es: "Riparato bug nel login").
  --amend #con --amend dopo il messaggio sovrascrivi il commit precedente
  -a #permette di skippare completamente la staging area committando direttamente
  
- git mv "Nome-file-vecchio" "Nome-file-nuovo"
  #cambiare nome file
  
--------------------------------------------------------------   
#4
#Sincronizzazione con GitHub
#Una volta salvato sul PC, devi inviare i dati online

- git push origin main
  #invia i tuoi salvataggi (commit) dal computer locale a GitHub

- git pull
  #scarica le ultime modifiche fatte dai tuoi colleghi da GitHub al tuo PC
  
---------------------------------------------------------------

#5
#Esplorare la Cronologia (Beccare chi fa cagate)

- git log
  #mostra la lista di tutti i commit fatti in passato (chi, quando e cosa)
  # con -p vediamo la storia dei commit e anche cosa hanno fatto
  --oneline #permette di vedere solo l'ultimo commit
  
- git diff
  #mostra riga per riga cosa è cambiato nel file rispetto all' ultimo salvataggio
  
---------------------------------------------------------------

#6
#Rami e Sperimentazione (
Branching)

Un branch è una copia del tuo main branch, ha le stesse entrate di commit nella history ma permette di lavorare ad altre cose (feature, bug fix, modifiche, ecc...) senza che il main branch venga alterato.

Una volta finiti i lavori sul branch secondario, si può fare il merge dei due branch così da integrare tutto in uno solo.

- git branch nome-ramo
  #crea un ramo parallelo per testare una nuova funzione senza toccare il codice principale
- git checkout nome-ramo
  #ti sposta da un ramo all'altro
- git merge nome-ramo
  #Unisce le modifiche del ramo secondario a quello principale (main)
  
--------------------------------------------------------------------------

#7
#Comandi utili / salvaculo

- git reset codice_del_commit (si vede con git log i numeri affianco)
  #permette di tornare al salvataggio di commit precedenti
- git rebase -i --root 
  #permette di modificare cosa appare nella history dei commit, l'ordine con cui appaiono i commit, possono essere uniti (merged) più commit e renderli un unico commit nuovo
  #come si fa:
  #si manda il comando git rebase -i --root è darà un'immagine come questa:

```

![[immagine_rebase.png | 1200]]

```Shell
#Una volta al suo interno mettiamo al posto di pick squash (oppure s per abbreviare) salviamo il file, chiudiamo l'editor e tornando nella shell ci verrà chiesto il nuovo messaggio per il nuovo commit unito.

```