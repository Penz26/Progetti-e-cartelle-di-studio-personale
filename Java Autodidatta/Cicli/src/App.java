import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        //Cicli While, vengono ripetuti finché la condizione è vera
        String name = "";
        while(name.isEmpty()){
            System.out.print("Inserisci il tuo nome: ");
            name = scanner.nextLine();
        }

        System.out.println("Ciao " + name);



        String response = "";
        while(!response.equals("Q")){
            System.out.println("Stai giocando ad un gioco");
            System.out.println("Scrivi Q per uscire");
            response = scanner.nextLine().toUpperCase();
        }
        System.out.println("Hai lasciato il gioco"); 



        int age = 0;
        System.out.print("Quanti anni hai? ");
        age = scanner.nextInt();
        while(age <=0){
            System.out.print("Età non valida. Inserisci un'età valida: ");
            age = scanner.nextInt();
        }

        System.out.println("Hai " + age + " anni");
        scanner.nextLine();
        //do-while, viene eseguito almeno una volta, poi continua finché la condizione è vera
        String password = "";
        do{
            System.out.print("Inserisci la password: ");
            password = scanner.nextLine();
        }while(password.isEmpty());

        System.out.println("Password inserita correttamente");


        int numero = 0;
        do{
            System.out.print("Inserisci un numero da 1 a 10: ");
            numero = scanner.nextInt();
        }while(numero <=0 && numero >10);

        System.out.println("Il numero che hai inserito è valido (" +numero+ ").");


        //for , esegue un blocco di codice per un determinato numero di volte

        for(int i=0; i < 10; i++){
            System.out.println(i);
        }

        for(int i=10; i>=0; i-=2){
            System.out.println(i);
        }

        System.out.print("Inserisci quante volte vuoi ripetere");
        int max = scanner.nextInt();

        for(int i=0; i<=max; i++){
            System.out.println("Ripetizione " + (i));
        }


        //break = esce da un ciclo (STOP)
        //continue = salta l'terazione attuale del loop (SKIP)

        for (int i = 0; i < 10; i++){
            if(i == 5){
                break   //una volta che il contatore arriva a 5 il ciclo si ferma
            }
            System.out.println("Ripetizione " + (i));
        }

        for(int i = 0; i < 10; i++){
            if(i == 5){
                continue;   //Una volta che il contatore arriva a 5 TUTTO quello che viene dopo viene saltato
            }
        }


        //Cicli annidati
        //Vengono utilizzati soprattutto per matrici, algoritmi e data structure o per seguire più cicli alla volta

        for(int i = 1; i <= 3; i++){
            for(int j = 1; j <= 10; j++){
                System.out.println("Ripetizione " + (j));
            }
        }

        int rows;
        int columns;
        char symbol;

        System.out.print("Inserisci il numero di righe: ");
        rows = scanner.nextInt();
        System.out.print("Inserisci il numero di colonne: ");
        columns = scanner.nextInt();
        System.out.print("Inserisci il simbolo che vuoi mostrare: ");
        symbol = scanner.next().charAt(0);

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                System.out.print(symbol);
            }
            System.out.println();
        }
        scanner.close();
    }
}
