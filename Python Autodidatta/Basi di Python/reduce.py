# reduce() = applicauna funzione a un iterabile e lo riduce a un singolo valore comulativo
#            performa la funzione sui primi 2 elementi e la ripete finchè non rimane 1 valore
#
# reduce(funzione, iterabile)
import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y,letters) #Prende la prima lettera (x) e la unisce alla seconda (y)"HE", poi ripete finchè non ne rimane una "HEL" poi "HELL" infine "HELLO" 

print(word)

#Altro esempio (Calcolo Fattoriale)

numbers = [5, 4, 3, 2, 1]
fact = functools.reduce(lambda numero_1, numero_2: numero_1 * numero_2, numbers) #Prende 5 (numero_1) lo moltiplica per 4 (numero_2) che fa 20
                                                                                 #, poi 20 che diventa numero_1 viene moltiplicato per 3 che numero_2
                                                                                 # e così via
print(fact)