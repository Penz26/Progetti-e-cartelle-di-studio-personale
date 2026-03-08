#Git [[Git & GitHub]]
I file .gitignore sono file molto importanti che permettono di far si che certi file vengano ignorati, in modo che non vengano caricati su GitHub e non tenga traccia delle sue modifiche.

Senza questi file, si finirebbe per caricare online dati spazzatura e peggio dati sensibili.

# 4 principali file da mettere nel gitignore

### 1. File di sistema e temporanei

Ogni sistema operativo crea file invisibili per gestire le cartelle. Non hanno nulla a che fare con il tuo codice e infastidiscono i colleghi che usano sistemi diversi.

- **Windows:** `Thumbs.db`, `desktop.ini`
    
- **macOS:** `.DS_Store`
    

### 2. Dati Sensibili (I più pericolosi!) 🛡️

Non vuoi mai che le tue password o le chiavi di accesso al database finiscano su GitHub (che è pubblico!).

- **Esempio:** file `.env`, `config.json` con password, chiavi API private.
    

### 3. Cartelle delle dipendenze (Troppo pesanti) 📦

I progetti moderni usano librerie esterne che possono pesare centinaia di MB. Non serve caricarle su GitHub perché possono essere scaricate in un secondo momento con un comando.

- **Node.js:** `node_modules/`
    
- **Python:** `venv/` (ambienti virtuali)
    

### 4. File generati automaticamente (Output)

Git deve tracciare il **codice sorgente**, non i risultati della compilazione o i log.

- **Esempio:** file `.exe`, `.log`, cartelle `dist/` o `build/`, file PDF generati da LaTeX.



# Come si creano questi file .gitignore

1. Si va nella cartella che si ha iniziallizato su git con **git init** 
2. Si crea un nuovo file di testo di cui cambieremo il nome in .gitignore e il tipo di file **DEVE ESSERE TOLTO** 
3. Dopo aver fatto ciò si entra a scrivere all'interno del file con un proprio editor di testo preferito e si inizia a dare le misure di filtraggio

Esempio:

ignore all .txt files
*.txt (c'è davanti l'asterisco per simboleggiare  TUTTI i file txt)