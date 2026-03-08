# **Cosa Sono** ?

#Git 

Git è un software per il controllo di versione locale utilizzabile da interfaccia a riga di comando.

*Come funziona?*

Invece di salvare il file come prova_sito_finale.html, git scatta delle "istantanee" chiamate **commit** 

Se si fa un macello con il codice e questo smette di funzionare si può tornare a una versione funzionante precedente in pochi secondi.

Permette anche di creare "branch" paralleli per testare nuove idee senza rovinare la versione principale


## Ci sono 3 principali aree in Git
- **Working Directory**
   - Mentre si lavora su dei file (modifica, correzione errori, migliorie ecc...) si è in questa cartella.
- **Staging Area**
   - "Sala di attesa" prima di aggiungere i file alla history della repo, è come dire "Voglio che questi file facciano parte del prossimo salvataggio"
   - Per aggiungere file all'area di staging usiamo il comando                                                          *git add nome_file*
   - per rimuoverli invece dalla staging area se invece ci abbiamo ripensato e dobbiamo ancora modificare qualcosa usiamo il comando                                                                                        *git restore --staged nome_file*
   
- **Repository**
   -  Aggiornamento del file ed iscrizione nella history della repo
   -  si fa facendo *git commit -m "Messaggio"*
   - si può fare anche con file non nello staging aggiungendo la flag -a prima di -m per il messaggio
   
   

#GitHub

GitHub è la piattaforma che ospita i tuoi progetti Git (chiamati repository).

Permette a migliaia di persone di lavorare sullo stesso progetto contemporaneamente senza sovrascrivere il lavoro altrui.

Se il tuo computer decide di morire il tuo codice è al sicuro sui server di GitHub

[[Comandi di Git basilari]]
[[Cos'è un file .gitignore]]
[[Comandi di Git per collegarsi a GitHub]]