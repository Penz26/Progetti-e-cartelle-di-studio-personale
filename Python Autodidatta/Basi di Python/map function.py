#map() = applica una funzione ad ogni oggetto in una iterabile (liste, tuple, etc...)
#
#
#map(funzione,iterabile)

store = [("Shirt", 20.00),
         ("Pants", 35.00),
         ("Kicks", 60.00),
         ("Jeans", 35.00),
         ("Chain", 20.00), 
        ]

to_euros = lambda data: (data[0],round(data[1]*0.82,2)) #prende dalla lista store le tuple e non cambia il primo valore [0] ,
#                                                        ma il secondo valore [1] viene moltiplicato per 0.82 per la  conversione 
#                                                        ,tiene i dati in una tupla con le () iniziali

#Per il contrario dopo aver cambiato da dollari in euro
#to_dollars = lambda data: (data[0],data[1]/0.82)


store_euros = list(map(to_euros,store)) #usa la funzione to_euros, sull' iterabile store (effettuando il collegamento tra funzione e lista) 
#e fa diventare la variabile una lista con list() davanti con all'interno le tuple all' interno di to_euros

for i in store_euros:
    print(i)


