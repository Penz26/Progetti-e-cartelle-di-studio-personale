import  java.util.Scanner;
public class Introduzione {
    public static void main(String[] args) {    //Ogni codice con Java deve avere questa linea per poter funzionare
        System.out.print("Hello World");    //System.out.print permette di stampare a schermo quello che inseriamo all'interno dei doppi apici
                                                // ogni comando in Java deve essere chiuso con ; come in C
     
        System.out.println("This is my first Java program");    //aggiungendo ln a print permette di mandare a capo dopo la stringa
        System.out.println("This string is on another line!\n");          //altrimenti possiamo usare \n per mandare a capo
        System.out.print("This one too!");


        //System.out.printf si usa per formattare come si vuole l'output
        //Esempi:

        String personaggio = "Spongebob";
        System.out.printf("Ciao %s\n", personaggio);            //%s per gli string

        char inizio = 'C';
        System.out.printf("Il tuo nome inizia con %c\n", inizio);   //%c per i char

        int grado = 8;
        System.out.printf("Sei di grado %d\n", grado);          //%d per gli int

        double valori = 55.3232;
        System.out.printf("I tuoi valori sono %f\n", valori);   //%f per i double
        //Si possono anche limitare i valori decimali arrotondandoli automaticamente da far vedere così:
        System.out.printf("%.1f\n", valori);

        boolean risposta = false;
        System.out.printf("La risposta era %b\n", risposta);    //%b per i boolean

        //Più formattazioni alla volta
        System.out.printf("%s è di grado %d\n", personaggio, grado);

        //Dopo % si possono mettere + per specificare che sia positivo
        // , per formattare coi punti le migliaia
        // ( racchiude i numeri negativi in ()
        // space con uno spazio dopo al % i numeri positivi avranno uno spazio davanti mentre quelli negativi avranno un meno davanti

        //Possiamo mettere degli 0 davanti ai numeri così da renderli tutti omogenei con %0n (n sta per il numero di 0 che vogliamo davanti)
        //con un numero decidiamo quanto padding dargli di spazio
        //con un numero negativo decidiamo quanti spazi dargli dopo


        //I commenti come abbiamo visto sono aperti con //
        /*
        Dei commenti su più righe si aprono con (/*) */
        
        //#1. Variabili
        //Le variabili si dividono in 2 tipi in Java

        //Primitive, valori allocati direttamente nella memoria (stack)
        //E sono: int, double, char, boolean

        //Mentre le Reference sono variabili di massa che si riferiscono a un valore ma non a dove è allocata
        //E sono string, array, object


        //Step delle variabili:
        //1. Dichiarazione
        //2. Assegnazione
        int age;
        age = 19;
        System.out.print(age);

        //Concatenazione
        System.out.println("Io ho " + age + " anni.");

        double price;
        price = 19.99;
        System.out.println(price);


        char genere;
        genere = 'M';
        System.out.println(genere);

        boolean isVivo;
        isVivo = true;
        System.out.println(isVivo);

        String nome;
        nome = "John";
        System.out.println(nome);

        //2. Scanner (User Input)
        //Bisogna importare come prima cosa degli utensili di java
        //Attraverso:
        //import java.util.Scanner;

        Scanner sc = new Scanner(System.in);

        System.out.print("Inserisci il tuo paese di nascita: ");
        String paese = sc.nextLine();   //nextLine legge la stringa contando anche gli spazi
                                        //next e basta non considera gli spazi
        System.out.println(paese);

        System.out.print("Inserisci il tuo numero preferito: ");
        int numero = sc.nextInt();      //nextInt legge gli interi
        System.out.println(numero);

        System.out.print("Qual' è la tua media scolastica: ");
        double media = sc.nextDouble(); //nextDouble legge i decimali
        System.out.println(media);

        System.out.print("Sei uno studente? (true/false): ");
        boolean isStudente = sc.nextBoolean(); //nextBoolean legge i valori booleani
        System.out.println(isStudente);

        //Quando si chiede un numero e dopo una stringa bisogna mettere di un sc.nextLine() dopo quello del numero per cancellare il buffer


        //A fine programma è buona prassi chiudere lo scanner
        sc.close();

        //3. IF & ELSE

        if(age >= 18){
            System.out.println("Sei maggiorenne");
        }else if(age < 0){
            System.out.println("Non sei ancora nato");
        }else{
            System.out.println("Sei minorenne");
        }
    }
}
