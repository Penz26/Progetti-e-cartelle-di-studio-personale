#Dizionari, sono simili alle liste ma la chiave identificativa non è un numero ma bensì una stringa

dati_personali = {"nome": "Manuel" , "cognome": "Bernardelli"}

print(dati_personali) #stampa  {'nome': 'Manuel', 'cognome': 'Bernardelli'}

#mentre per stampare un singolo valore si va a chiamare il valore con la rispettiva chiave

print(dati_personali["nome"]) #stampa Manuel

#per MODIFICARE un valore di una chiave del dizionario mettiamo  la chiave = al nuovo valore
dati_personali["nome"] = "Alberto"
print(dati_personali["nome"])

#per AGGIUNGERE una chiave e un suo valore facciamo così:

dati_personali["colore_preferito"] = "Rosso"
print(dati_personali["colore_preferito"])

'''Chiedere 3 volte (con un ciclo) nome artista, numero album fatti e genere di 3 artisti diversi
e aggiungere ogni artista (dizionario) ad una lista di artisti'''

list_artists = []
new_artist = {} 
for x in range(3):
       #la dichiarazione va inserita all' interno altrimenti gli elementi ogni volta si sostituiscono
    new_artist["nome"] = input("Nome artista: ")
    new_artist["numero_album"] = int(input("Numero album: "))
    new_artist["genere"] = input("Genere: ")

    list_artists.append(new_artist)

print(list_artists)

artista = {"nome": "Kendrick", "Album": 4, "Genere": "Rap"}

#per stampare il dizionario dobbiamo scriverlo così, se stampassimo solo chiave stamperebbe solo la chiave
for chiave in artista:
    print("Chiave: ",chiave , "Valore :", artista[chiave])




'''Data una lista iniziale con delle ripetizioni, creare un dizionario delle frequenze aka un dizionario 
che come chiavi abbia gli elementi della lista e come valore il numero di volte che appare quell' elemento all' interno della lista

this_week_foods = ["Chili", "Poke", "Pizza", "Poke", "Kebab", "Kebab", "Kebab"]
food_frequency = {}

for food in this_week_foods:    #fa una copia della lista che passa di elemento in elemento ad ogni inizio di ciclo
    if food in food_frequency:  #se l'elemento della lista di adesso è già presente nella lista della frequenza aumento di uno il suo counter
        food_frequency[food] +=1  
    else:                       #altrimenti lo mette a 1, quindi all'inizio la prima volta che viene trovato questo cibo passerà per forza per questa interazione e quindi la crea
        food_frequency[food] = 1   #'Chili ': 1

print(food_frequency)'''