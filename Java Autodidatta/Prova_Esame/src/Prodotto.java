public class Prodotto {
    private String titolo;
    private int anno;
    private double prezzo;

    //Costruttore padre
    public Prodotto(String titolo, int anno, double prezzo){
        this.titolo = titolo;
        this.anno = anno;
        this.prezzo = prezzo;
    }


    //Metodi Getter

    public String get_titolo(){
        return titolo;
    }

    public int get_anno(){
        return anno;
    }

    public double get_prezzo(){
        return prezzo;
    }


    //Metodi Setter

    public void set_titolo(String titolo){
        this.titolo = titolo;
    }

    public void set_anno(int anno){
        this.anno = anno;
    }

    public void set_prezzo(double prezzo){
        this.prezzo = prezzo;
    }


    //Stampa la descrizione del prodotto
    public void descrizione(){
        System.out.println("Questo prodotto si chiama: " + this.titolo + " è uscito il " + this.anno + " e costava " + this.prezzo);
    }
}
