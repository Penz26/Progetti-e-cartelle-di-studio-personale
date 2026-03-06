#Previene a un utente di creare un oggetto di una classe
#+ obbliga un utente a sovrascrivere un metodo astratto in una classe figlia


#classe astratta = una classe che contiene uno o più metodi astratti
#metodo astratto = un metodo che ha una dichiarazione ma non una implementazione

#Per poter creare classi e metodi astratti dobbiamo importare dalla libreria ABC (ABSTRACT), abstractmethod

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod #con questo diciamo alle classi figlie che creeremo che dovranno
                    #sovrascrivere/implementare questo metodo altrimenti non le lasceremo inizializzare
    def go(self):
        pass
    
    @abstractmethod #stessa cosa per questo metodo, tutte le classi figlie dovranno avere anche questo metodo
    def stop(self):
        pass

#Se facessimo così, quindi non sovrascriviamo il metodo go ci darà un errore di implementazione
#è un buon modo per verificare che non ci stiamo dimenticando nulla nelle classi figlie
#class Car(Vehicle):
#    pass
#Errore per non aver implementato il metodo:
#Can't instantiate abstract class Car without an implementation for abstract method 'nome_metodo'

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("The car has stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle has stopped")

car1 = Car()
car1.go()
car1.stop()

motorcycle1 = Motorcycle()
motorcycle1.go()
motorcycle1.stop()

