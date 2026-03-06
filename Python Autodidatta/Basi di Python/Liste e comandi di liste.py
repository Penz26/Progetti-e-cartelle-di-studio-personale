# le liste vengono usate per conservare più valori in una singola variabile

food = ["Pizza", "Pasta"]  #per dichiarare una lista scriviamo il nome della variabile e la mettiamo uguale a []

print(food[1]) #come ogni cosa in Python si inizia a contare da 0

for i in food:  #stampa tutti i valori all'interno di quella lista, perchà la i funge da copia della lista
    print(i)

#per aggiungere alla fine della lista un valore utilizziamo .appendd
food.append("Ice Cream")

#per rimuovere un elemento in particolare  utiliizamo .remove
food.remove("Pasta")

#per rimuovere l'elemento alla fine utilizziamo .pop
food.pop()

#per inserire/sostituire un valore all'interno di una lista in una determinata posizione utillizamo .insert
food.insert(0,"Cake")

#per ordinare alfabeticamente  una lista automaticamente
food.sort()

#per cancellare tutti gli elementi di una lista utilizziamo .clear
food.clear()
