#CyberSecurity 
# Linguaggio di programmazione C

- Principali vulnerabilità:
1. Buffer Overflow
2. Format string attack
3. Integer overflow
4. Use-After-Free
5. Race condition/TOCTOU
6. Command Injection

## Compilare il file .c con:
```Bash
gcc nome_file.c
```

## Questo produce un file eseguibile chiamato solitamente a.out, che si esegue normalmente con ./
```Bash
./a.out
```

## 1. **Buffer Overflow**

```C
#include <stdio.h>
#include <stdlib.h>

int main(){
	char buffer[10];
	printf("Inserisci qualcosa: ");
	gets(buffer);
	printf("Hai scritto: %s\n", buffer);
	
	return 0;
}

```

>Se inseriamo del testo di più di 10 caratteri ci darà un problema perchè appunto il buffer è di solo 10.
>Possiamo evitare questo overflow eseguendolo dalla shell con: 


>-fno-stack-protector disabilita lo Stack Canary, ovvero un piccolo valore casuale posto sullo stack prima dell'indirizzo di ritorno.
>Se un utente tenta un _buffer overflow_, il canarino viene sovrascritto, il programma se ne accorge e si chiude immediatamente per evitare l'esecuzione di codice malevolo.
>
```bash
gcc -fno-stack-protector nome_file.c
```

>Ma a causa di ciò i caratteri inseriti che eccedono il decimo spazio del buffer vengono scritti al di fuori del buffer e quindi va ad occupare delle celle di memoria al di fuori del buffer.

```C
#include <stdio.h>
#include <stdlib.h>
int main(){
	char buffer[10];
	printf("Inserisci qualcosa" );
	gets(buffer);
	
	
	for(int i = 0; i<100; i++){
		printf("%c", *(buffer+i))  //con * indichiamo il primo valore del                                      buffer, questa cosa si chiama puntatore
	}
}
```

>Con questo codice stamperemo il buffer ma anche delle robe che avevamo in memoria fino ad arrivare al 100esimo valore del ciclo.
>PERCHE' NON ABBIAMO ALLOCATO GLI SPAZI DI MEMORIA

---

## **2. Format String Attack**
>Con questo blocco di codice aveva libertà di stamparlo in qualsiasi formato volesse
>Se inseriamo %x o %n ec.. ci darà i relativi valori in quel formato (come %x ci dà un valore esadecimale)
```C
#include <stdio.h>
#include <stdlib.h>
int main(){
	char buf[256];
	fgets(buf, sizeof(buf), stdin);
	printf(buf)
}
```

>Mentre con questo gli diciamo che il formato che deve stampare è per forza String
```C
#include <stdio.h>
#include <stdlib.h>
int main(){
	char buf[256];
	fgets(buf, sizeof(buf), stdin);
	printf("%s", buf)
}
```

---

## **3. Integer Overflow**
>Il programma richiede un numero e questo numero deve essere allocato in memoria
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
	size_t n = (size_t)atoi(argv[1]);
	sixe_t alloc_size = n * sizeof(int);
	
	printf("n               = %zu\n", n);
	printf("sizeof(int)     = %zu\n", sizeof(int));
	printf("alloc_size      = %zu\n", alloc_size, alloc_size)

	//Sorgente di dati: 16 byte innocui
	char src[16] = "AAAABBBBCCCCDDDD";
	char *buf = malloc(alloc_size);
	if(!buf)
	{
		printf("malloc fallita (size troppo grande o overflow evidente)\n");
		return 1;
	}
	printf("buf allocato a: %p  (size richiesta: %zu byte)\n", (void*)buf, alloc_size);
	memcpy(buf, src, n * sizeof(int));
	printf("memcpy completata (o crash avvenuto sopra)\n");
	free(buf);
	
	return 0;
}
```
>PERO' IN QUESTA VERSIONE


>Per risolvere:
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limit.h> 
//oppure

#define MAX_SIZE 10000

int main(int argc, char *argv[]){
	size_t n = (size_t)atoi(argv[1]);
	if (n > MAX_SIZE)
		return 1;
		
	size_t alloc_size = n * sizeof(int);
	
	printf("n               = %zu\n", n);
	printf("sizeof(int)     = %zu\n", sizeof(int));
	printf("alloc_size      = %zu\n", alloc_size, alloc_size)

	//Sorgente di dati: 16 byte innocui
	char src[16] = "AAAABBBBCCCCDDDD";
	char *buf = malloc(alloc_size);
	if(!buf)
	{
		printf("malloc fallita (size troppo grande o overflow evidente)\n");
		return 1;
	}
	
	printf("buf allocato a: %p  (size richiesta: %zu byte)\n", (void*)buf, alloc_size);
	memcpy(buf, src, n * sizeof(int));
	printf("memcpy completata (o crash avvenuto sopra)\n");
	free(buf);
	
	return 0;
}

```

