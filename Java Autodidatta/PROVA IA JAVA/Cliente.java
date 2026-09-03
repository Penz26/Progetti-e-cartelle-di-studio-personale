import java.util.ArrayList;
import java.util.List;

public class Cliente {
    private String nome;
    private int id;
    private List<Prodotto> acquisti;

    public Cliente(String nome, int id) {
        this.nome = nome;
        this.id = id;
        this.acquisti = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void acquistaProdotto(Prodotto p) {
        acquisti.add(p);
    }

    public void visualizzaAcquisti() {
        System.out.println("Acquisti di " + nome + ":");
        for (Prodotto p : acquisti) {
            System.out.println(p.descrizione());
        }
    }
}