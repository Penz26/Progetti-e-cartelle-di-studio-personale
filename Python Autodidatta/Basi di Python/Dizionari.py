#Dizionari: una collezione di coppie chiave:valore non ordinate e che possono essere cambiate
#veloce perchè usano l'hashing che ci permette di accedere a un valore in modo veloce

capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing" ,
    "Russia": "Moscow"
    }

#Per aggiungere o modificare qualcosa all'interno del dizionario utiliziamo .update
capitals.update({"Germany": "Berlin"}) 
capitals.update({"USA": "Las Vegas"})

#per cancellare una coppia all'interno del dizionario utilizziamo .pop
capitals.pop("China")

#per cancellare tutto da un dizionario usiamo .clear
#capitals.clear()


print(capitals.get("Germany"), "\n")  #va a vedere se all'interno del dizionario c'è o meno un valore a quella chiave (STAMPA Berlin)
print(capitals.keys(), "\n")          #stampa solo le chiavi della lista, stampa: dict_keys(['USA', 'India', 'Russia', 'Germany']) 
print(capitals.values(), "\n")        #stampa solo i valori della lista,  stampa: dict_values(['Las Vegas', 'New Delhi', 'Moscow', 'Berlin']) 
print(capitals.items(), "\n")         #stampa tutti i valori della lista, stampa: dict_items([('USA', 'Las Vegas'), ('India', 'New Delhi'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])

#per stampare tutti i valori di una lista possiamo usare anche un ciclo for

for key,value in capitals.items():
    print(key, value)

print()

for i in capitals: #se diamo solo un valore come indice lui stamperà solo la chiave (USA, India, Russia, Germany)
    print(i)