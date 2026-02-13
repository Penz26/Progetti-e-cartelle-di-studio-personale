#exceptions = eventi rilevati durante l'esecuzione che interrompono l'andamento del programma

#il codice proverà (try) questa porzione di codice perchè è considerato potenzialmente pericoloso
#se il codice sopra nel try provoca un errore l'except specifico di quell' errore, (o uno generale come except Exception), preverrà il fermasi del programma 
try:
    numeratore = int(input("Inserisci un numero da dividere: "))
    denominatore = int(input("Inserisci un numero per cui dividere: "))
    result = numeratore/denominatore
except ZeroDivisionError as e:   #succedere quando si prova a dividere per 0
    print(f"Non puoi dividere per 0, IDIOTA! Codice Errore: {e}")
except ValueError as e: #succede quando il valore inserito non è conforme al tipo di variabile
    print(f"Devi inserire solo numeri. Codice Errore: {e}")
#except Exception as e: #viene usato alla fine se non si riesce a rilevare un errore specifico, NOT GOOD PRACTICE
    #print("Something went wrong")
else:  #se non rivela alcun errore fa quello al suo interno
    print(result)
finally: #il blocco di codice all'interno del finally viene eseguito sempre, sia che venga rilevato oppure no un errore utile per chiudere file
    print("Questo verrà sempre stampato")

