#If, elif, else

nome=input("Come ti chiami? ")

if nome == "Iacopo":
    print("Sei il facilitatore di Python!")
else:
    print("Non sei il facilitatore")

'''se non viene scritto Iacopo, esattamente come
viene specificato nell'if, risulterà false'''


# >, <, >=, <=, ==, != Operatori di Comparazione Standard

'''Chiedere all'utente quanti anni ha, se ha almeno 18 anni
stampare "Puoi entrare in Disco!", se l'utente ha meno di 18 anni
stampare "Stai Fuori!!!" '''

eta=int(input("Quanti anni hai? "))

if eta>=18:
    print("Puoi entrare in Disco!")

if eta<18:
    print("Stai fuori!")

'''Chiedere all'utente di quale stato vuole sapere la capitale
e poi stampare la capitale. (farlo almeno di 4 Stati)'''

Stato=input("Di quale Stato vuoi sapere la capitale: ")

#If else annidati, continua a controllare finchè non la trova
#quando la trova esce senza controllare il resto


if Stato == "Italia":
    print("Roma")
else:
    if Stato == "Spagna":
        print("Madrid")
    else:
        if Stato == "Germania":
            print("Berlino")
        else:
            if Stato == "Francia":
                print("Parigi")
            else:
                print("Sei un clown")




if Stato == "Italia":
    print("La capitale è Roma")
elif Stato == "Spagna":           #Gli elif solitamente vengono usati quando 
    print("La capitale è Madrid") #le condizioni si escludono
elif Stato == "Germania":         #non utilizziamo if else annidati
    print("La capitale è Berlino")
elif Stato == "Francia":
    print("La capitale è Parigi")
else:                             #in tutti gli altri casi fai questo
    print("Non conosco la capitale")



'''Scrivere un programma che chieda all'utente due numeri
e l'operazione che vuole fare (+,-,/,*) e stampare il risultato.
Se l'utente inserisce un'operazione inesistente deve essere avvisato che ha inserito un'operazione errata'''

numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
operazione = input("Inserisci il tipo di operazione da svolgere (+ , - , * , / , **)")

if operazione == "+":
    print("Il risultato di" , numero1 ," + " , numero2 ," è " , numero1+numero2)
elif operazione == "-":
    print("Il risultato di" , numero1 ," - " , numero2 ," è " , numero1-numero2)
elif operazione == "*":
    print("Il risultato di" , numero1 ," * " , numero2 ," è " , numero1*numero2)
elif operazione == "/":
    print("Il risultato di" , numero1 ," / " , numero2 ," è " , numero1/numero2)
elif operazione == "**":
    print("Il risultato di" , numero1 ," ** " , numero2 ," è " , numero1**numero2)
else:
    print("Operatore non valido")




    
