#Higher Order Function = una funzione che:
#                        1. accetta funzioni come argomenti
#                        2. ritorna una funzione
# 
#                        (In python si può fare perchè le funzioni sono trattate come oggetti)
#


#1. accetta funzioni come argomenti
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def Hello(func):   #la funzione di ordine più alto accetta come argomento func che sarà il nome della funzione che decideremo di passare
    text = func("Hello")
    print(text)

Hello(loud)     #passiamo il nome della funzione come argomento



#2. ritorna una funzione
def divisor(x): 
    def dividend(y):    #alla prima chiamata 
        return y/x      #salta questo
    return dividend

divide = divisor(2) #chiama divisor così da passargli il numero che diventa la x, salta la parte della funzione dividend ediventa dividend
print(divide(10))   #e visto che poi divide è diventato dividend può passare l'ultimo argomento (y) così da poterlo poi printare 