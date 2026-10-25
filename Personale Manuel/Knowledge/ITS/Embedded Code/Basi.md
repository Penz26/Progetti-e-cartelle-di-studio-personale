#embedded

# **Struttura progetto**

1. **platformio.ini**: file di configurazione centrale (board, framework, velocità seriale)
2. **src/**: cartella destinata ad ospitare il codice sorgente C/C++
3. **lib/**: eventuali librerie esterne
---
## **Platformio.ini**

>*descrizione*

---

## **src**

>Lo scheletro di ogni singolo principale consiste in una struttura come segue:
```C++
#include <Arduino.h>

void setup() {
//Il codice all'interno di questa funzione è solamente di setup, viene eseguito solo una volta
}

void loop() {
//Il codice principale (logica) viene scritta qua ed eseguita ripetutamente
}
```