#Esercizio Meteo

temperatura=int(input("Inserisci la temperatura all' esterno: "))
stato=input("Inserisci lo stato del cielo (sole, nuvoloso, pioggia): ")

if temperatura >=20 and temperatura <=30 and stato == "sole":
    print("Ottimo tempo per uscire")

else:
    print("Il tempo non è dei migliori")

if stato == "nuvoloso" or "pioggia":
    print("Potrebbe essere necessario un ombrello")
