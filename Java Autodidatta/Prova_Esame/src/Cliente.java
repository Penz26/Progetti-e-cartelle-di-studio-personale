public class Cliente {
    private String nome;
    private int id;

    public Cliente(String nome, int id){
        this.nome = nome;
        this.id = id;
    }

    //Metodi Getter

    public String get_nome(){
        return nome;
    }

    public int get_id(){
        return id;
    }

    //Metodi Setter

    public void set_nome(String nome){
        this.nome = nome;
    }

    public void set_id(int id){
        this.id = id;
    }

    //Metodi

    public void acquistaProdotto(){
        System.out.println("Il cliente " + nome + " ha acquistato un prodotto");
        //Aggiungere il prodotto acquistato alla lista dei prodotti acquistati dal cliente
        
    }

    public void visualizzaAcquisti(){

    }
}
