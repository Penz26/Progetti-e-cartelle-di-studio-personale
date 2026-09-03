public class Nemico extends Personaggio {
    private int livello;
    private int difesaAttiva;

    public Nemico(String nome, int livello) {
        // I nemici diventano più forti ad ogni livello
        super(nome, 30 + (livello * 15), 15 + (livello * 5), 5 + (livello * 2));
        this.livello = livello;
        this.difesaAttiva = 0;
    }

    public int getLivello() {
        return livello;
    }

    // Metodo per calcolare il danno con variazione maggiore per i nemici
    @Override
    public int calcolaDanno() {
        int variazione = (int) (Math.random() * (getAttacco() * 0.3));
        return getAttacco() + variazione;
    }

    // Azione di difesa per il nemico
    public void difenditi() {
        this.difesaAttiva = (int) (getDifesa() * 1.5);
    }

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
        resettaDifesaAttiva();
        return dannoFinale;
    }

    // IA del nemico: sceglie casualmente l'azione
    // I nemici di livello più alto hanno più probabilità di attaccare
    @Override
    public String agisci() {
        // Probabilità di attacco aumenta con il livello
        double probabilitaAttacco = 0.5 + (livello * 0.1); // Da 0.5 a 0.8
        probabilitaAttacco = Math.min(0.9, probabilitaAttacco); // Max 90%
        
        if (Math.random() < probabilitaAttacco) {
            System.out.println(getNome() + " attacca!");
            return "attacca";
        } else {
            System.out.println(getNome() + " si difende!");
            difenditi();
            return "difende";
        }
    }

    @Override
    public String toString() {
        return getNome() + " [Livello " + livello + ", Vita: " + getVita() + "]";
    }
}
