# Con un # viene aperto un commento su una linea

''' Con i tripli apici si apre
un commento multilinea '''
print("Hello World")
print(23)
print("26")

#type ci dice il tipo del dato che viene PRIMA stampato
print(type("26"))

nome = "Iacopo"
print(nome)
nome = "Ieri sono andato a sciare"
eta = 26
print(eta)

#Per far leggere un input al computer utilizziamo il comando input()
nome = input("Come ti chiami? ")
print(nome)
print(type(nome))

#Casting = tecnica per cambiare il tipo della variabile, con il comando int() (int sta solo per il tipo della variabile con cui vogliamo fare il casting)
eta= int(input("Quanti anni hai? "))
print(eta)
print(type(eta))

anno_nascita = int(input("In che anno sei nato? "))
print(anno_nascita)
print(type(anno_nascita))

#Per concatenare stringhe e variabili si utilizza "" + Nome_variabile + ""
print("Ciao " + nome + " piacere di conoscerti")
print("Hai " + str(eta) + " anni") 
#in questo caso il casting vale solo per questa linea perchè non è stato overscritto il tipo della variabile

