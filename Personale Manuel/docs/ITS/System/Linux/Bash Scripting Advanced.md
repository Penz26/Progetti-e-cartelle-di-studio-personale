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

---
# **Best Practice #7**
>**Verificare che l'input Esista davvero***


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

---
# **Best Practice #8**
>Introdurre funzioni di supporto log() e die()

>Quando uno script cresce, conviene incapsulare i comportamenti ricorrenti in funzioni riutilizzabili. Le più utili fin dall'inizio sono log() per i messaggi operativi e die() per i fallimenti fatali

>La funzione log() centralizza tutti i messaggi operativi con un timestamp coerente. Ogni messaggio va su stderr, lasciando stdout libero per l'output effettivo dello script
```Shell
log(){
	printf '[%s]%s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >&2)
}
```

>La funzione die() centralizza il fallimento: stampa un messaggio di errore formattato e termina con codice 1.
>Sostituisce tanti echo >&2; exit 1 sparsi nel codice
```Shell
die(){
	log "ERRORE: $*"
	exit
}
```

---

# **Best Practice #9**
>Logging chiaro e Orientato all'operatività

>Uno script utile non dovrebbe limitarsi a fallire o riuscire: dovrebbe anche raccontare cosa sta facendo. Il logging è fondamentale per il troubleshooting, per i cron job e per le automazioni in ambienti di produzione.

1. Avvio dello script
```Shell
log "Avvio script $SCRIPT_NAME"   
```

2. Parametri ricevuti
```Shell
log "Sorgente: $src | Destinazione $dst"   
```

3. Validazioni superate
```Shell
log "File sorgente verificato"   
```

4. Operazione eseguita
```Shell
log "Copia completata con successo"   
```

---

# **Best Practice #10**
>Dare nomi espliciti ai Parametri

>Appena possibile, conviene assegnare i parametri posizionali a variabili con nomi descrittivi.
>Leggere src e dest è molto più chiaro di $1 e $2 in ogni riga della logica

❌Prima
```Shell
[[ -f "$1" ]] || die "Non trovato: $1"
cp "$1" "$2"
log "Copiato $1 in $2"
```

✅Dopo
```Shell
src="$1"
dst="$2"
[[ -f "$src" ]] || die "File sorgente non trovato: $src"
cp "$src" "$dst"
log "Copiato $src in $dst"
```

---

# **Best Pratice #11**
>Gestire le opzioni con getopts

>Quando uno script inizia ad avere flag come -h, -v o -f è meglio usare getopts.
>getopts è il modo standard POSIX in Bash per gestire opzioni brevi in modo robusto

```Shell
verbose=0
force=0
while getopts ":hvf" opt; do
	case "$opt" in
		h) 
			usage; exit 0 ;;
		v) 
			verbose=1 ;;
		f) 
			force=1 ;;
		:) 
			die "L'opzione -$OPTARG richiede un valore" ;;
		\?) 
			die "Opzione non valida: -$OPTARG" ;;
	esac
done
shift $((OPTIND - 1)
```

>[!NOTE] **Gestione errori integrata**
>:) e \?) coprono opzioni con valore mancante e flag sconosciute

>[!NOTE] **Pulizia finale**
>shif$((OPTIND - 1)) rimuove le opzioni già elaborate, lasciando solo gli argomenti reali.

---

# **Best Practice #12**
>Modalità Verbose e Force

>Le flag non servono solo a "fare scena": servono a esporre comportamento controllato e prevedibile.
>-v è utile per il debug e il troubleshooting
>-f consente la sovrascrittura esplicita della destinazione, rendendo l'azione intenzionale e non accidentale

```Shell
if [[ $verbose -eq 1 ]]; then
	set -x
fi

if [[ -e "$dst" && $force -ne 1 ]]; then
	die "Il file di destinazione esiste già. Usa -f per sovrascrivere."
fi
```

- -v -Verbose
  >Attiva set -x per tracciare ogni comando eseguito. Indispensabile durante il debug di script complessi.
- -f -Force
  >Permette di sovrascrivere un file di destinazione già esistente. Senza questo flag, lo script e conservativo per default: non sovrascrive mai silenziosamente
