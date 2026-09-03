public class CD extends Prodotto {
    private String artista;
    private int numeroTracce;

    public CD(String titolo, int anno, double prezzo, String artista, int numeroTracce) {
        super(titolo, anno, prezzo);
        this.artista = artista;
        this.numeroTracce = numeroTracce;
    }

    public String getArtista() {
        return artista;
    }

    public void setArtista(String artista) {
        this.artista = artista;
    }

    public int getNumeroTracce() {
        return numeroTracce;
    }

    public void setNumeroTracce(int numeroTracce) {
        this.numeroTracce = numeroTracce;
    }

    @Override
    public String descrizione() {
        return super.descrizione() + ", Artista: " + artista + ", Numero Tracce: " + numeroTracce;
    }
}