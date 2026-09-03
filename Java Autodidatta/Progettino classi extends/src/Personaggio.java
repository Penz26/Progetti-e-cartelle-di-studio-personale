public abstract class Personaggio {
    private int vita;
    private int attacco;
    private int difesa;
    private String nome;

    public Personaggio(String nome, int vita, int attacco, int difesa) {
        this.nome = nome;
        this.vita = vita;
        this.attacco = attacco;
        this.difesa = difesa;
    }

    // Getter
    public String getNome() {
        return nome;
    }

    public int getVita() {
        return vita;
    }

    public int getAttacco() {
        return attacco;
    }

    public int getDifesa() {
        return difesa;
    }

    // Setter per vita (necessario quando si subisce danno)
    public void setVita(int vita) {
        this.vita = Math.max(0, vita); // Non scendere sotto 0
    }

    // Metodo per calcolare il danno inflitto
    public int calcolaDanno() {
        // Danno base + variazione casuale (0-20% dell'attacco)
        int variazione = (int) (Math.random() * (this.attacco * 0.2));
        return this.attacco + variazione;
    }

    // Metodo per calcolare il danno ridotto dalla difesa
    public int subisciDanno(int dannoInflitto) {
        // La difesa riduce il danno
        int dannoFinale = Math.max(1, dannoInflitto - this.difesa / 2);
        return dannoFinale;
    }

    // Metodo per verificare se è vivo
    public boolean isVivo() {
        return vita > 0;
    }

    // Metodo astratto per l'azione del turno (attaccare o difendersi)
    public abstract String agisci();

    @Override
    public String toString() {
        return nome + " [Vita: " + vita + "/" + (nome.equals("Giocatore") ? 100 : 50) + "]";
    }
}
