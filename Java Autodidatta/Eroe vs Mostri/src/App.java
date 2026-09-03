import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Inserisci il nome del personaggio: ");
        String nome = scanner.nextLine();
        System.out.print("Inserisci la classe del personaggio: ");
        String classe = scanner.nextLine();
        System.out.print("Inserisci i punti salute del personaggio: ");

        Personaggio Eroe = new Personaggio(nome, classe, scanner.nextInt(), 10);
        Eroe.Stats();
        System.out.println("##########################################");

        System.out.print("CHE ABBIA INIZIO LA BATTAGLIA! PREMERE INVIO PER CONTINUARE...");
            scanner.nextLine(); // Consuma il newline rimasto
            scanner.nextLine(); // Attende l'input dell'utente
    
        Enemies Nemico1 = new Enemies("Goblin", "Guerriero", 30, 5);
        Enemies Nemico2 = new Enemies("Orco", "Guerriero", 50, 8);
    
        while (Eroe.isAlive()){
            if (!Nemico1.isAlive() && !Nemico2.isAlive()) {
                System.out.println("Hai sconfitto tutti i nemici! Complimenti!");
                scanner.nextLine();
                break;
            }else if (!Nemico1.isAlive()) {
                System.out.println("Il nemico " + Nemico1.getNome() + " è stato sconfitto! Ora affronti " + Nemico2.getNome());
                scanner.nextLine();
                Battle.startBattle(Eroe, Nemico2);
            }else if (!Nemico2.isAlive()) {
                System.out.println("Il nemico " + Nemico2.getNome() + " è stato sconfitto! Ora affronti " + Nemico1.getNome());
                scanner.nextLine();
                Battle.startBattle(Eroe, Nemico1);
            }else{
                System.out.println("DAVANTI A TE SI MOSTRANO DEI NEMICI:");
                Nemico1.printStats();
                System.out.println("##########################################");
                Nemico2.printStats();
                System.out.println("Scegli un nemico da attaccare (1 o 2): ");
                int scelta = scanner.nextInt();
                if (scelta == 1){
                    System.out.println("La battaglia tra " + Eroe.getNome() + " e " + Nemico1.getNome() + " è iniziata!");
                    scanner.nextLine();
                    Battle.startBattle(Eroe, Nemico1);
                }else{
                    System.out.println("La battaglia tra " + Eroe.getNome() + " e " + Nemico2.getNome() + " è iniziata!");
                    scanner.nextLine();
                    Battle.startBattle(Eroe, Nemico2);
                }
            }
            
        }
        System.out.println("Il gioco è terminato.");
    }
}
