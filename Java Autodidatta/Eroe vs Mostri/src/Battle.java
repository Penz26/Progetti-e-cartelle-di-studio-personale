import java.util.Scanner;

public class Battle {
    private static Scanner scanner = new Scanner(System.in); // Scanner statico per leggere l'input dell'utente durante la battaglia
    public static void startBattle(Personaggio eroe, Enemies nemico) { // Metodo statico per avviare la battaglia tra un eroe e un nemico
                                                                        //Un metodo statico è un metodo che appartiene alla classe stessa, piuttosto che a un'istanza specifica della classe. Ciò significa che puoi chiamare questo metodo senza dover creare un oggetto della classe Battle.
        while (eroe.isAlive() && nemico.isAlive()) {
            System.out.println("##########################################");   
            System.out.println("ATTACHI IL NEMICO!");
            scanner.nextLine();
            eroe.attack(nemico);
            if (nemico.getHp() > 0) {
                System.out.println("##########################################");
                System.out.println(nemico.getNome() + " ha " + nemico.getHp() + " HP rimanenti.");
                System.out.println(nemico.getNome() + " contrattacca " + eroe.getNome() + " con " + nemico.getAtk() + " punti danno.");
                scanner.nextLine();
                eroe.setHp(eroe.getHp() - nemico.getAtk());
                if (eroe.getHp() <= 0) {
                    eroe.setIsAlive(false);
                    System.out.println(eroe.getNome() + " è stato sconfitto!");
                    
                } else {
                    System.out.println(eroe.getNome() + " ha " + eroe.getHp() + " HP rimanenti.");
                }
            }else{
                System.out.println("Il nemico è stato sconfitto!");
                nemico.setIsAlive(false);
            }
        }
    }
}
