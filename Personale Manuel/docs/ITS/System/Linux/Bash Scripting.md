#Bash #Linux 

# **Cos'è uno Script bash?**
>Uno script bash è un file di testo contenente una sequenza di comandi Linux che vengono eseguiti  automaticamente dalla shell bash.
>E' il modo più naturale per automatizzare operazioni e creare strumenti amministrativi personalizzati

### Quando Utilizzarlo?
> - Automatizzare task ripetitivi e noiosi
> - Eseguire sequenze complesse di comandi e sistema
> - Creare strumenti di amministrazione personalizzati
> - Implementare procedure di backup e manutenzione
> - Orchestrare operazioni su più server

### Vantaggi Principali
> **- Semplicità:** facile da scrivere e leggere
> **- Immediatezza:** nessuna compilazione necessaria
> **- Potenza:** Accesso completo ai comandi di sistema
> **- Portabilità:** funziona su tutti i sistemi Unix-like


### Limitazioni
>Prestazioni inferiori rispetto a linguaggi compilati. Non ideale per logica computazione complessa

---
# **Step principali di uno script in Bash**
>Ci sono 4 stadi principali per creare uno script in Bash:

1. Creazione del File:
```Bash
nano mio_script.sh
```

2. Scrivere il Contenuto
```Bash
#!/usr/bin/env bash
echo "Ciao mondo"
```

