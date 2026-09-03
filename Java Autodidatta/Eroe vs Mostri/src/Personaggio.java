public class Personaggio {
    private String nome;
    private String classe;
    private int hp;
    private int atk;
    private boolean isAlive;

    //Metodi Getter
    public String getNome() {
        return this.nome;
    }

    public String getClasse() {
        return this.classe;
    }

    public int getHp() {
        return this.hp;
    }

    public int getAtk() {
        return this.atk;
    }

    public boolean isAlive() {
        return this.isAlive;
    }

    //Metodi Setter
    //Prendono in inserimento i valori da app.java e questo viene passato come argomento
    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setClasse(String classe) {
        this.classe = classe;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public void setAtk(int atk) {
        this.atk = atk;
    }

    public void setIsAlive(boolean isAlive) {
        this.isAlive = isAlive;
    }



    //COSTRUTTORE
    Personaggio(String nome, String classe, int hp, int atk) {
        this.nome = nome;
        this.classe = classe;
        this.hp = hp;
        this.atk = atk;
        this.isAlive = true;
    }

    void Stats(){
        System.out.println("Nome: " + this.nome);
        System.out.println("Classe: " + this.classe);
        System.out.println("HP: " + this.hp);
        System.out.println("ATK: " + this.atk);
    }
    void attack(Enemies nemico)
    {
        if(this.isAlive){
            System.out.println(this.nome + " attacca " + nemico.getNome() + " con " + this.atk + " punti danno.");
            nemico.setHp(nemico.getHp() - this.atk);
        }else{
            System.out.println(this.nome + " è morto e non può attaccare.");
        }
    }
}
