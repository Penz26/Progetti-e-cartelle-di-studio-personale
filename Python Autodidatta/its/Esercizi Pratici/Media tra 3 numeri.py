#L'esercizio chiede di chiedere all' utente 3 numeri e trovarne la media

'''Iniziamo chiedendo i numeri che ci serviranno per fare la media, essendo il tipo predefinito delle variabili string dobbiamo trasformarle in int con il casting'''

numero_1 = int(input("Inserisci il primo numero "))
numero_2 = int(input("Inserisci il secondo numero "))
numero_3 = int(input("Inserisci il terzo numero "))

#Dividiamo la loro somma per 3 essendo i numeri solo 3
print((numero_1 + numero_2 + numero_3)/3)
