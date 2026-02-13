#zip(*iterables) = aggrega elementi da due o più iterabili (liste,tuple,set. etc)
#                  crea un oggetto zip con coppia di elementi conservati dentro una tupla per ogni elemento


usernames = ["Bro", "Dude", "Mister"]
passwords = ["1234", "qwerty", "Milan"]
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
users = zip(usernames, passwords) #così escono come tuple senza casting

for i in users:
    print(i)

#Accoppia gli elementi in base alla loro posizione, 0 con 0, 1 con 1, 2 con 2
#('Bro', '1234')
#('Dude', 'qwerty')
#('Mister', 'Milan')

#Possiamo castare lo zip creato in chiavi e valori di un dizionario come qua

dizionario = dict(zip(usernames, passwords))
for key, value in dizionario.items():
    print(key + ": " + value)

dati = zip(usernames, passwords, login_date)
for i in dati:
    print(i)


