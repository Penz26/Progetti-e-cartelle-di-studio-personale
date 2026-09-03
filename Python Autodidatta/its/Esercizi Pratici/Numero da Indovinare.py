import random  #libreria che ci permette di generare un numero randomico attraverso random.randint
secret = random.randint(1, 20) #per le funzioni importate scriviamo prima il nome della libreria più un punto che precede il comando da utilizzare
attempt = int(input("Prova ad indovinare il numero: "))  #è int SOLO per questa linea di conseguenza prossimamente può essere di tipo stringa in default
tries = 1
print(secret)
while secret != attempt:     #!= va ad indicare il diverso, quindi fino a che il numero non è uguale continua ad entrare nel ciclo
    if attempt < secret:
        print("Sbagliato: " +str(attempt) + " è più piccolo del numero segreto.")
        attempt = input("Se vuoi uscire dal gioco puoi scrivere 'Quit' altrimenti premi invio per continuare ")
        if attempt == "Quit":
            break
        attempt =int(input("Riprova: "))
    else:
        print("Sbagliato: " +str(attempt) + " è più grande del numero segreto.")
        attempt = input("Se vuoi uscire dal gioco puoi scrivere 'Quit' altrimenti premi invio per continuare ")
        if attempt == "Quit":
            break
        attempt =int(input("Riprova: "))
        
    if tries == 6:
        break
    tries +=1
    
if attempt == secret:
    print("Complimenti! Hai indovinato il numero in " + str(tries) +" tentativi!!!")
elif tries == 6:
    print("Hai esaurito il numero di tentativi")
else:
    print("Hai abbandonato il gioco")


