#Linux 
>Lungo questo appunti partireo da uno script minimale e lo arrichiremo passo dopo passo, introducendo ogni volta una best practice concreta, spiegata e immediatamente applicabile.

>Il risultato finale sarà un **template standard riutilizzabile** come punto di partenza per automazioni, task di sistema e utility interne.

## 1. Script per copiare un file sorgente in una destinazione

>1.1. Versione fragile e incompleta
```Bash
#!/bin/bash
cp $1 $2
```
>In questa versione se mancano argomenti, se i percorsi contengono spazi, o se il file sorgente non esiste, il comportamento sarà imprevedibile o direttamente sbagliato. 

- **Ecco i problemi concreti che sono da risolvere in questo script:**
  1. **Nessuna validazione dei parametri**
     >Lo script non verifica quanti argomenti riceve, nè se sono del tipo corretto.
  2. **Nessuna gestione degli errori**
     >File inesistenti, percorsi con spazi e permessi mancanti vengono ignorati silenziosamente
  3. **Nessun help o messaggi chiari**
     >L'utente non sa come usare lo script nè cosa è andato storto in caso di fallimento
  4. **Nessun supporto per flag e opzioni**
     >Non è previsto alcun meccanismo per opzioni come -h, -v o -f.
     

# **Best Practice #1**
>**Shebang Corretto e Portabile**


>La forma consigliata è /usr/bin/env bash, perchè cerca Bash nel PATH ed è più portabile rispetto a un path hardcoded come /bin/bash.

>Questa scelta rende lo script robusto su ambienti diversi: macOS, Ubuntu, Alpine, NixOS e qualsiasi distribuzione con Bash installato in un percorso non standard.

```Bash
#!/urs/bin/env bash
cp $1 $2
```
>[!IMPORTANT] Portabilità 
>Funziona su macOS, Linux e ambienti con Bash in posizioni non standard.

>[!IMPORTANT] Riutilizzabile
>Meno dipendenze dalla specifica dalla specifica distribuzione o piattaforma

# **Best Practice #2**
>Fail Fast con set -euo pipefail


>Una delle pratiche più diffuse in Bash è attivare set -euo pipefail all'inizio dello script per intercettare errori prima che si propaghino causando comportamenti imprevedibili.

```Bash
#!/usr/bin/env bash
set -euo pipefail
cp $1 $2
```

>[!NOTE] -e
>Termina lo scipt se un qualsiasi comando fallisce (exit code diverso da 0).

>[!NOTE] -u 
>Segnala l'uso di variabili non definite, intercettando typo e variabili dimenticate

>[!NOTE] -o
>Introduce l'opzione pipefail

>[!NOTE] pipefail
>Fa fallire l'intera pipeline se fallisce un comando interno, non solo l'ultimo

# **Best Practice #3**
>Quotare sempre le variabili

>In bash, quasi sempre le variabili vanno racchiuse tra doppi apici. Questo evita problemi con spazi, wildcard e word splitting, che sono tra le cause più frequenti di bug sileziosi.

```Bash
#!/usr/bin/env bash
set -euo pipefail
cp "$1" "$2"
```

>Senza quoting un path come /temp/file con spazi.txt viene interpretato come tre argomenti separati. Questo causa errori oscuri difficili da diagnosticare.

# **Best Practice #4**
>Verificare il numero dei Parametri

>Prima di eseguire la logica principale, lo script deve verificare che l'utente abbia passato i parametri attesi. Questo migliora sia l'usabilità che la robustezza $# rappresenta il numero di argomenti ricevuti dallo script.

```Bash
#!usr/bin/env bash
set -euo pipefail

if [[$# -ne 2]]; then
	echo "Uso: $0 INPUT OUTPUT" >&2
	exit 1
fi

cp "$1" "$2"
```
>[!NOTE]  **Interrompi subito**
>Se i parametri non sono corretti, non eseguire mai la logica principale. Meglio fallire presto e in modo chiaro.

>[!IMPORTANT] Scrivi su stderr
>I messaggi di errore vanno su stderr con >&2, non su stdout. Questo rispetta le convenzioni Unix e facilita il piping.


# **Best Practice #5**
>Separare la Logica dall' Help

>Invece di stampare messaggi inline separati nello script, conviene una funzione usage() dedicata. Questo rende il codice più pulito, facilita la manutenzione e garantisce coerenza tra tutti i punti in cui l'help viene mostrato.

```Bash
Usage(){
cat <<'EOF'

Uso:
	nome_script [OPZIONI] [ARGOMENTI]

Opzioni corte:
	-h    Mostra questo help
	-v    Verbose
	ecc..
	
Esempi:
	ecc...
	
EOF
}
```

>[!NOTE] **Riuso**
>La stessa funzione viene chiamata per errori di utilizzo che per l'opzione -h.

>[!NOTE] **Manutentibilità**
>Modificare il testo dell' help richiede un solo intervento, in un punto del codice

>[!NOTE] **Leggibilità**
>Il codice della logica principale rimane pulito e non intasato da testo di supporto


# **Best Practice #6**
>Help Inline e Uscita Corretta

>Uno script usabile dovrebbe supportare una modalità help esplicita con -h. L'help non è solo una comodità: è parte dell'interfaccia dello script.

### **Exit 0**
>Se l'utente chiede l'help l'exit code deve essere 0
>**exit code 0**

### **Exit 1**
>Se l'help deve essere mostrato per un errore, l'exit code deve essere 1, affinchè gli script chiamanti lo rilevino


## **Verificare che l'input Esista davvero***
>Non basta controllare il numero di parametri: bisogna anche validare ciò che i parametri rappresentano. Nel nostro caso, il file sorgente deve effettivamente esistere prima di tentare la copia.

>La validazione preventiva riduce gli errori ambigui e rende lo script molto più affidabile in produzione.
```Bash
[[ -f "$1" ]] || {
	echo "Errore: file sorgente non trovato: $1" >&2
exit 1
}
```

>**Principio generale:**
- File e directory
  Esistenza, tipo e permessi di lettura/scrittura
- Valori ammessi
  Range numerici, formati attesi, liste di valori validi
- Comandi esterni
  Presenza nel sistema prima di invocarli 



>Questa funzione serve a stampare a schermo quello dentro EOF

``` Shell
usage() {
	cat <<EOF
Uso: $0 INPUT OUTPUT 

INPUT File sorgente
OUTPUT File di destinazione
EOF
}
