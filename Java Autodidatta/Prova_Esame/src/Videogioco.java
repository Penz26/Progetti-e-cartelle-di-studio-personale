public class Videogioco extends Prodotto{
    private String piattaforma;
    private String genere;

    //Costruttore di Videogioco (include anche gli attributi del padre (Prodotto))
    public Videogioco(String titolo, int anno, double prezzo, String piattaforma, String genere){
        super(titolo, anno, prezzo);
        this.piattaforma = piattaforma;
        this.genere = genere;
    }

    @Override
    public void descrizione(){
        System.out.println("Questo Videogioco si chiama " + get_titolo() + " è uscito nel " + get_anno() + " costava "+ get_prezzo() + ". \nSi gioca su " + piattaforma + " appartiene al  " + genere + " genere.");
    }
}
