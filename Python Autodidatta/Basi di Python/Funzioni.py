#Funzioni = un blocco di codice che viene eseguito solo quando chiamato
#definizione di una funzione quelli all'interno delle () sono PARAMETRI
#possono anche essere diversi dal nome originale della variabile usata come argomento
def Hello(name, last_name, age):   
    print("Hello " + name + " " + last_name)
    print("You are", age)
    print("Have a Nice Day")

my_name = "Manuel"
my_last_name = "Bernardelli"
my_age = 19
Hello(my_name, my_last_name, my_age)    #quello che viene passato ad una funzione si chiama ARGOMENTO

#return statement (affermazione) = con questo statement la funzione manda valori/oggetti
#indietro alla chiamata, questi valori sono detti 

def multiply(number1, number2):
    result = number1 * number2
    return result

x = multiply(6,8)
print(x)

print()

#Argomenti parole-chiave = argomenti preceduti da un identificatore quando li passiamo a una funzione
#       l'ordine degli argomenti non ci interessa, a differenza di argomenti posizionali
#       Python riconosce il nome degli argomenti che la nostra funzione riceve

#ESEMPIO DI UNA FUNZIONE CHE UTILIZZA ARGOMENTI POSIZIONALI

def hello(first,middle,last):
    print(f"Hello nome: {first} cognome: {middle} soprannome: ({last})")

hello("Manuel","Bernardelli","Penna")  #la posizione degli argomenti importa per il senso logico del passaggio

#invece se usiamo argomenti parole-chiave

def salute(first,middle,last):
    print(f"Ciao {first} {middle} {last}")

salute(last = 19, middle = "Bernardelli", first = "Manuel")

print()

#Chiamate di funzioni annidate = chiamate di funzioni all'interno di altre chiamate di funzioni
#le chiamate avvengono in ordine in base alla successione delle parentesi come in matematica (da quella più interna a quella più esterna)
#valori ritornati vengono usati come argomenti per altre chiamate di funzioni più esterne

print(round(abs(float(input("Inserisci un nome intero positivo: ")))))   #ESENPIO ESTREMO NON CONSIGLIATO PER BEST PRACTICES

print()

#Scope = la regione in cui una variabile è riconosciuta
#        una variabile è disponibile solamente all'interno della regione in cui è stata creata
#        una versione globale e una locale di una variabile possono essere create allo stesso momento

name = "Penna"
def display_name():
    name = "Manuel"   # è disponibile solo in questa funzione, ma se essa non esistesse verrebbe utilizzata quella globale
    print(name)
#Python segue la regola LEGB (Local, Enclosing, Global, Built-in)
#quindi prima usa quelle locali e successivamente se non esistono si parte con il tipo succesivo

display_name()
print(name) 

print()

#*args = parametro che incapsula tutti gli argomenti in una tupla
#        utile così che una funzione possa accettare una quantità variabile di argomenti

#Si può chiamare come si vuole args basta che abbia * davanti
def add(*numeri):
    sum = 0
    stuff = list(numeri)  #visto che le tuple non sono ordinate per poter attribuire una posizione a un valore e cambiarne l'ordine dobbiamo trasformale in liste
    stuff[0] = 0
    for i in stuff:  #se dovessimo stampare senza dover fare modifiche sui valori possiamo stampare normalmente
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9))

#kwargs = parametro che inpachetta tutti gli argomenti in un dizionario
#       = utile perchè così la funzione può accettare un numero variabile di chiavi argomento

#Si può chiamare in qualsiasi modo basta che ci sia ** davanti
def hello(**names):
    #print(f"Hello {names["first"]} {names["last"]}")
    print("Hello", end=" ")
    for key,value in names.items():   #itera per ogni coppia chiave-valore all'interno del dizionario
        print(value, end=" ")
hello(first = "Manuel",middle = "Motta" ,last = "Bernardelli")


#POSSIAMO ANCHE CHIAMARE UNA FUNZIONE CON UNA VARIABILE
#ESEMPIO

def Hello():
    print("Hello")


Hello()
hi = hello  #senza parentesi altrimenti staremmo returnando dalla funzione
hi()

#funziona anche con funzioni già implementate
#ciao = print
#ciao("Ciao sta funzionando come la funzione print")