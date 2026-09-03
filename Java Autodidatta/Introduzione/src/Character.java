public abstract class Character { 
    //Ogni classe ha un file proprio con lo stesso nome della classe

    //DI DEFAULT E' MEGLIO SETTARE COME PRIVATE TUTTE LE VARIABILI DI UNA CLASSE IN JAVA
    //COSI' CHE SI POSSANO VEDERE SOLO DA QUESTO FILE
    private String name;
    private String genre;
    private int hp;
    private int atk;
    private int lvl;


    // Costruttore della classe Character DEVONO AVERE IL NOME DELLA CLASSE E NON HANNO UN TIPO DI RITORNO
    Character(String name, String genre, int hp, int atk, int lvl){
        this.name = name;
        this.genre = genre;
        this.hp = hp;
        this.atk = atk;
        this.lvl = lvl;
    }


    //Metodi Getter, permettono di ottenere le informazioni delle variabili private della classe DA ALTRI FILE
    public String getName(){
        return this.name;
    }

    public String getGenre(){
        return this.genre;
    }

    public int getHp(){
        return this.hp;
    }

    public int getAtk(){
        return this.atk;
    }

    public int getLvl(){
        return this.lvl;
    }



    //Metodi Setter, permettono di settare i valori delle variabili durante l'esecuzione delle app DA ALTRI FILE
    public void setName(String name) {
        this.name = name;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public void setAtk(int atk) {
        this.atk = atk;
    }

    public void setLvl(int lvl) {
        this.lvl = lvl;
    }


    // Metodo che printa la scheda del personaggio
    // Le variabilii vengono prese da quelle dichiarate all'interno del costruttore
    void printSheet(){
        System.out.println("################# CHARACTER SHEET ##################");
        System.out.println("Name = " + this.name);
        System.out.println("Hp = " + this.hp);
        System.out.println("Gender = " + this.genre);
        System.out.println("Attack = " + this.atk);
        System.out.println("Level = " + this.lvl);
    }

    void attack(Character enemy){ // Passiamo l'istanza del personaggio che subisce l'attacco come parametro
        //Attacco del personaggio che attacca (this.atk)
        //Vita di chi subisce l'attacco (enemy.hp)
        if (enemy.hp - this.atk < 0){
            if (enemy.hp <=0){
                System.out.println(enemy.name + " è gia morto.");
            }else {
                enemy.hp = 0;
                System.out.println(this.name + " ha attaccato " + enemy.name);
                System.out.println(enemy.name + " è stato sconfitto! " + enemy.name + " ha 0 hp!");
            }
        }else{
            enemy.hp -= this.atk;
            System.out.println(this.name + " ha attaccato " + enemy.name + " e gli ha tolto " + this.atk + " hp!\nOra " + enemy.name + " ha " + enemy.hp + " hp!");
        }
    }

    abstract void useSpecialAbility(); //Metodo astratto, non ha un corpo, deve essere implementato nelle classi figlie che estendono questa classe padre

    //invece un metodo statico è un metodo che può essere chiamato senza creare un'istanza della classe, si chiama direttamente con il nome della classe, ad esempio Character.someStaticMethod()
    static void someStaticMethod() {
        System.out.println("This is a static method in the Character class.");
    }   
}