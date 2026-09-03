#Exception =    un blocco di codice che prevede un evento che interromperebbe lo scorrere del programma
#               (ZeroDivisionError, TypeError, ValueError, NameError, IndexError, KeyError)
#               1. try,   2. except,  3. finally


#Try , exception e finally vengono utilizzati in casi considerati pericolosi
#come inserimento di dati da parte dell' utente

#Try - si usa quando quella parte di codice è considerata pericolosa e non si sa
#se possa provocare un errore, (non viene trovato il file da leggere, il valore della variabile 
#non  combacia con il tipo della variabile dichiarato)

#------------------------------------------------------------------------------

#Except - si usa appunto per prevedere il tipo di errore che si potrebbe incontrare
#per far sì che il programma nonostante abbia trovato un errore possa continuare
#e l' utente può essere notificato con una stampa a schermo in base all'errore che ha incontrato


#------------------------------------------------------------------------------

#Finally - viene eseguito sempre anche se non viene incontrato un errore
#viene solitamente utilizzato per:
#chiudere un file che è stato aperto
#chiudere connessioni di rete o Database per evitare perdite di risorse

#-------------------------------------------------------------------------------
#1° ESEMPIO - ZeroDivisionError - ValueError

#L'utente in questo caso può anche inserire una stringa al posto di un numero
#e ciò ci darebbe un ValueError
#ovvero che il valore inserito dall'utente non coincide con il tipo della variabile (es: int,float ecc)
#mentre se l'utente segue la direzione del programma ma inserisce 0
#ci uscirebbe l'errore ZeroDivisionError, ovvero un errore causato dalla divisione per 0 di un numero

'''number = int(input("Enter a number: "))
print(1 / number)'''

#per fixarlo facciamo:

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("Non puoi dividere un numero per 0!")
except ValueError:
    print("Inserisci solo numeri!") 
finally:                            #si esegue sempre anche se non ci sono eccezioni
    print("Do some cleanup here")

#per considerare tutte le eccezioni possiamo scrivere
#except Exception:
#ma non è considerata come good practice di un buon programmatore
#ovvero che si funziona ma non è consigliato perchè non si può specificare
#nel print a schermo un messaggio adatto per uno specifico errore

print()

#2° ESEMPIO - NameError

#Se si cerca di stampare una variabile che non è stata dichiarata il codice ci darebbe un NameError
#print(x)

#per fixarlo:
'''
try:
    print(x)
except NameError:
    print("La variabile che hai cercato di stampare non è stat dichiarata")
'''

print()

#3° ESEMPIO - IndexError

#Se invece viene inserito un indice in una lista che è al di fuori degli indici presenti
#in una lista il programma ci darebbe IndexError
#lista = [1, 2, 3, 4, 5]
#print(lista[5])

#Per Fixarlo

lista = [1, 2, 3, 4, 5]
print(lista)
try:
    index = int(input("Inserisci l'indice del numero che vuoi vedere: "))
    print(lista[index])
except IndexError:
    print("L'indice che hai inserito è al di fuori della lista")
    print("Ricordati che in informatica si parte sempre da 0 con gli indici")
except ValueError:     #in questo caso ci sarebbe anche il caso che l'utente inserisca 
    print("Inserisci solo numeri!")

print()

#4° ESEMPIO - KeyError

#Se l'utente cerca di stampare un valore di un dizionario chiamando una chiave
#non esistente il programma ci darà KeyError
#dizionario = {"Nome": "Manuel", "Cognome": "Bernardelli", "Eta": 19}
#print(dizionario[Indirizzo])

#Per Fixarlo

dizionario = {"Nome": "Manuel", "Cognome": "Bernardelli", "Eta": 19}
print(dizionario)

try:
    indice = input("Inserisci la chiave del dizionario di cui vuoi printare il valore: ")
    print(dizionario[indice])
except KeyError:
    print("La chiave che hai inserito non è presente all'interno del dizionario")



