public class Videogioco extends Prodotto {
    private String piattaforma;
    private String genere;

    public Videogioco(String titolo, int anno, double prezzo, String piattaforma, String genere) {
        super(titolo, anno, prezzo);
        this.piattaforma = piattaforma;
        this.genere = genere;
    }

    public String getPiattaforma() {
        return piattaforma;
    }

    public void setPiattaforma(String piattaforma) {
        this.piattaforma = piattaforma;
    }

    public String getGenere() {
        return genere;
    }

    public void setGenere(String genere) {
        this.genere = genere;
    }

    @Override
    public String descrizione() {
        return super.descrizione() + ", Piattaforma: " + piattaforma + ", Genere: " + genere;
    }
}