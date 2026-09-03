public class GestioneCombattimento {
    
    // Avvio il combattimento tra due personaggi
    public static boolean combatti(Giocatore giocatore, Nemico nemico) {
        System.out.println("\n========== INIZIO BATTAGLIA ==========");
        System.out.println(giocatore.getNome() + " affronta " + nemico);
        System.out.println("=====================================\n");

        int turno = 1;
        
        while (giocatore.isVivo() && nemico.isVivo()) {
            System.out.println("\n--- TURNO " + turno + " ---");
            
            // Turno del giocatore
            String azioneGiocatore = giocatore.agisci();
            
            // Turno del nemico
            String azioneNemico = nemico.agisci();
            
            // Risoluzione del combattimento
            risolviTurno(giocatore, nemico, azioneGiocatore, azioneNemico);
            
            // Stampa lo stato dei combattenti
            stampaStatoCombattimento(giocatore, nemico);
            
            turno++;
            
            // Pausa tra i turni per migliore leggibilità
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        
        // Determina il vincitore
        if (giocatore.isVivo()) {
            System.out.println("\n========== VITTORIA! ==========");
            System.out.println(giocatore.getNome() + " ha sconfitto " + nemico.getNome());
            System.out.println("Vita rimanente: " + giocatore.getVita());
            return true;
        } else {
            System.out.println("\n========== SCONFITTA! ==========");
            System.out.println(nemico.getNome() + " ha sconfitto " + giocatore.getNome());
            return false;
        }
    }
    
    // Risolve il turno di battaglia
    private static void risolviTurno(Giocatore giocatore, Nemico nemico, 
                                      String azioneGiocatore, String azioneNemico) {
        
        // Calcola il danno del giocatore
        if (azioneGiocatore.equals("attacca")) {
            int dannoGiocatore = giocatore.calcolaDanno();
            int dannoSubito = nemico.subisciDanno(dannoGiocatore);
            System.out.println("» " + giocatore.getNome() + " infligge " + dannoSubito + " danni!");
            nemico.setVita(nemico.getVita() - dannoSubito);
        }
        
        // Calcola il danno del nemico
        if (azioneNemico.equals("attacca") && nemico.isVivo()) {
            int dannoNemico = nemico.calcolaDanno();
            int dannoSubito = giocatore.subisciDanno(dannoNemico);
            System.out.println("» " + nemico.getNome() + " infligge " + dannoSubito + " danni!");
            giocatore.setVita(giocatore.getVita() - dannoSubito);
        }
    }
    
    // Stampa lo stato dei combattenti
    private static void stampaStatoCombattimento(Giocatore giocatore, Nemico nemico) {
        System.out.println("\nStato:");
        System.out.println("  " + giocatore.getNome() + ": " + giocatore.getVita() + " HP");
        System.out.println("  " + nemico.getNome() + ": " + nemico.getVita() + " HP");
    }
    
    // Avvia l'arena con una serie di nemici progressivamente più forti
    public static void avviaArena(Giocatore giocatore) {
        int nemiciSconfitti = 0;
        int livelloNemico = 1;
        boolean continua = true;
        
        System.out.println("\n╔══════════════════════════════════════╗");
        System.out.println("║    BENVENUTO ALLA BATTLE ARENA!       ║");
        System.out.println("║ Sconfiggi quanti nemici riesci!       ║");
        System.out.println("╚══════════════════════════════════════╝\n");
        
        while (continua && giocatore.isVivo()) {
            Nemico nemico = new Nemico("Nemico Livello " + livelloNemico, livelloNemico);
            
            if (combatti(giocatore, nemico)) {
                nemiciSconfitti++;
                System.out.println("\nNemici sconfitti: " + nemiciSconfitti);
                
                // Guarigione parziale dopo la vittoria
                int guarigione = 20;
                giocatore.setVita(Math.min(100, giocatore.getVita() + guarigione));
                System.out.println("Guarigione: +" + guarigione + " HP (Vita totale: " + giocatore.getVita() + ")");
                
                // Aumenta difficoltà
                livelloNemico++;
                
                // Chiedi se continuare
                System.out.print("\nVuoi affrontare il prossimo nemico? (s/n): ");
                java.util.Scanner scanner = new java.util.Scanner(System.in);
                String risposta = scanner.nextLine().toLowerCase();
                continua = risposta.equals("s");
            } else {
                continua = false;
            }
        }
        
        // Risultato finale
        System.out.println("\n╔══════════════════════════════════════╗");
        System.out.println("║        FINE DELLA SFIDA!              ║");
        System.out.println("║ Nemici sconfitti: " + nemiciSconfitti);
        System.out.println("╚══════════════════════════════════════╝");
    }
}
