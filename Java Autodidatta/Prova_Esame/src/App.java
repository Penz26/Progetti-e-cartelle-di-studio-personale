import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner input = new Scanner(System.in);
        CD primocd = new CD("Currents", 2016, 20.00, "Tame Impala", 18);
        primocd.descrizione();

        CD secondocd = new CD("Tpab", 2015, 20.00, "Kendrick Lamar", 18);
        secondocd.descrizione();

        Videogioco primoVideogioco = new Videogioco("Hollow Knight", 2015, 20, "PC", "Platoform Soul");
        primoVideogioco.descrizione();

        Videogioco secondoVideogioco = new Videogioco("Hollow Knight SilkSong", 2025, 20, "PC", "Platoform Soul");
        secondoVideogioco.descrizione();

        System.out.print("Inserisci il nome del cliente: ");
        String primo_nome = input.nextLine();

        System.out.print("Inserisci l'id del cliente: ");
        int primo_id = input.nextInt();

        Cliente primo_cliente = new Cliente(primo_nome, primo_id);
        primo_cliente.acquistaProdotto();

    }
}
