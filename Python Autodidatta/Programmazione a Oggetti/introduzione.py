#una classe è un progetto per creare oggetti possiamo dargli attributi,metodi (ovvero cosa può fare l'oggetto all'interno)
#Gli attributi sono le variabili di una classe
#I metodi sono le funzioni che appartengono alla classe

class Car:      

    wheels = 4 #variabile di classe ovvero di default per tutti gli oggetti all'interno della classe, quindi tutti gli oggetti avranno come wheels 4, ammenochè non venga cambiata per un oggetto in particolare
    def __init__(self,nome,make,model,year,color): #questo è il costruttore
        self.nome = nome     #questa è una variabile di istanza (può essere diversa per ogni oggeto creato)
        self.make = make     #questa è una variabile di istanza (può essere diversa per ogni oggeto creato)
        self.model = model   #questa è una variabile di istanza (può essere diversa per ogni oggeto creato)
        self.year = year     #questa è una variabile di istanza (può essere diversa per ogni oggeto creato)
        self.color = color   #questa è una variabile di istanza (può essere diversa per ogni oggeto creato)

    def drive(self): #con self si rivolge alla classe a cui è all'interno (Car)
        print("This " +self.model+ " is driving")
    
    def stop(self):
        print("This " +self.model+ " is stopped")

car_1 = Car("Prima Auto","Chevy","Corvette","2021","blue") #non dobbiamo passare nessun argomento per self perchè in Python va in automatico
print(car_1.nome)
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

car_2 = Car("Seconda Auto","Ford","Mustang","2022","red")

car_2.drive()
car_2.stop()

#se per esempio vogliamo aggiungere una moto all'interno di Car possiamo dargli a wheels valore 2 è varrà 2 solo per la moto
moto = Car("Moto Manuel","Fantic","Performance","2022","red&white")
moto.wheels = 2

print(moto.wheels)
print(Car.wheels)
print(car_1.wheels)
print(car_2.wheels)

print("----------------------------------------")
#possiamo anche cambiare la variabile di classe per tutte facendo
Car.wheels = 3
print("Moto", moto.wheels)
print("Classe Car", Car.wheels)
print("Car 1", car_1.wheels)
print("Car 2" ,car_2.wheels)

#PASSAGGIO DEI VALORI DEGLI ATTRIBUTI IN INPUT

make_input = input("Insert the maker of this car: ")
model_input = input("Insert the model of this car: ")
year_input = input("Insert the year of this car: ")
color_input = input("Insert the color of this car: ")

nome_scelto = input("Come vuoi salvare questa auto? ")

macchina_1 = Car(nome_scelto, make_input, model_input, year_input, color_input)
macchina_1.drive()
macchina_1.stop()
