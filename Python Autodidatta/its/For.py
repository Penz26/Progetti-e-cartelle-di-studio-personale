nomi = ["Marco", "Elisa", "Anna", "Luca"]
print("Esercizio 1")
for i in nomi:     #i crea una copia della lista e la stampa, ma non la può modificare
    print(i, end=" ")

numeri = [3, 10, 22, 5, 8, 13, 2]

print("\n")


print("Esercizio 2")
for num in numeri:
    if num % 2 == 0 :
        print(num, end=" ")

print("\n")


print("Esercizio 3")
for i in range(20,-1,-2):
    print(i, end=" ")

print("\n")


print("Esercizio 4")
numeri = [11, 99, 3, 42, 7, 102]
for i in numeri:
    if i == 11:
        max = 11
    elif i > max:
        max = i
print(max)
print("\n")


print("Esercizio 5\n")
frase = input("Inserisci una frase: ")
count = 0
for i in frase:
    if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() =="o" or i.lower() == "u":
        count+=1

print("Ci sono ", count , "vocali")

#secondo metodo
vocali = "AaEeIiOoUu"
count=0
for i in frase:
    if i in vocali:
        count+=1

print("Ci sono ", count , "vocali")

