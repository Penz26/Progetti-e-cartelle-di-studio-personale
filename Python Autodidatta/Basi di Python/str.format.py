#str.format() = metodo opzionale che da all'utente più controllo nel mostrare output


animal = "cow"
item = "moon"

#print("The {} jumped over {}".format("cow", "moon"))  #le {} sono placeholders che vanno a sostituirsi a gli argomenti di format
#print("The {1} jumped over {0}".format("animal", "item"))  #placeholders posizionali (partendo da 0) così l'ordine dei valori si inverte
#print("The {animal} jumped over {item}".format(animal = "cow", item = "moon")) #placeholders chiave-valore

text = "The {} jumped over the {}"

print(text.format(animal,item))

name = "Bro"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10} nice to meet you".format(name)) #aggiungiamo degli spazi vuoti dopo aver messo in output la variabile
print("Hello, my name is {:>10}".format(name)) #sposta a destra la variabile esposta
print("Hello, my name is {:^10}".format(name)) #centro la variabile esposta
print("Hello, my name is {}".format(name))

pi = 3.14159
number = 1000
print("The number pi is {:.2f}".format(pi)) #manda in output il numero con solo 2 numeri decimali ATTENZIONE ARROTONDA PURE(f alla fine sta per float quindi decimale)
print("The number is {:b}".format(number)) #manda in output il corrispondente numero binario
print("The number is {:o}".format(number)) #manda in output il corrispondente numero oct (ottadecimale)
print("The number is {:X}".format(number)) #manda in output il corrispondente numere EX (esadecimale)
print("The number is {:e}".format(number)) #manda in output il corrispondente numero nella sua notazione scientifica


