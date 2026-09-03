import java.util.List;

public class UtilsNegozio {
    public static double calcolaValoreTotale(List<Prodotto> lista) {
        double totale = 0;
        for (Prodotto p : lista) {
            totale += p.getPrezzo();
        }
        return totale;
    }

    public static Prodotto cercaPerTitolo(List<Prodotto> lista, String titolo) {
        for (Prodotto p : lista) {
            if (p.getTitolo().equalsIgnoreCase(titolo)) {
                return p;
            }
        }
        return null;
    }
}