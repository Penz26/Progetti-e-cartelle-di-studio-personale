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

import java.util.Arrays;
import java.util.Scanner;
public class App {      //Senza questa funzione il programma non parte
    public static void main(String[] args) throws Exception {      //args ci permette di prendere in input valori dal prompt dei comandi
        //Senza questa funzione il programma non parte
        // la funzione main è void perché appunto non deve ritornare nulla



        //ESERCIZI BASE
        //1

        //System.out.println("Inserisci un numero: ");    //Questo comando permette di stampare a schermo con una linea a capo
        //System.out.print("");         Invece permette di stampare non andando a capo

        Scanner input = new Scanner(System.in);     //Anche gli scanner vanno inizializzati il suo nome sarà input
                                                    //Potrà essere utilizzato per tutto il programma
        /*
        int numero_1 = input.nextInt();          //In Java le variabili devono prima essere dichiarate
                                                //Si possono anche solo dichiarare e dargli il valore dopo
                                                //int num;
                                                //num = 9;

        //Le variabili possono essere di 2 tipi:
        //Primitive e Wrapper
        //Con le primitive non abbiamo delle funzioni integrate che avremmo con le Wrapper
        //Primitive iniziano con lettera minuscola
        //Wrapper iniziano con lettera Maiuscola

        // con input.nextint() prenderà in input un intero

        if (numero_1 > 0){                      //Ci vanno le { per aprire gli if e per chiuderli }, le condizioni vanno all'interno delle ()
            System.out.println("Il numero è positivo");
        }else if (numero_1 < 0){                //else if invece che elif come in Python
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

        input.nextLine();  // Resetta lo scanner prima di dover prendere un altro tipo di dato
        //4
        System.out.println("Inserisci una stringa");
        String mia_stringa = input.nextLine();
        if (mia_stringa == ""){
            System.out.println("La stringa è vuota");
        }else{
            System.out.println("La stringa non è vuota");
        }


        Si poteva fare anche con delle funzioni integrate delle stringhe:

        if (miastringa.isEmpty){
            ecc...

        if (miastringa.length() == 0){
            ecc ...
        }

        //5
        System.out.println("Inserisci un numero: ");
        int numero_5 = input.nextInt();
        System.out.println("Inserisci un numero: ");
        int numero_6 = input.nextInt();
        
        input.nextLine();  // Resetta lo scanner prima di dover prendere un altro tipo di dato
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
        for (int i = 0; i <= tabellina * 10 ; i+=tabellina ){   // (start, stop, step) come il range di python ma i campi non sono trascurabili
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

        for (i = 0; i < misura; i++){
            for (int j = 0; j < misura; j++){ //stampa la prima riga
                System.out.print("$");
            }
            System.out.println();   //va a capo visto che la prima riga è finita e riprende da capo
        }

        //9
        for (i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){ //stampa la prima riga
                System.out.print(i * j);
            }
            System.out.println();   //va a capo visto che la prima riga è finita e riprende da capo
        }

        //ARRAY//

        int[] numeri = {1, 2, 3, 4, 5};     //DEGLI ARRAY VANNO DICHIARATI IL TIPO CHE CONTERRA' E LA SUA LUNGHEZZA
        //int[] numbers = new int[5];         COSI' DICIAMO CHE L'ARRAY AVRA' 5 ELEMENTI AL SUO INTERNO

        //11

        for (int pos = 0; pos < numeri.length; pos++ ){
            numeri[pos] = numeri[pos] * numeri[pos];
            System.out.println(numeri[pos]); //li stampa uno alla volta
        }

        System.out.println (Arrays.toString(numeri)); //questo stampa l'array in una botta sola
        //converte momentaneamente l'array in una stringa

        //12

        String[] stati_europei = new String[12];
        stati_europei[0] = "Italia";
        stati_europei[1] = "Francia";
        stati_europei[2] = "Germania";
        stati_europei[3] = "Norvegia";
        stati_europei[4] = "Spagna";
        int stati_valorizzati = 0;









































































        
        int stati_non_valorizzati = 0;
        for (String stato : stati_europei){
            if(stato != null){
                stati_valorizzati++;
            }else{
                stati_non_valorizzati++;
            }
        }
        System.out.println("Stati valorizzati " + stati_valorizzati);
        System.out.println("Stati non valorizzati " + stati_non_valorizzati);

        //13
        int numeriLista[] = {1,7,2,9,5};
        int numeri2[] = Arrays.copyOf(numeriLista, numeriLista.length); //crea un altro array con le stesse caratteristiche dell'originale
        Arrays.sort(numeri2);   //mette in ordine crescente l'array
        System.out.println(Arrays.toString(numeri2));   //questo stampa l'array in una botta sola
        //converte momentaneamente l'array in una stringa

    }
}
