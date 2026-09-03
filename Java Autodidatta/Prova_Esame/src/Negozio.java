public class Negozio {
    private Prodotto[] prodotti;
    private Cliente[] clienti;
    public Negozio(Prodotto[] prodotti, Cliente[] clienti){
        this.prodotti = prodotti;
        this.clienti = clienti;
    }

    //Metodi

    public void aggiungiProdotto(Prodotto prodotto){
        for(int i = 0; i < 1000; i++){
            if(prodotti[i] == null){
                prodotti[i] = prodotto;
            }
        }
    }

    public void rimuoviProdotto(){
        
    }

    public void registracliente(Cliente cliente){
        for(int i = 0; i < 1000; i++){
            if (clienti[i] == null){
                clienti[i] = cliente;
            }
        }
    }

    public void mostraprodotti(){
        for(int i = 0; i < prodotti.length; i++){
            System.out.println(prodotti[i]);
        }
    }

    public void mostraclienti(){
        for(int i = 0; i < clienti.length; i++){
            System.out.println(clienti[i]);
        }
    }

}
