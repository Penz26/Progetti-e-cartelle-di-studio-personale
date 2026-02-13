import os
import shutil #libreria che ci permette di eliminare cartella con dei file al loro interno

with open("elima.txt", "w") as eliminare:
    eliminare.write("File da eliminare")

os.mkdir("cartella_vuota")

#os.remove("elima.txt")  Come negli altri casi visto che stiamo lavorando con un file all' interno della cartella dobbiamo solo mettere il nome del file invece che l'intero percorso
file = "elima.txt"
path = "cartella_vuota"
try:
    os.remove(file) #per rimuovere solo file
    #os.remove(path) se provassimo a cancellare una cartella con questo comando ci darebbe Permission Error
    os.rmdir(path)  #per rimuovere la cartella, LA CARTELLA PERO' NON DEVE CONTENERE FILE
    shutil.rmtree("cartella non vuota")
except FileNotFoundError:
    print("Il file non esiste")
except PermissionError:
    print("Non hai i permessi per rimuovere ciò")
except OSError:
    print("non puoi usare os.rmdir per eliminare un cartella con dei file")
else:
    print(f"{file} è stato eliminato")
    print(f"{path} è stata eliminata")
    print("Cartella non vuota eliminata")