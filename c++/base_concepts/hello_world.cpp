#include <iostream> //Libreria che permette di usare i comandi di input ed output
using namespace std;  //Accorcia i comandi senza dover usare std::nome_comando

int main() {                  //Funzione principale
  cout << "Hello World\n";      //Ogni comando deve finire con ;

  cout << 3 + 3 << "\n";
  int n = 3;
  cout << "Il valore della variabile è: " << n <<".\n";


  return 0;                   //La funzione main deve sempre finire con un return 0
}
