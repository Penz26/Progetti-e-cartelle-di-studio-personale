#set = collezione di valori non ordinati, non indicizzati. Niente valori duplicati
# non essendo indicizzati nella stampa i valori non hanno una posizione fissa
utensils = {"fork","spoon","knife","knife","knife"} #posso anche aggiungere altri "knife" ma non me li stamperà visto che non accetta duplicati
dishes = {"bowl","plate","cup","knife"}


#per aggiungere un elemento a un set usiamo .add

utensils.add("napkin")

# per rimuovere utilizziamo .remove

utensils.remove("fork")

#per svuotare un set utilizziamo .clear

#utensils.clear()

#per aggiungere a un set gli elementi di un altro set usiamo .update

dishes.update(utensils)

#per creare un nuovo set in cui ci sono gli elementi di entrambi i set usiamo .union

dinner_table = utensils.union(dishes)

#per vedere quali elementi sono presenti in una lista ma non nell'altra usiamo .difference

print(utensils.difference(dishes))

#per vedere cosa hanno in comune i 2 set usiamo .intersection

print(utensils.intersection(dishes))

for x in utensils:
    print(x)  