>[!NOTE] Lo Shebang (#!/usr/bin/env bash) indica al sistema quale interprete utilizzare per eseguire i file. Senza questa riga il sistema non saprà come processare lo script

3. Rendere eseguibile
```Bash
chmod +x mio_script.sh   
```

4. Eseguire lo script
```Bash
./mio_script.sh
```

---
# **Variabili**

### Dichiarazione e Assegnazione
```Bash
nome="Manu"
eta=30
percorso="/var/www/html"

echo "Il mio nome è $nome"
echo "Ho $eta anni"
echo "Il path è $percorso"
```

>Output:
```Bash
Il mio nome è Manu
Ho 30 anni
Il path è /var/www/html
```

### Convenzioni e Best Practice

- Costanti Globali
>Usare MAIUSCOLE PER VALORI CHE NON CAMBIANO
```Bash
BACKUP_DIR="/backups"
MAX_RETRY=3
```
- Variabili Locali
>Usare minuscole per variabili temporanee
```Bash
nome="Valore"
contatore=0  
```
- Regole Fondamentali
>Mai spazi intorno a =
>Prefisso $ per leggere il valore
>Quote per stringhe con spazi

---
# **Parametri**
>Gli script bash possono accettare parametri dalla linea di comando, rendendoli estremamente versatili.
>Bash fornisce variabili speciali per accedere a questi parametri

### Esempio:
```Bash
#!/bin/bash
echo "Numero argomenti: $#"
echo "Nome script: $0"
echo "Primo parametro: $1"
echo "Secondo parametro: $2"
echo "Tutti i parametri: $@"
```

>Output:
```Bash
Numero argomenti: 3
Nome script: ./script.sh
Primo parametro: uno
Secondo parametro: due
Tutti i parametri: uno due tre
```

### Variabili Speciali:
- $0 - Nome dello script
- $1, $2, ... - Parametri posizionali
- $# - Numero totale di parametri
- $@ - Tutti i parametri come lista
- $? - Codice di uscita del comando precedente
- $ $ - PID (Process ID) dello script corrente 

---
# **Operatori Aritmetici***

### Operazioni Base
```Bash
a=10
b=3
echo $((a + b)) # Somma: 13
echo $((a - b)) # Sottrazione: 7
echo $((a * b)) # Moltiplicazione: 30
echo $((a / b)) # Divisione: 3
echo $((a % b)) # Modulo (resto): 1
echo $((a ** 2)) # Potenza: 100
```

### Incrementi e Decrementi
```Bash
((a++)) # Incrementa a di 1
((a--)) # Decrementa a di 1
((a+=5)) # Aggiunge 5 a a
((a*=2)) # Moltiplica a per 2
((a-=3)) # Sottrae 3 da a
((a/=2)) # Divide a per 2
```

### Sintassi Avanzata
```Bash
risultato=$((a * b + 5))
somma=$(( (a + b) * 2 ))
# Usare (( )) per aritmetica
# No spazi tra parentesi
# Supporto espressioni complesse
```
>[!IMPORTANT] Bash esegue solo aritmetica intera. Per calcoli con decimali, utilizzare strumenti esterni come bc o awk

---
# Operatori di Confronto

### Confronto Numerico
```Bash
a=10
b=20
[ $a -eq $b ] # uguale
[ $a -ne $b ] # diverso
[ $a -lt $b ] # minore
[ $a -le $b ] # minore uguale
[ $a -gt $b ] # maggiore
[ $a -ge $b ] # maggiore uguale
```

### Confronto Stringhe
```Bash
str1="hello"
str2="world"
[ "$str1" = "$str2" ] # uguale
[ "$str1" != "$str2" ] # diverso
[ -z "$str" ] # vuota
[ -n "$str" ] # non vuota
```

### Test su File
```Bash
file="/etc/passwd"
dir="/home"
[ -f "$file" ] # è un file
[ -d "$dir" ] # è directory
[ -r "$file" ] # leggibile
[ -w "$file" ] # scrivibile
[ -x "$file" ] # eseguibile
[ -e "$file" ] # esiste
```

---
# **Condizionale: if-then-else**

### Struttura Base
```Bash
#!/bin/bash
eta=$1
if [ $eta -ge 18 ]; then
	echo "Sei maggiorenne"
else
	echo "Sei minorenne"
fi
```

### Esempi di Esecuzione
```Bash
./script.sh 25
# Output: Sei maggiorenne
./script.sh 15
# Output: Sei minorenne
```

### If-Elif-Else Multipli
```Bash

Struttura Base
Esempi di Esecuzione
#!/bin/bash
voto=$1
if [ $voto -ge 90 ]; then
	echo "Eccellente"
elif [ $voto -ge 80 ]; then
	echo "Buono"
elif [ $voto -ge 70 ]; then
	echo "Sufficiente"
elif [ $voto -ge 60 ]; then
	echo "Appena sufficiente"
else
	echo "Insufficiente"
fi
```

---
# Operatori Logici

### AND (&&) - Entrambe Vere
>Entrambe le condizioni devono essere soddisfatte
```Bash
if [ $eta -ge 18 ] && [ -f "$documento" ]; then
	echo "Puoi votare, hai documento valido"
fi
```

### OR ( | | ) - Almeno Una Vera
>Basta che una delle condizioni sia soddisfatta
```Bash
if [ "$EUID" -eq 0 ] || [ "$UID" -eq 0 ]; then
	echo "Sei root o hai privilegi elevati"
fi
```

### NOT (!) - Negazione
>Inverte i risultati di una condizione
```Bash
if [ ! -f "$file" ]; then
	echo "File non esiste"
	touch "$file"
fi
```

### Combinazioni Complesse
>Usare parentesi per raggruppare condizioni
```Bash
if [ -f "$file" ] && ([ -r "$file" ] || [ -w "$file" ]); then
	echo "File esiste ed è leggibile o scrivibile"
fi
```

---
# **Ciclo For**

### Lista di Elementi
```Bash
#!/bin/bash
for frutto in mela banana arancia; do
	echo "Mi piace: $frutto"
done
```

>Output:
```Bash
Mi piace: mela
Mi piace: banana
Mi piace: arancia
```

### Parametri Script
```Bash
#!/bin/bash
for parametro in $@; do
	echo "Parametro: $parametro"
done
```

>Esecuzione e Output
```Bash
./script.sh uno due tre

Parametro: uno
Parametro: due
Parametro: tre
```

### Sequenza Numerica
```Bash
#!/bin/bash
for ((i=1; i<=5; i++)); do
	echo "Numero: $i"
done
```

>Output:
```Bash
Numero: 1
Numero: 2
Numero: 3
Numero: 4
Numero: 5
```

### Iterare su File e Directory
```Bash
for file in /var/log/*.log; do
	echo "Elaborando: $file"
	wc -l "$file"
done
```

---
#  **Ciclo While**

### Ciclo Condizionale Base
```Bash
#!/bin/bash
contatore=1
while [ $contatore -le 5 ]; do
	echo "Contatore: $contatore"
	((contatore++))
done
```

### Leggere File Riga per Riga
```Bash
#!/bin/bash
while IFS= read -r riga; do
	echo "Riga: $riga"
done < /etc/passwd
```
>[!NOTE] IFS (Internal Field Separator): Quando si legge da file, IFS= preserva gli spazi iniziali e finali. read -r disabilita l'interpretazione dei backslash

---
# **Switch Case**
>Da usare quando si devono confrontare valori discreti contro una singola variabile.
>Particolarmente utile per:
>- Menù di selezione
>- Script di gestione servizi
>- Parser di opzioni
>- Switch su tipi di file

### Pattern Matching:
- * - qualsiasi stringa
- ? - singolo carattere
- [...] - set di caratteri

### Esempio Completo:
```Bash
#!/bin/bash
opzione=$1
case $opzione in
start)
echo "Avviando servizio..."
systemctl start myservice
;;
stop)
echo "Fermando servizio..."
systemctl stop myservice
;;
restart)
echo "Riavviando servizio..."
systemctl restart myservice
;;
status)
echo "Stato servizio:"
systemctl status myservice
;;
*)
echo "Opzione non riconosciuta: $opzione"
echo "Uso: $0 {start|stop|restart|status}"
exit 1
;;
esac
```

---
# **Funzioni**
>Le funzioni permettono di suddividere script complessi in blocchi riutilizzabili, migliorando leggibilità e manutenzione del codice.

### Dichiarazione e Utilizzo Base
```Bash
#!/bin/bash
# Definizione funzione
saluta() {
echo "Ciao, $1!"
echo "Benvenuto nel sistema"
}
# Chiamate alla funzione
saluta "Marco"
saluta "Lucia"
```

>Output:
```Bash
Ciao, Marco!
Benvenuto nel sistema
Ciao, Lucia!
Benvenuto nel sistema
```

### Variabili Locali vs Globali
```Bash
#!/bin/bash
GLOBALE="Visibile ovunque"
funzione_esempio() {
	local var_locale="Visibile solo qui"
	var_globale="Accessibile all'esterno"
	echo "Dentro funzione: $var_locale"
}
echo "Fuori funzione: $var_globale"
# echo "$var_locale" # ERRORE: non definita
```
>[!NOTE] **Best Practice:** usare sempre local per variabili di funzioni per evitare conflitti e side-effects

### Funzioni con ritorno valore
```Bash
#!/bin/bash
addiziona() {
	local a=$1
	local b=$2
	local risultato=$((a + b))
	echo $risultato
}
# Catturare il risultato
somma=$(addiziona 10 20)
echo "Risultato: $somma"
```

---
# **Redirezioni e Pipe: Orchestrare il flusso dei Dati**

### Redirezione Output (stdout)
```Bash
echo "Testo nel file" > file.txt # Sovrascrive
echo "Aggiungi riga" >> file.txt # Appende
ls -la > lista_file.txt # Output in file
```

### Redirezione Errori (stderr)
```Bash
comando_errato 2> errori.log # Solo errori
comando 2>&1 output_completo.log # Output + errori
comando > output.log 2>&1 # Sintassi alternativa
```

### Pipe | - Concatenazione Comandi
```Bash
cat /var/log/syslog | grep "error" # Filtra righe
cat lista.txt | sort | uniq # Ordina e deduplica
ls -l | wc -l # Conta file
ps aux | grep apache | wc -l # Conta processi
```

### Combinazioni Avanzate
```Bash
#!/bin/bash
# Conta errori in log
errori=$(grep -c "ERROR" /var/log/apache2/error.log)
echo "Errori trovati: $errori"
# Salva processi Apache
ps aux | grep apache > processi_apache.txt
# Reindirizza tutto
./script.sh > output.log 2>&1 &
```