import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("╔══════════════════════════════════════╗");
        System.out.println("║     BATTLE ARENA - Benvenuto!         ║");
        System.out.println("╚══════════════════════════════════════╝\n");
        
        System.out.print("Inserisci il nome del tuo personaggio: ");
        String nomeGiocatore = scanner.nextLine();
        
        // Crea il giocatore con statistiche iniziali
        Giocatore giocatore = new Giocatore(nomeGiocatore, 100, 20, 10);
        
        System.out.println("\n" + giocatore.getNome() + " entra nell'arena!");
        System.out.println("Statistiche iniziali:");
        System.out.println("  Vita: " + giocatore.getVita());
        System.out.println("  Attacco: " + giocatore.getAttacco());
        System.out.println("  Difesa: " + giocatore.getDifesa());
        
        // Avvia l'arena
        GestioneCombattimento.avviaArena(giocatore);
        
        scanner.close();
    }
}
