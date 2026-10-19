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

---
## **Registri**
>Parte in cui copiare i valori per farli eseguire alla CPU

primo registro della CPU in 64 bit, tutti i registri sono divisi a metà.
La metà meno significativa quella a destra (EAX). Questa è divisa di nuovo in 2 parti (AX , AL)

RAX
RBX
RCX
RDX

RSI, registro di inizio stringa 
RDI, registro di fine stringa

RSP, stack point (dove scrivere)
RBP, base point

R8
...
R15

RIP, instructure point

---
# Assembly
>Piccole indicazioni di codice che indicano lo spostamento di dati da vari registri


>[!NOTE] La sintassi di ogni comando è la seguente
operazione DESTINAZIONE SORGENTE/VALORE

>MOV sposta/copia valori da un registro ad un altro
```c
MOV RAX 0      //Spostiamo il valore 0 al registro RAX
MOV RBX RAX

MOV RCX [113]   //spostiamo quello che c'è dentro l'indirizzo 113 dentro il registro RCX

MOV [114] RAX    //Così invece lo leggiamo
```

>ADD somma il valore al valore dentro un registro e ne salva il risultato
```C
ADD RAX 1

//Aggiungiamo 1 (IMMEDIATO) al valore dentro RAX
```

![[Registers]]

>PUSH copia il suo parametro, sposta avanti il suo parametro
```C
PUSH RAX //=1
```

>POP, rimuove il valore più in alto nello stack e rimette l' RSP su quello
```C
POP RCX //=67
```

```C
MV RDX [RSP-3] //Copiamo quello che c'è nello stack point -3 e lo mettiamo dentro RDX 
```

>Compilare ed avvviare uno script in assembly:
```shell
nasm -f elf64 nomefile.asm -o nomefile.o; ld nomefile.o -o nomefile
```

>Questo programma avrà alla fine del programma tutti i regiistri a valore 2
>Ma andrà in segmentation fault
```C
section .text ;sezione dell' ELF che contiene il codice
	global _start ;gli diciamo dove inizia lo _start

	_start: ;inizio programma
		mov rax, 1
		add rax, 1
		mov rbx, rax
		push rbx ;scrive gli 8byte contenuti dentro rbx in ram all'indirizzo indicato nel puntatore di stack rsp
		pop rcx ;prende il valore che era in cima allo stack e lo carica dentro rcx1
```

>Per non farlo andare in segmentation fault dobbiamo ridare il controllo al kernel.
>L'equivalente di un return a fine programma
>Rimette in Rip (instructure point)
```C
mov rax, 60
mov rdi 0

syscall 
```

Una volta compilato il programma con nasm per avviarlo e vedere come procede.
```C
gdb nomefile

//Settiamo il breakpoint da cui partire
b _start

//ogni istruzione da seguire si vede con 
ni

//La sezione dei registri 
```