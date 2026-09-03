public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Ciao, sono una classe!");

        //Creazione di due istanze della classe Character
        Character pg1 = new Eroe("Manuel", "Maschio", 100, 99, 69, "Fireball");
        Character pg2 = new Eroe("Iacopo", "Maschio", 100, 80, 45, "Ice Shield");


        System.out.println(pg1.getName());
        System.out.println(pg2.getName());

        pg1.printSheet();
        System.err.println();
        pg2.printSheet();
        System.err.println();

        //Il personaggio pg1 attacca pg2
        pg1.attack(pg2);
        //Il personaggio pg2 attacca pg1
        pg2.attack(pg1);
        pg1.attack(pg2);
        pg1.attack(pg2);
        pg1.attack(pg2);
        pg1.attack(pg2);

    }
}
