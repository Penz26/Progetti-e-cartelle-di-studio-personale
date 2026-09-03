public class Prodotto {
    private String titolo;
    private int anno;
    private double prezzo;

    public Prodotto(String titolo, int anno, double prezzo) {
        this.titolo = titolo;
        this.anno = anno;
        this.prezzo = prezzo;
    }

    public String getTitolo() {
        return titolo;
    }

    public void setTitolo(String titolo) {
        this.titolo = titolo;
    }

    public int getAnno() {
        return anno;
    }

    public void setAnno(int anno) {
        this.anno = anno;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public String descrizione() {
        return "Titolo: " + titolo + ", Anno: " + anno + ", Prezzo: " + prezzo + "€";
    }
}