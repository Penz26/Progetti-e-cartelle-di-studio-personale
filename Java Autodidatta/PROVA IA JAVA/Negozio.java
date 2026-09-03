import java.util.ArrayList;
import java.util.List;

public class Negozio {
    private List<Prodotto> prodotti;
    private List<Cliente> clienti;

    public Negozio() {
        this.prodotti = new ArrayList<>();
        this.clienti = new ArrayList<>();
    }

    public void aggiungiProdotto(Prodotto p) {
        prodotti.add(p);
    }

    public void rimuoviProdotto(Prodotto p) {
        prodotti.remove(p);
    }

    public void registraCliente(Cliente c) {
        clienti.add(c);
    }

    public void mostraProdotti() {
        System.out.println("Prodotti disponibili:");
        for (Prodotto p : prodotti) {
            System.out.println(p.descrizione());
        }
    }

    public List<Prodotto> getProdotti() {
        return prodotti;
    }
}