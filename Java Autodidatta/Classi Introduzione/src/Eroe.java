public class Eroe extends Character {

    //UNA CLASSE FIGLIA E' UNA CLASSE CHE ESTENDE UNA CLASSE PADRE, QUINDI HA TUTTE LE CARATTERISTICHE DELLA CLASSE PADRE PIU' EVENTUALI CARATTERISTICHE AGGIUNTIVE
    //IN QUESTO CASO LA CLASSE FIGLIA HA TUTTE LE CARATTERISTICHE DELLA CLASSE CHARACTER PIU' L'ABILITA' SPECIALE

    //LA CLASSE GENITORE (Character) CHIAMATA ANCHE superCLASSE, HA UN COSTRUTTORE CHE INIZIALIZZA LE VARIABILI DELLA CLASSE PADRE, 
    //MENTRE LA CLASSE FIGLIA HA UN COSTRUTTORE CHE CHIAMA IL COSTRUTTORE DELLA CLASSE PADRE E INIZIALIZZA ANCHE LE VARIABILI SPECIFICHE DELLA CLASSE FIGLIA

    private String specialAbility;

    // Costruttore della classe Figlia, che chiama il costruttore della classe padre (Character)
    Eroe(String name, String genre, int hp, int atk, int lvl, String specialAbility) {
        super(name, genre, hp, atk, lvl); // Chiamata al costruttore della classe padre
        this.specialAbility = specialAbility; // Inizializzazione dell'attributo specifico di Figlia
    }

    // Getter per l'abilità speciale
    public String getSpecialAbility() {
        return this.specialAbility;
    }

    // Setter per l'abilità speciale
    public void setSpecialAbility(String specialAbility) {
        this.specialAbility = specialAbility;
    }
    
    //Puoi anche aggiungere metodi specifici per la classe Figlia, ad esempio un metodo per usare l'abilità speciale
    public void useSpecialAbility() {
        System.out.println(getName() + " usa l'abilità speciale: " + specialAbility);
    }


    //Metodo statico che appartiene alla classe e non agli oggetti, quindi può essere chiamato senza creare un'istanza della classe Figlia
    @Override //serve a sovrascrivere un metodo della classe padre, in questo caso il metodo toString() che serve a stampare le informazioni del personaggio
    public String toString() {
        return super.toString() + "\nSpecial Ability: " + specialAbility; // Chiama il toString() della classe padre e aggiunge l'abilità speciale
    }
}
