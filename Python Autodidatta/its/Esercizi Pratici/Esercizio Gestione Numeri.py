'''
Crea un programma che, partendo da una lista di numeri, abbia un menù in cui è possibile:
-stampare la lista
-aggiungere numero
-eliminare numero
-modificare un numero
-calcolare la somma dei numeri nella lista
-calcolare la media dei numeri nella lista
-sapere il numero più grande della lista
-sapere il numero più piccolo della lista
'''

#Almeno le ultime 4 operazioni devono essere fatte ognuna in una funzione diversa. 

def sommaNumbers(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def AverageNumbers(sum,nums):
    return sum / len(nums)

def CalcolaMin(nums):
    min = nums[0]
    for num in nums:
        if num < min:
            min = num

    print("Il numero più piccolo è ", min)

def CalcolaMax(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    print("Il numero più grande è ",max)

def NumberDelete(nums):
    numero_da_eliminare = input("Inserisci il numero che vuoi eliminare: ")

def NumbersChange(nums):
    numero_da_cambiare = input("Inserisci il numero che vuoi cambiare: ")
    scambio = input("Inserisci il numero con cui vuoi cambiarlo")

def Menu():
    print("------AZIONI DISPONIBILI------\n")
    print("Print - per stampare la lista")
    print("#################################################\n")
    print("Del - per eliminare un numero")
    print("#################################################\n")
    print("Change - per modificare un numero")
    print("#################################################\n")
    print("Max - per sapere il numero più grande della lista")
    print("#################################################\n")
    print("Min - per sapere il numero più piccolo della lista")
    print("#################################################\n")
    print("Add - per aggiungere un numero alla lista\n")
    print("#################################################\n")
    print("Sum - per sapere la somma dei numeri\n")
    print("#################################################\n")
    print("Avg - per sapere la media dei numeri\n")
    print("#################################################\n")
    print("Quit - per uscire dal menù")

numbers = [8, 10, 24, 3, 9]

while True:
    
    Menu()
    #Scelta dell'azione dell' utente
    action = input("Inserisci l'azione che vuoi eseguire: ")
    
    #gestore azioni

    if action == "Add":
        new_number = int("Inserisci il numero che vuoi aggiungere: ")
        numbers.append(new_number)
    elif action =="Print":
        print(numbers)
    elif action == "Del":
        NumberDelete(numbers)
    elif action == "Change":
        NumbersChange(numbers)
    elif action == "Max":
        CalcolaMax(numbers)

    elif action == "Min":
        CalcolaMin(numbers)
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