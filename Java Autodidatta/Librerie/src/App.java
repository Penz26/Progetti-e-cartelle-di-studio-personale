import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {

        //RANDOM

        //Creiamo il nostro generatore di valori randomici:
        Random rand = new Random();

        int number;
        number = rand.nextInt(1, 7);    //Numero da cui partire (compreso), Numero a cui arrivare (non compreso)
        System.out.println(number);

        double decimal;
        decimal = rand.nextDouble(1.0, 10.01);  //Numero decimale da 1.0 a 10.0
        System.out.println(decimal);

        boolean bool;
        bool = rand.nextBoolean();  //True or False
        System.out.println(bool);

        //MATH

        System.out.println(Math.PI);    //Stampa il valore arrotondato del pi greco
        System.out.println(Math.E);     //Stampa il numero di Nepero

        double result;
        result = Math.pow(2, 4);        //Base, Esponente
        System.out.println(result);

        result = Math.abs(-5);          //Restituisce il Valore Assoluto
        System.out.println(result);

        result = Math.sqrt(9);          //Radice Quadrata
        System.out.println(result);

        result = Math.round(3.1321);    //Arrotonda all'intero più vicino
        System.out.println(result);

        result = Math.floor(3.1321);    //Arrotonda per difetto all'intero più vicino in ogni caso
        System.out.println(result);

        result = Math.ceil(3.1321);     //Arrotonda per eccesso all'intero più vicino in ogni caso
        System.out.println(result);

        result = Math.max(10, 20);      //Confronta tra questi qual'è il numero più grande
        System.out.println(result);

        result = Math.min(10, 20);      //Confronta tra questi qual'è il numero più piccolo
        System.out.println(result);
    }
}
