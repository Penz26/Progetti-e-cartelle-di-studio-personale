import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Creazione prodotti
        CD cd1 = new CD("Album1", 2020, 15.99, "Artista1", 12);
        CD cd2 = new CD("Album2", 2021, 12.99, "Artista2", 10);
        Videogioco vg1 = new Videogioco("Gioco1", 2022, 49.99, "PC", "Avventura");
        Videogioco vg2 = new Videogioco("Gioco2", 2023, 59.99, "PlayStation", "Azione");

        // Creazione negozio
        Negozio negozio = new Negozio();
        negozio.aggiungiProdotto(cd1);
        negozio.aggiungiProdotto(cd2);
        negozio.aggiungiProdotto(vg1);
        negozio.aggiungiProdotto(vg2);

        // Registrazione cliente
        Cliente cliente = new Cliente("Marco", 1);
        negozio.registraCliente(cliente);

        // Simulazione acquisti
        cliente.acquistaProdotto(cd1);
        cliente.acquistaProdotto(vg1);

        // Mostra prodotti
        negozio.mostraProdotti();

        // Visualizza acquisti cliente
        cliente.visualizzaAcquisti();

        // Uso metodo statico
        List<Prodotto> prodotti = negozio.getProdotti();
        double totale = UtilsNegozio.calcolaValoreTotale(prodotti);
        System.out.println("Valore totale dei prodotti: " + totale + "€");

        // Cerca per titolo
        Prodotto trovato = UtilsNegozio.cercaPerTitolo(prodotti, "Gioco1");
        if (trovato != null) {
            System.out.println("Prodotto trovato: " + trovato.descrizione());
        }
    }
}