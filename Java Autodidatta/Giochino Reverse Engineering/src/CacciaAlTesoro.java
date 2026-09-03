import java.util.Scanner;
import java.util.Random;

public class CacciaAlTesoro {

    // VARIABILI GLOBALI (Stato del gioco)
    static int xGiocatore = 0;
    static int yGiocatore = 0;
    static int xTesoro;
    static int yTesoro;
    static int tentativi = 15;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        inizializzaMappa();
        
        System.out.println("=== BENVENUTO ALLA CACCIA AL TESORO ===");
        System.out.println("Il tuo obiettivo è trovare il tesoro nascosto sulla mappa.");
        System.out.println("Puoi muoverti a Nord (N), Sud (S), Est (E) o Ovest (O).");
        
        // CICLO PRINCIPALE DEL GIOCO
        while (tentativi > 0) { //FINCHE' AL GIOCATORE RIMANGONO TENTATIVI IL WHILE CONTINUA A CICLARE, FINCHE':
                                //1. il giocatore trova il tesoro (controllaVittoria() ritorna true) oppure
                                //2. il giocatore finisce i tentativi (tentativi == 0)

            mostraStato();
            
            if (controllaVittoria()) {      //se ritorna true la funzione controllaVittoria() allora entra nell'f che stampa il messaggio e poi usa break per uscire dal ciclo
                System.out.println("\n🎉 INCREDIBILE! Hai trovato il tesoro! Hai vinto!");
                break; // Esce dal ciclo while
            }
            
            System.out.print("Dove vuoi andare? (N/S/E/O): ");
            String direzione = input.nextLine().toUpperCase();  //legge l'input stringa del giocatore e lo converte in maiuscolo così da essere case sensitive
            
            if (mossaValida(direzione)) {   //gli passiamo come argomento la stringa inserita (direzione) dal giocatore
                eseguiMossa(direzione);     //se la mossa è valida, passiamo la stringa in esecuzione
                tentativi--;                //ovviamente essendo la mossa valida, decrementiamo i tentativi
            } else {
                System.out.println("Mossa non valida. Usa solo N, S, E, O.");   //se non ha inserito N, S, E, oppure O, gli diciamo che ha sbagliato
            }
        }
        
        // CONTROLLO SCONFITTA IN BASE AI TENTATIVI
        if (tentativi == 0 && !controllaVittoria()) {
            System.out.println("\n💀 Hai finito i tentativi! Game Over.");
            System.out.println("Il tesoro si trovava alle coordinate: X=" + xTesoro + ", Y=" + yTesoro);
        }
        
        input.close(); // Chiude lo scanner per evitare perdite di memoria
    }




    //==================================================================================================================================
    // --- FUNZIONI DEL GIOCO ---

    //1. Imposta la posizione casuale del tesoro
    static void inizializzaMappa() {
        Random rand = new Random();     //Inizializza un oggetto Random per generare numeri casuali

        xTesoro = rand.nextInt(11) - 5; // Genera un numero casuale tra 0 e 10 e gli sottrae 5 per ottenere un numero tra -5 e 5 grazie all'oggetto rand che abbiamo creato prima
        yTesoro = rand.nextInt(11) - 5; // Genera un numero casuale tra 0 e 10 e gli sottrae 5 per ottenere un numero tra -5 e 5 grazie all'oggetto rand che abbiamo creato prima
        
        // Assicura che il tesoro non sia sulla posizione di partenza
        if (xTesoro == 0 && yTesoro == 0) {
            xTesoro = 3; 
        }
    }

    //==================================================================================================================================


    //2. Stampa le informazioni per il giocatore
    static void mostraStato() {
        System.out.println("\n------------------------------------------------");
        System.out.println("Posizione attuale: [X: " + xGiocatore + ", Y: " + yGiocatore + "]");
        System.out.println("Distanza dal tesoro: " + calcolaDistanza());    //CHIAMATA DI FUNZIONE ALL'INTERNO DI UN ALTRA FUNZIONE,
                                                                            // chiama la funzione calcolaDistanza() per mostrare la distanza al giocatore
        System.out.println("Tentativi rimasti: " + tentativi);
    }


    //====================================================================================================================================================


    //6. Usa il Teorema di Pitagora per calcolare la distanza
    static double calcolaDistanza() {
        int diffX = xTesoro - xGiocatore;
        int diffY = yTesoro - yGiocatore;
        // Math.pow calcola la potenza (al quadrato), Math.sqrt calcola la radice quadrata
        double distanza = Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
        
        // Arrotonda a due decimali
        return Math.round(distanza * 100.0) / 100.0;
    }

    //==========================================================================================================================

    //4. Controlla se la stringa inserita è corretta (N, S, E, O)
    static boolean mossaValida(String input) {
        //se inserisce una stringa diversa dalle lettere N, S, E, O allo
        return input.equals("N") || input.equals("S") || input.equals("E") || input.equals("O");
    }

    //=========================================================================================================================

    //5. Modifica le coordinate del giocatore usando uno Switch
    static void eseguiMossa(String dir) {
        switch (dir) {
            case "N":
                yGiocatore++;
                break;
            case "S":
                yGiocatore--;
                break;
            case "E":
                xGiocatore++;
                break;
            case "O":
                xGiocatore--;
                break;
        }
    }

    //=========================================================================================================================

    //3. Ritorna vero (true) se le coordinate coincidono
    static boolean controllaVittoria() {
        return (xGiocatore == xTesoro && yGiocatore == yTesoro);
    }
}
