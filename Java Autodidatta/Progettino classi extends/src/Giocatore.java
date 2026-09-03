import java.util.Scanner;

public class Giocatore extends Personaggio {
    private int difesaAttiva;

    public Giocatore(String nome, int vita, int attacco, int difesa) {
        super(nome, vita, attacco, difesa);
        this.difesaAttiva = 0;
    }

    // Azione di attacco
    public void attacca() {
        System.out.println(getNome() + " attacca!");
    }

    // Azione di difesa
    public void difenditi() {
        this.difesaAttiva = (int) (getDifesa() * 1.5); // Bonus difesa temporaneo
        System.out.println(getNome() + " si difende! Difesa temporanea: +" + (int)(getDifesa() * 0.5));
    }

    // Getter per difesa attiva
    public int getDifesaAttiva() {
        return difesaAttiva;
    }

    public void resettaDifesaAttiva() {
        this.difesaAttiva = 0;
    }

    // Override del metodo subisciDanno per considerare la difesa attiva
    @Override
    public int subisciDanno(int dannoInflitto) {
        int difesaTotale = getDifesa() + difesaAttiva;
        int dannoFinale = Math.max(1, dannoInflitto - difesaTotale / 2);
        resettaDifesaAttiva(); // Resetta la difesa dopo il turno
        return dannoFinale;
    }

    @Override
    public String agisci() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\n--- Turno di " + getNome() + " ---");
        System.out.println("Vita: " + getVita());
        System.out.println("1. Attaccare");
        System.out.println("2. Difendersi");
        System.out.print("Scegli un'azione (1-2): ");
        
        int scelta = scanner.nextInt();
        
        if (scelta == 1) {
            attacca();
            return "attacca";
        } else if (scelta == 2) {
            difenditi();
            return "difende";
        } else {
            System.out.println("Azione non valida, attacchi!");
            attacca();
            return "attacca";
        }
    }
}
