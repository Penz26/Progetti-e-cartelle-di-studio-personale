#filter() = crea una collezione di elementi da un iterabile per cui una funzione ritorna true

# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data: data[1] >= 18    #Cerchiamo in base a questo criterio, che diventerà il nostro filtro all' interno del filter()

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)



