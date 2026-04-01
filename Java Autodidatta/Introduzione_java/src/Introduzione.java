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

        //Si possono avere condizioni if nested come in ogni linguaggio di programmazione
        //Come nell'esempio:

        if(age > 0){
            if(age >= 18){
                System.out.println("Sei maggiorenne");
            }else if(age <18){
                System.out.println("Non sei ancora maggiorenne");
            }
        }else{
            System.out.println("Non sei ancora Nato");
        }


        //4. Metodi delle stringhe

        String chiave = "Caspiterina";

        int lunghezza = chiave.length();    //restituisce la lunghezza (contando gli spazi della stringa
        char letter = chiave.charAt(0);     //Restituisce la lettera all'index specificato
        int index = chiave.indexOf("a");    //Restituisce l'indice di dove appare per la prima volta la lettera all'interno della stringa
        int lastIndex = chiave.lastIndexOf("a"); //Restituisce l'indice di dove appare la lettera per l'ultima volta all'interno della stringa

        System.out.println(lunghezza);
        System.out.println(letter);
        System.out.println(index);
        System.out.println(lastIndex);

        chiave = chiave.toUpperCase();      //Rende la stringa MAIUSCOLA
        chiave = chiave.toLowerCase();      //Rende la stringa MINUSCOLA

        chiave = "     Accidenti    ";
        chiave = chiave.trim();             //Elimina gli spazi davanti e dietro

        chiave = chiave.replace("a", "i");  //Rimpiazza la prima lettera con la seconda

        System.out.println(chiave.isEmpty());   //ritorna true o false

        System.out.println(chiave.contains(" "));   //ritorna true or false in base se la stringa contiene tale carattere

        if(chiave.equals("password")){           //ritorna true or false se la stringa è uguale a quella determinata (CASE SENSITIVE)
            System.out.println("La password non può essere password");
        }

        if(chiave.equalsIgnoreCase("password")){        //ritorna true or false se la stringa è uguale a quella determinata (CASE INSENSITIVE
            System.out.println("La password non può essere password");
        }

        //Substring
        String email = "blabla@gmail.com";
        String username = email.substring(0, 6); //prende i caratteri da 0 a 6 NON COMPRESI
        String domain = email.substring(9);

        //Così è più flessibile:
        username = email.substring(0, email.indexOf("@"));  //Parte dall'inizio ed arriva fino alla @ senza comprenderla
        domain = email.substring(email.indexOf("@") +1);    //Parte dal carattere dopo la chiocciola e và fino alla fine
        System.out.println(username);
        System.out.println(domain);


        //Operatore Terziario (?)
        int score = 70;

        String passOrFail = (score >= 60) ? "PASS" : "FAIL";    //Se la condizione è vera stampa PASS altrimenti (:) stampa FAIL
        System.out.println(passOrFail);

        //Switch Case (sostituto di if cases inutili)
        String day = "Venerdì";
        switch(day){
            case "Lunedì" -> System.out.println("Oggi è Lunedì");
            case "Martedì" -> System.out.println("Oggi è Martedì");
            case "Mercoledì" -> System.out.println("Oggi è Mercoledì");
            case "Giovedì" -> System.out.println("Oggi è Giovedì");
            case "Venerdì" -> System.out.println("Oggi è Venerdì");
            //Si possono aggregare questi per dire "E' una giornata normale" così:
            //case "lunedì" , "martedì", "mercoledì", ecc.. -> System.out.println("Giornata normale");
            case "Sabato" -> System.out.println("Oggi è Sabato");
            case "Domenica" -> System.out.println("Oggi è Domenica");
            default -> System.out.println(day + " non è una giornata.");   //Se nessuna delle condizioni è rispettata enterà in questo
        }

        //Operatori Logici
        //&& = AND
        //|| = OR
        //! = NOT
        
        double temp = 40;
        boolean isSunny = true;
        
        if(temp <= 30 && temp >= 0 && isSunny){         //ENTRAMBE LE CONDIZIONI DEVO ESSERE TRUE
            System.out.println("Giornata perfetta per uscire");
            System.out.println("C'è mite e c'è il Sole");
        } else if (temp <= 30 && temp >= 0 && !isSunny) {   //TUTTE LE CONDIZIONI DEVONO ESSERE VERE, e NON ci deve essere il sole
            System.out.println("Il tempo è bello");
            System.out.println("Ma non c'è il Sole");
        } else if (temp > 30 || temp < 0){
            System.out.println("Il tempo è brutto");
        }


    }
}
