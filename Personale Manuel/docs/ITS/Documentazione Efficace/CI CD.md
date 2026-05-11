#GitHub [[Git & GitHub]]
# **Il Problema**
>Con MkDocs creiamo la pagina della nostra documentazione, però non è online. Abbiamo il sito in locale.

>Con il comando mkdocs build il sistema crea una cartella site/ con i veri file HTML e CSS pronti per essere pubblicati

# **Soluzione**
>GitHub Pages con GitHub Actions

>Usiamo GitHub pages, un servizio che prende i file HTML dalla repository e li trasforma in un sito web pubblico.

![[github-page-setting.png]]

---

# **Automatizzazione**
>CI/CD

# **CI - Continuos Integration**
>Ogni volta che un programmatore aggiunge del codice (o un file MarkDown), un sistema automatico lo scarica e lo controlla per assicurarsi che non ci siano errori.

# **CD - Continuos Deployment**
>Se i controlli sono superati, il sistema prende quel codice e lo pubblica automaticamente su internet.

---

# **CI/CD GitHub**
>GitHub Actions

>GitHub ti mette a disposizione un computer vuoto chiamato runner in cui esegue la tua automazione CI/CD.

>Le GitHub Actions si articolano in 3 fasi:
![[github_actions.png]]

- **TRIGGER** 
  >Definisce quando accendersi, in base a che evento
- **ESECUZIONE**
  >Dice cosa fare
- **SPEGNIMENTO**
  >Pubblica il risultato e dice quando spegnersi
  
# **Definizione delle Actions**
>Per definire un action basta creare un fiile .yml dentro alle cartelle .github/workflows nella nostra repository GithHub.

>[!ATTENTION] La cartella .github/workflows DEVE essere a livello ROOT della directory.
>Stessa roba il mkdocs.yml, così che lui possa leggerlo direttamente.
>In quest'ultimo bisognerà anche specificare di conseguenza la directory di dove andare a cercare la documentation

>Il file YAML è strutturato in 4 livelli:
1. Workflow
   >E' l'intero processo automatizzato. Corrisponde al file .yml stesso
2. Job
   >Un workflow ha uno o più job (programmi). Ogni job gira su un computer diverso
3. Step
   >Dentro ad un job ci sono gli step (funzioni del programma), la lista delle azioni da fare.
4. Action / Run
   >run, esegue un comando da terminale (es. pip, ls, cd, ecc)
   >   uses, usa un comando preconfezionato scritto da altri (es. actions/checkout)
   

>**Esempio Action**
```yml
name: Il mio primo Workflow
on:
  push:
jobs:
  saluta_e_controlla:
    runs-on: ubuntu-latest
    steps:
     - name: Scarico il codice
       uses: actions/checkout@v4
       
     - name: Stampo un saluto
       run: echo "Ciao ITS, la GitHub Action funziona!"
       
     - name: Guarda cosa c'è nel server
       run: ls -la
```

---

# **Pubblicazione della nostra documentazione su GitHub**

>MkDocs build genera una documentazione statica in Html + Css, già pronta per essere pubblicata.

>Con MkDocs possiamo anche pubblicare direttamente su GitHub Pages usando il comando mkdocs gh-deploy

1. Genera il sito Statico
2. Carica su gh-pages
   >Creando automaticamente il branch gh-pages
   

>[!ATTENTION] Di norma le Action possono solo leggere il codice. Per pubblicare il sito dobbiamo dargli il permesso di scrivere i file nella repository.

>Per Farlo:
![[action-write-settings.jpg]]

>Esempio di deploy.yml
```yml
name: Deploy della Documentazione

on:
  push:
    branches:
     - main
       
permissions:
  contents: write
  
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
	  - name: Scarica il codice
		uses: actions/checkout@v4
	  - name: Installa Python
		uses: actions/setup-python@v5
		with:
		  python-version: 3.x
	  - name: Installa MkDocs e tema Material
		run: pip install mkdocs-material
	  - name: Compila e Pubblica
		run: mkdocs gh-deploy --force
```