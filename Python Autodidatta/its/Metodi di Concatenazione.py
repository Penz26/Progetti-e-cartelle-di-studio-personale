#Metodi di Concatenazione

nome = "Iacopo"
eta = 26

#con il + serve fare il casting perchè concatena SOLO Stringhe
print("Mi chiamo " + nome + " e ho " +str(eta) + " anni")

#con la , non serve fare il casting perchè concatena OGNI tipo di variabile
print("Mi chiamo" , nome , "e ho" , eta , "anni")

#con la f davanti a tutto (formatted) formatta da solo tutto
print(f"Mi chiamo {nome} e ho {eta} anni")