- -h -Help
  >Mostra l'help e termina con exit(). Disponibile in qualsiasi momento, anche senza altri argomenti
>		

---

# **Best Practice #13**
>Verificare le Dipendenze Esterne

>Se uno script usa comandi estermi come jq, curl, awk, sed o rsync, deve verificarne la presenza prima di iniziare. Questo evita fallimenti a metà esecuzione, che possono lasciare il sistema in uno stato inconsistente.

```Shell

require_cmd() {
	command -v "$1" >/dev/null 2>&1 \
	|| die "Comando mancante: $1"
}
```

>Come usarla
```Shell
# All'inizio dello script, dopo le funzioni:
require_cmd cp
require_cmd rsync
require_cmd jq
```

---
# **Best practice #14**
>Cleanup e trap

>Se lo script crea file temporanei o risorse intermedie, dovrebbe ripulire sempre, anche in caso di errore o interruzione con Ctrl+C. Per questo trap è uno strumento fondamentale in qualsiasi script robusto.

>Questo script elimina la directory temporanea in $tmpdir se trova un errore tra quelli in trap
```Bash
#!/bin/bash
set -e
tmpdir=/tmp/myscript
mkdir -p $tmpdir
cleanup(){
	echo "Pulizia per segnale $1 (codice $?): rimuovo $tmpdir"
	rm -rf $tmpdir
}
trap 'cleanup INT' INT    #quando si chiude il programma con Ctrl+c
trap 'cleanup ERR' ERR    #Scatta ogni volta che un comando all'interno dello script fallisce
trap 'cleanup TERM' TERM  #quando si chiude con un kill generico
trap 'cleanup EXIT' EXIT #EXIT quando muore naturalmente
echo "Test: sleep 20, Ctrl+c o kill $BASHPID"  #restituisce il pid dello script
sleep 20
echo "Fatto."
```
>Se si usa un kill -9 (SIGKILL) muore subito (e male) e non finisce nemmeno il codice, quindi non cancella nemmeno la directory temporanea (/tmp/myscript)

---

# **Best Practice #15**
>Linting, Sintassi e Debug

>Scrivere bene Bash non significa solo far girare lo script: significa anche verificarlo con strumenti dedicati. ShellCheck è uno standard de facto nella community per individuare errori comuni e migliorare la qualità del codice Bash in modo sistematico.

>**Validazione sintattica**
>Controlla la sintasi senza eseguire lo script.
```Shell
bash -n nome_script.sh
```

>**Tracciamento esecuzione**
>Stampa ogni comando prima di eseguirlo
```Shell
bash -x nome_script.sh
```

>**Analisi Statistica**
>Analizza approfonditamente lo script con suggerimenti su quoting, test, variabili e pattern pericolosi
```Shell
shellcheck script.sh
```

---
# **TEMPLATE BASH RIUTILIZZABILE**

```Shell
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_NAME="$(basename "$0")"

usage() {
	cat <&2; 
}

die() { 
	log "ERRORE: $*"; 
	exit 1; 
}

require_cmd() { 
	command -v "$1" >/dev/null 2>&1 || die "Comando mancante: $1"; 
}

cleanup() { : }

main() {
	local verbose=0 force=0
	while getopts ":hvf" opt; do
		case "$opt" in
			h) 
				usage; 
				exit 0 ;;
			v) 
				verbose=1 ;;
			f) 
				force=1 ;;
			:) 
				die "L'opzione -$OPTARG richiede un parametro" ;;
			\?) 
				die "Opzione non valida: -$OPTARG" ;;
		esac
	done
	shift $((OPTIND - 1))
	[[ $# -eq 2 ]] || { usage; exit 1; }
	local src="$1" dst="$2"
	[[ $verbose -eq 1 ]] && set -x
	[[ -f "$src" ]] || die "File sorgente non trovato: $src"
	[[ -e "$dst" && $force -ne 1 ]] && die "Output esistente: $dst (usa -f)"
	require_cmd cp
	log "Copia da $src a $dst"
	cp "$src" "$dst"
	log "Operazione completata"
}

trap cleanup EXIT
main "$@
```