
```
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
  #rimuove un file dalla Staging Area   
  
- git rm "nome-file"
  #Cancella il file dalla repository 
  #Se si vuole cancellarlo definitivamente bisogna fare un    git commit successivamente
  
- git restore "nome-file"
  #Permette di recuperare il file cancellato, affinchè non sia stato già fatto il commit
  
- git commit -m "Messaggio descrittivo" 
  #Scatta l'istantanea definitiva. Il messaggio (-m) spiega cosa hai cambiato (es: "Riparato bug nel login").
  #con --amend sovrascrivi il commit precedente
  
- git mv "Nome-file-vecchio" "Nome-file-nuovo"
  s
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
  
- git diff
  #mostra riga per riga cosa è cambiato nel file rispetto all' ultimo salvataggio
  
---------------------------------------------------------------

#6
#Rami e Sperimentazione (
Branching)

- git branch nome-ramo
  #crea un ramo parallelo per testare una nuova funzione senza toccare il codice principale
- git checkout nome-ramo
  #ti sposta da un ramo all'altro
- git merge nome-ramo
  #Unisce le modifiche del ramo secondario a quello principale (main)
```