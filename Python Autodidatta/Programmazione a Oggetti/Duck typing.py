#Duck typing = al computer non interessa di che "classe" sia l'oggetto.
#Gli interessa solo che l'oggetto abbia i metodi o gli attributi richiesti in quel momento.
#"Se cammina come un'anatra e starnazza come un'anatra, allora per me è un'anatra."

#Perché è utile?

#Flessibilità estrema: Puoi scrivere funzioni che lavorano con oggetti molto diversi tra loro 
#senza dover creare complicate gerarchie di ereditarietà.

#Codice più snello: Non devi dichiarare continuamente i tipi di dato.

#Polimorfismo naturale: Il comportamento cambia a seconda dell'oggetto passato, purché quell'oggetto "sappia cosa fare".


class Duck():
    def walk(self):
        print("This duck is walking ")
    def talk(self):
        print("This duck is quacking ")

class Chicken():
    def walk(self):
        print("This chicken is walking ")
    def talk(self):
        print("This chicken is clucking ")

class Person():
    def catch(self,animale): #il tipo di classe non viene verificato affinchè il numero di metodi/attributi sono presenti
        animale.walk()
        animale.talk()
        print("You caught the animal")

duck_1 = Duck()
chicken_1 = Chicken()
person_1 = Person()

person_1.catch(duck_1)
print()
person_1.catch(chicken_1)





