rows = int(input("Quante righe vuoi nel quadrato? "))
columns = int(input("Quante colonne vuoi nel quadrato? "))
symbol = input("Inserisci il simbolo con cui vuoi costruire il quadrato: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end="")  #alla fine della stampa
    print()
