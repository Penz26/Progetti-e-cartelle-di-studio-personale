'''Slicing, ottenere da una stringa di una variabile altre variabili
con il contenuto della stringa di prima
[posizione d'inizio: posizione di fine: unità di avanzamento ]
[start:stop:step]
Lo start è incluso mentre lo stop è escluso
Quindi per vedere la 5° lettera bisogna mettere come stop 6

'''

name = "Manuel Bernardelli"

first_name = name[0:6:1] # se si parte da 0 si può omettere [:6:1] lo step invece è di default 1 quindi si può omettere in questo caso [:6:]
last_name = name[7:18:1] # se si va fino alla fine della stringa si può omettere lo stop [7::]
reversed_name = name[::-1] #parte dall' inizio alla fine girando con step negativo la stringa
print(first_name)
print(last_name)
print(reversed_name)

website = "http://google.com"

slice = slice(7,-4) 
#permette di partire dal carattere come primo argomento e arrivare fino al carattere con index negativo corrispondente a quello del secondo argomento
#in questo caso l'indice in entrambi i casi parte da 1 e non da 0
print(website[slice])
print(name[slice])