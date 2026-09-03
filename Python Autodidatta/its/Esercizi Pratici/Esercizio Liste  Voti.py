'''Partendo da una lista vuota:
Chiedere all'utente quanti voti vuole inserire e poi chiedere il singolo
voto tante volte quante il numero che ha inserito l'utente all'inizio.
Infine stampare la lista'''

grades = []
times = int(input("Quante voti vuoi inserire: "))
index = 0

while index < times:
    grades.append(float(input("Inserisci il voto: ")))  #In questo modo aggiunge alla lista l'input inserito dall'utente
    index+=1

print("I tuoi voti sono: ", grades)


'''Partendo dalla lista dell'esercizio precedente calcolare la somma di tutti i numeri
all'interno e stamparla (senza usare funzioni apposite). E anche la Media'''

index = 0
somma= 0
while index < times:
    somma += grades[index]
    index+=1

print("La somma dei numeri all'interno della lista è: ", somma)
print("La media dei numeri all'interno è: ", somma/times)




