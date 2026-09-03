#Funzioni = blocchi di codice che vengono usate per riusare un codice che serve in più parti del programma

def saluta():     #definizione di una funzione
    print("SALUTO")

def SalutaConNome(nome_1):  #quello che arriva ad una funzione si chiama PARAMETRO  
    print("Ciao", nome_1)

nome = "Manuel"
SalutaConNome(nome)  #quello che viene passato ad una funzione si chiama ARGOMENTO
SalutaConNome("Giovanna")
saluta()
saluta()
saluta()

def AuguriCompleanno(nome,eta):   #assegna in ordine in base a quello che viene scritto prima
    print("Tanti auguri", nome, "per i tuoi", eta, "anni")

eta = 10
AuguriCompleanno(nome,eta)   #assegna in ordine nella funzione in base a quello che viene scritto prima




#Esercizio gestione numeri


def sommaNumbers(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def AverageNumbers(sum,nums):
    return sum / len(nums)

def Menu():
    print("------AZIONI DISPONIBILI------\n")
    print("Add - per aggiungere un numero alla lista\n")
    print("#################################################\n")
    print("Sum - per sapere la somma dei numeri\n")
    print("#################################################\n")
    print("Avg - per sapere la media dei numeri\n")

numbers = [8, 10, 24, 3, 9]

while True:
    
    Menu()
    #Scelta dell'azione dell' utente
    action = input("Inserisci l'azione che vuoi eseguire: ")
    
    #gestore azioni

    if action == "Add":
        new_number = int("Inserisci il numero che vuoi aggiungere: ")
        numbers.append(new_number)

    elif action == "Sum":
        somma_dei_numeri= sommaNumbers(numbers)
        print("La somma dei numeri è", somma_dei_numeri)
        print()
        print()


    elif action == "Avg":
        average = AverageNumbers(somma_dei_numeri,numbers)
        print("La media è", average)
        print()
        print()
        
    else:
        print("Azione non trovata")
        print()
        print()
