#Librerie = è un file o un gruppo di file contenente codice già scritto da altri
#           esistono librerie built-in ovvero proprie di python (Os,Math,Random,Time,DateTime)
#           oppure esterne come numpy,pandas ecc 
#           che hanno bisogno di una loro installazione prima di installarlo
#Ci sono 3 modi 
#import totale
#import di una specifica funzione all'interno della libreria
#oppure importare tutte le funzioni in modo da non dover mettere il nome della libreria davanti alla funzione importata


#LIBRERIE RANDOM E TIME
import random as rd, time

numero = rd.randint(0,10)
tentativo = input("Prova ad indovinare il numero misterioso da 1 a 10: ")

if numero == tentativo:
    print("Sei molto fortunato e hai trovato il numero random")
else:
    print("Non hai indovinato il numero random")
    for seconds in range(2,0,-1):
        print(seconds)
        time.sleep(1)

#LIBRERIA Math

from math import sqrt, pi

risultato_sqrt = sqrt(16)
print(f"La radice quadrata di 16 è {risultato_sqrt}")

#Calcola l'area di un cerchio con raggio 5

raggio = 5

area = pi * (raggio**2)
print(f"L'area del cerchio  con raggio 55 è {area}")

    