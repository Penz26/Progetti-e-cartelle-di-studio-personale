#Le classi possono ereditare da altri classi attributi metodi ecc

class Animal:   #Classe Padre
                #in questa classe vengono raggruppate tutte le cose che hanno in comune le classi figlie
                #così per evitare di modificare in un secondo momento in tutte le classi
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):   #Classe figlio di Animal
    #Ovviamente possono avere dei loro metodi e attributi che li distinguono dalle altre classi
    #Possono anche sovrascrivere metodi e attributi che ereditano come con eat()
    def run(self):
        print("This rabbit is running")
    def eat(self):
        print("This rabbbit is eating")

class Fish(Animal):   #Classe figlio di Animal
    #Ovviamente possono avere dei loro metodi e attributi che li distinguono dalle altre classi
    
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):   #Classe figlio di Animal
    #Ovviamente possono avere dei loro metodi e attributi che li distinguono dalle altre classi

    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)     #essendo una classe figlia avrà l'attributo alive
rabbit.eat()            #avendo sovrascritto la funzione eat nella classe rabbit ci darà un messaggio diverso
fish.eat()              
hawk.sleep()

#-------------------------------------------------------------------------------------------------------------

#L'eredità può anche essere a più livelli come per esempio

class Organism: #Classe Nonno
    alive = True

class Animal(Organism): #Classe Padre
    def eat(self):
        print("This animal is eating")

class Dog(Animal):  #Classe Figlio
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

#----------------------------------------------------------------------------------------------------------------------

#Eredità multipla: quando una classe figlia eredita da più di una classe Padre

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")


class Mouse(Prey):
    pass

class Cat(Predator):
    pass

class Bird(Prey,Predator):  #essendo gli uccelli sia prede che predatori ereditano da entrambe le classi
    pass

mouse = Mouse()
cat = Cat()
bird = Bird()

mouse.flee()
Cat.hunt()
bird.hunt()         #di conseguenza avrà sia i metodi di Prey(flee) e di Predator(hunt)
bird.flee()















