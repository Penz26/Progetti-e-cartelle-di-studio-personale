import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        //Cicli While, vengono ripetuti finché la condizione è vera
        String name = "";
        while(name.isEmpty()){
            System.out.println("Inserisci il tuo nome: ");
            name = scanner.nextLine();
        }

        System.out.println("Ciao " + name);



        String response = "";
        while(!response.equals("Q")){
            System.out.println("Stai giocando ad un gioco");
            System.out.println("Scrivi Q per uscire");
            response = scanner.nextLine();
        }
        System.out.println("Hai lasciato il gioco"); 



        int age = 0;
        System.out.print("Quanti anni hai? ");
        age = scanner.nextInt();
        while(age <=0){
            System.out.println("Età non valida. Inserisci un'età valida: ");
            age = scanner.nextInt();
        }

        System.out.println("Hai " + age + " anni");

        //do-while, viene eseguito almeno una volta, poi continua finché la condizione è vera
        String password = "";
        do{
            System.out.println("Inserisci la password: ");
            password = scanner.nextLine();
        }while(password.isEmpty());

        System.out.println("Password inserita correttamente");


        int numero = 0;
        do{
            System.out.println("Inserisci un numero da 1 a 10");
            numero = scanner.nextInt();
        }while(numero <=0 && numero >10);

        System.out.println("Il numero che hai inserito è valido (" +numero+ ").");


    }
}
