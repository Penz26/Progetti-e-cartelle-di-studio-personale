#Git  #GitHub [[Git & GitHub]]
# Metodo HTTPs
```Shell
- git remote add origin URLREPOGITHUB.git
  
  #Dice al computer dove si trova la cartella online
  #origin è il nome che diamo a GitHub, si può chiamare come si vuole ma per convention si usa origin
  
  #Per verificare: 
  git remote -v
  
  #Ora dobbiamo aggiungere i file alla staging area per committarli e poi pusharli sulla repo di GitHub
  
  git add .
  git commit -m "Messaggio" #salva localmente
  
- git push -u origin main
  
  #Pusha quello committao su GitHub
  #la flag -u (--set-upstream) si utilizza per la prima volta che si pusha così da collegare d'ora in poi questo ramo locale a quello remoto
  #origin si riferisce alla destinazione
  #main è il branch che si sta inviando
  
  #dopo la prima volta si può anche evitare di mettere origin e main quindi fare solo git push

 - git pull
   #scarica eventuali modifiche fatte da altri su GitHub. (Sempre meglio farlo quando si ha una repo condivisa)
```

# Metodo SSH
```shell
#Inizializzare in locale la repository
#Fare il primo commit
git init 
git add .
git commit -m "First Commit"

#Cambiare il nome del branch principale in main (segue standard GitHub)
git branch -M main

#ANDARE SU GITHUB CREARE NUOVA REPOSITORY
#LASCIARE DESELEZIONATO IL README.md ED IL .gitignore
#Selezionare visibilità repo
git remote add origin git@github.com:UTENTE/NOME-REPOSITORY.git

#Effettuare il primo push
git push -u origin main
```

---
## **Togliere la richiesta di login a Github per ogni push via ssh da Linux**

>Dobbiamo modificare l'url di origine della nostra repo con:
```shell
git remote set-url origin git@github.com:username_github/repo_progetto.git

#Controllare con
git remote -v
```