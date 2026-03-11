////////////// ESERCIZI ///////////////

// 1) da numero in input, controllare se è positivo o negativo e scrivere
//    "il numero è positivo" o "il numero è negativo" oppure "il numero
//    non è nè positivo nè negativo"
// 2) prendendo 2 numeri in input confrontarli e scrivere, a seconda dei casi
//    "il primo numero è maggiore", "il secondo numero è maggiore" oppure
//    "i due numeri sono uguali"
// 3) da un numero in input stampare "il numero è pari" se è pari o 
//    "il numero è dispari" se è dispari
// 4) chiedi in input una stringa, se la stringa è vuota stampare "la stringa
//    è vuota", altrimenti stampare "la stringa non è vuota"
// 5) chiedere all'utente di inserire due numeri, e l'operazione che vuole
//    eseguire trs (+,-,*,/). In base all'operazione stampare tutta l'operazione
//    e il risultato (tipo "8 * 4 = 32")
//    RICORDA: SE CI SONO PROBLEMI A PRENDERE I NUMERI/STRINGHE IN INPUT
//             QUANDO SI PRENDE IN INPUT I NUMERI SCRIVERE:
//    int num1 = scanner.nextInt();
//    scanner.nextLine();
// 6) chiedi in input un voto tra 1 e 10, se il voto è compreso tra 6 e 10
//    stampare "il voto è sufficiente", se è tra 1 e 6 stampare "il voto
//    è insufficiente", se è minore di 1 o maggiore di 10 stampare "il voto
//    non è valido"


////////////// CICLI ///////////////

// 7) Scrivere un programma che chieda all'utente di quale numero scrivere
//    la tabellina, della tabellina stampare solo i primi 10 numeri
//	  FARLO SIA CON IL CICLO FOR CHE CON IL CICLO WHILE
//    Es. se l'utente inserisce il numero 5, si dovrà stampare a schermo:
//    5
//    10
//    15
//    20
//    25
//    30
//    35
//    40
//    45
//    50
// 8) Scrivere un programma che chieda all'utente un numero, stampare un
//    quadrato fatto di dollari "$" con la lunghezza del lato del numero
//    inserito dall'utente.
//    Es.
//    Dimmi un numero: 4
//    $$$$
//    $$$$
//    $$$$
//    $$$$
// 9) Scrivere un programma che stampi la tavola pitagorica, con i lati che
//     vanno da 1 a 10. (per stampare il tab si fa "\t")
//     Es.
//     1       2       3       4       5       6       7       8       9       10
//     2       4       6       8       10      12      14      16      18      20
//     3       6       9       12      15      18      21      24      27      30
//     4       8       12      16      20      24      28      32      36      40
//     5       10      15      20      25      30      35      40      45      50
//     6       12      18      24      30      36      42      48      54      60
//     7       14      21      28      35      42      49      56      63      70
//     8       16      24      32      40      48      56      64      72      80
//     9       18      27      36      45      54      63      72      81      90
//     10      20      30      40      50      60      70      80      90      100
// 10) Scrivere un programma che chieda all'utente di indovinare un numero
//    da 1 a 100, e continui a chiedere all'utente di indovinare il numero
//    finchè il numero non è stato indovinato. Ogni volta che l'utente prova
//    ad indovinare il numero gli diremo se il numero da indovinare è
//    più grande o più piccolo.


////////////// ARRAY ///////////////

// 11) Scrivi un programma che, partendo da un array già popolato di numeri interi, 
//   sostituisca i numeri con i loro quadrati.
// 12) Scrivi un programma che parta da questo codice:
//       String[] stati_europei = new String[12];
//       stati_europei[0] = "Italia";
//       stati_europei[1] = "Francia";
//       stati_europei[2] = "Germania";
//       stati_europei[3] = "Norvegia";
//       stati_europei[4] = "Spagna";
//    stampi il numero di quanti elementi dell'array sono stati valorizzati
//    e quanti no.
// 13) Scrivi un programma che, partendo da un array di numeri interi positivi,
//    crei un altro array e ci metta gli stessi numeri dell'array di partenza
//    ma ordinati in ordine crescente.

import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        
        //ESERCIZI BASE
        //1

        /* 
        System.out.println("Inserisci un numero: ");
        int numero_1 = input.nextInt();
        if (numero_1 > 0){
            System.out.println("Il numero è positivo");
        }else if (numero_1 < 0){
            System.out.println("Il numero è negativo");
        }else{
            System.out.println("Il numero è 0");
        }
        
        input.nextLine();
        //2
        System.out.println("Inserisci un numero: ");
        int numero_2 = input.nextInt();
        System.out.println("Inserisci un numero: ");
        int numero_3 = input.nextInt();

        if (numero_2 > numero_3){
            System.out.println("Il primo numero è più grande");
        }else{
            System.out.println("Il secondo numero è più grande");
        }

        //3

        System.out.println("Inserisci un numero: ");
        int numero_4 = input.nextInt();
        if (numero_4 % 2 == 0){
            System.out.println("Il numero è pari");
        }else{
            System.out.println("Il numero è dispari");
        }

        input.nextLine();  // Resetta lo scanner dopo dover prendere un altro tipo di dato
        //4
        System.out.println("Inserisci una stringa");
        String mia_stringa = input.nextLine();
        if (mia_stringa == ""){
            System.out.println("La stringa è vuota");

        }else{
            System.out.println("La stringa non è vuota");
        }

        //5
        System.out.println("Inserisci un numero: ");
        int numero_5 = input.nextInt();
        System.out.println("Inserisci un numero: ");
        int numero_6 = input.nextInt();
        
        input.nextLine(); 
        System.out.println("Inserisci l'operazione: ");
        String operatore = input.nextLine();

        if (operatore.equals("+") ){        //per comparare stringhe si usa .equals("+")
            int risultato = numero_5 + numero_6;
            System.out.println("Il risultato è: " + risultato);
        }else if (operatore.equals("-")){
            int risultato = numero_5 - numero_6;
            System.out.println("Il risultato è: " + risultato);
        }else if (operatore.equals("*")){
            int risultato = numero_5 * numero_6;
            System.out.println("Il risultato è: " + risultato);
        }else{
            int risultato = numero_5 / numero_6;
            System.out.println("Il risultato è: " + risultato);
        }

        //6
        System.out.print("Inserisci un voto: ");
        int voto = input.nextInt();
        if (voto >= 6 && voto <= 10){
            System.out.println("Il voto è sufficente");
        }else if (voto > 0 && voto < 6){
            System.out.println("Il voto è insufficente");
        }else{
            System.out.println("Il voto è invalido");
        }

        */
        //CICLI

        //7
        System.out.print("Di che numero vuoi vedere la tabellina: ");
        int tabellina = input.nextInt();
        for (int i = 0; i <= tabellina * 10 ; i+=tabellina ){
            System.out.println(i);
        }

        int i = 0;
        while (i <= tabellina * 10){
            System.out.println(i);
            i+=tabellina;
        }

        //8
        System.out.println("Inserisci misura: ");
        int misura = input.nextInt();

        for (i = 0; i <= misura; i++){
            for (int j = 0; j < i; j++){
                System.out.print("$");
            }
            System.out.println("$");
        }

    }
}
