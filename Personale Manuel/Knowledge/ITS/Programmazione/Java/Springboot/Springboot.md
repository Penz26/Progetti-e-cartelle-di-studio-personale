#Programmazione #Java

# **Springboot**
>Basato su Inversion of control.
>Springboot sa quando chiamare le classi

>Non esiste un vero e proprio main

>Quando effettua il controllo per cercare che funzioni, variabili da chiamare chiama dei **beans**. Ci sono diversi tipi di beans:
>- restcontroller, si occupano di rispondere alle chiamate HTTP in base alla radice chiamata
>- 
# Creazione progetto

![[springboot-init.png]]

[Inizializzazione](https://start.spring.io/)
- Project: Gradle - Kotlin (Tipo di progetto)
- Language: Java (Linguaggio del progetto)

### Project Metadata
- group: com.example
- artifact: Nome del progetto
- package name: Nome del pacchetto

>Packaging: Jar
>Configuration: YAML (linguaggio di configurazione)
>Java: versione Java (21 stabile)

###  Dependencies
- Lombok
- SpringWeb
---
# Inizio sviluppo

>Comandi utili:
```shell
./gradlew bootRun 
```

- Area di lavoro (src/java/com/example/prova)


```java
package com.example.prova.controller; //Dice al compilatore dove si trova il file

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api") //Radice a cui appartengono tutti gli endpoint di questo controller
public class Healthccontroller {

    @GetMapping("/ping")  //endpoint jvm sotto /api
    public String ping() {
        return "pong";
    }
}
```

>Adesso eseguendo un curl verso localhost:8080/api/ping lui risponderà pong

Mappatura
```java
@GetMapping("/sede/311")
public Map<String.String> sede() {
	return Map.of(
		"nome", "311 Verona",
		"indirizzo", "Lun.ge Galtarossa, 21"
	);
}
```