---

## **4. Use After Free**

>Creiamo un pointer (* ptr) che PUNTA a quello spazio di memoria
>Una volta cancellati i valori detro quel pointer con free(ptr) quello spazio viene ancora IDENTIFICATO come quello spazio di memoria e quindi se lo ristampiamo ci stamperà i valori che ora sono dentro quello spazio di memoria.
```C                          
#include <stdlib.h>
#include <stdio.h>
int main()
{
    int *ptr = malloc(sizeof(int));
    *ptr = 42;
    free(ptr);
    printf("%d\n", *ptr);
}
```

>COME RISOLVERE:
>mettendo a NULL il ptr lo CANCELLA
```C                          
#include <stdlib.h>
#include <stdio.h>
int main()
{
    int *ptr = malloc(sizeof(int));
    *ptr = 42;
    free(ptr);
    ptr = NULL;
    printf("%d\n", *ptr);
}
```

---
## **5. Race condition/TOCTOU**
>

```C
#include <stdio.h>
#include <string.h>
int main()
{
    char buffer[8];
    int is_admin = 0;
    gets(buffer);
    if (is_admin)
        printf("Accesso admin!\n");
    else
        printf("Accesso normale.\n");
    return 0;
}
```
>gets() prende delle stringhe in input e le butta dentro a buffer, anche se sono numeri gli input quello che verrà registrato sarà una stringa.

|**Tipo**|**Dimensione (Byte)**|**Range Approssimativo**|
|---|---|---|
|**`char`**|1|Da -128 a 127|
|**`short`**|2|Da -32.768 a 32.767|
|**`int`**|4|Da -2 miliardi a +2 miliardi|
|**`long`**|8|Molto ampio (64 bit)|
|**`long long`**|8|Molto ampio (64 bit)|
|**`float`**|4|Precisione singola (virgola mobile)|
|**`double`**|8|Precisione doppia|
|**`long double`**|16|Precisione estesa (spesso 80-bit su x86)|
|**Puntatore** (`void*`, `int*`, etc.)|8|Indirizzo di memoria (su sistemi 64-bit)|

>Inserendogli 9 carattere (numero o lettera) il 9° verrà scritto in is_admin e visto che è un char non vale 0.

>Per farlo eseguire e andare in Race condition tramite gcc flags:
```Bash
gcc -fno-stack-protector -Wno-implicit-function-declaration challenge_11.c
```

>Dice al compilatore: "Stai zitto, non avvertirmi se mancano le dichiarazioni delle funzioni".
>Normalmente il GCC se si prova ad usare funzioni come system() o gets() come in questo caso senza aver incluso l'header corretto il compilatore ti dà un warning


## **2. Esempio**
```C
#include <stdio.h>
#include <string.h>

int main()
{
	char username[8];
	char password[8];
	int authenticated = 0;
	//char authenticated = 0; // variante più interessante

	printf("Username: ");
	gets(username);

	printf("Password: ");
	gets(password);

	if (strcmp(username, "admin") == 0 && strcmp(password, "1234") == 0)
	        authenticated = 1;

	if (authenticated)
		printf("Benvenuto admin!\n");
	else
	printf("Accesso negato.\n");

	return 0;
}
```

>In questo caso se l'username è uguale a "admin" e la password è "1234" l'autenticazione è 1, quindi vera, e stamperà di conseguenza "Benvenuto Admin".
>Può essere mandato in overflow con i comandi di prima.