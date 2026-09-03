#Le liste conservano una lista di valori al suo interno
#e si dichiara così

fav_artists = ["Tame Impala", "Kendrick Lamar", "Clipse", "JID"]
print(fav_artists)
print("I miei artisti preferiti sono: " , fav_artists)

#Si può stampare anche un solo elemento della lista mettendo tra [] il numero a cui
#corrisponde il valore all' interno delle liste

print(fav_artists[2]) #stamperà i Clipse, perchè si parte sempre da 0 a contare

print(len(fav_artists)) #ci stamperà a schermo quanti valori abbiamo all' interno della lista

i = 0
while i < len(fav_artists): #essendo len(artists) 4 dovremo mettere < e non <= uguale perchè l'identificatore di ogni dato parte da 0
    print(i, "-" , fav_artists[i])
    i+=1


#Per aggiungere degli elementi a una lista utilizziamo il comando .append dopo il nome della lista
votes = []
votes.append(8)

#Per eliminare un elemento da una lista utilizziamo del

del fav_artists[2]

#Per vedere se un elemento è in una lista facciamo così

if "Clipse" in fav_artists:
    print("Clipse è nella lista")
else:
    print("clipse non è nella lista")
