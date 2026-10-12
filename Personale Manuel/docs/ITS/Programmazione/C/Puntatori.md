#Programmazione #C 

# **Cosa sono?**
>Associando un valore ad una variabile in C il nostro compilatore dovrà trovare l'indirizzo dentro cui è stato asssegnato quel valore in memoria

```C
#include <stdio.h>
int main()
{
	int test = 5;
	int *test_ptr = &test;

	printf("%d", test);
	printf("%x", test_ptr)


}
```

# **ELF (Executable Linkable Format)**
>Formato eseguibile di linux
>Quello che va copiato in memoria in modo che il programma funzioni

![[ELF]]


## **Registro**
>Parte in cui copiare i valori per farli eseguire alla CPU