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

>[!NOTE]

>[!NOTE]







>Questa funzione serve a stampare a schermo quello dentro EOF

``` Shell
usage() {
	cat <<EOF
Uso: $0 INPUT OUTPUT 

INPUT File sorgente
OUTPUT File di destinazione
EOF
}
