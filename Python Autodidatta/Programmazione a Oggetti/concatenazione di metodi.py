#concatenazione di metodi = chiamare molteplici metodi in sequenza
                            # ogni chiamata fa un azione sullo stesso oggetto e ritorna se stessa

class Car:
    def turn_on(self):
        print("You start the engine")
        return self     #Per poter concatenare metodi sequenzialmente dobbiamo fare return self per ogni metodo

    def drive(self):
        print("You drive the car")
        return self     #Per poter concatenare metodi sequenzialmente dobbiamo fare return self per ogni metodo
    
    def brake(self):
        print("You step on the brakes")
        return self     #Per poter concatenare metodi sequenzialmente dobbiamo fare return self per ogni metodo
    
    def turn_off(self):
        print("You turn off the engine")
        return self     #Per poter concatenare metodi sequenzialmente dobbiamo fare return self per ogni metodo
car = Car()

#Concatenazione di metodi (il programma li legge da sinistra a destra)
car.turn_on().drive()

car.brake().turn_off()

#Per facilitare la lettura del codice se abbiamo molte concatenazioni è meglio scrivere così

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

