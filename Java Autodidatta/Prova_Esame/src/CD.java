public class CD extends Prodotto{
    private String artista;
    private int numero_tracce;


    //Costruttore di CD (include anche gli attributi del padre (Prodotto))
    public CD (String titolo, int anno, double prezzo, String artista, int numero_tracce){
        super(titolo, anno, prezzo); //Richiama il costruttore del padre
        this.artista = artista;
        this.numero_tracce = numero_tracce;
    }

    @Override
    public void descrizione(){
        System.out.println("Questo CD si chiama " + get_titolo() + " è uscito nel " + get_anno() + " costava "+ get_prezzo() + ". \nL'ha registrato " + artista + " ha " + numero_tracce + " tracce.");
    }


}
