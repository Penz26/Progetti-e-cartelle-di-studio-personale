import os #importa il sistema operativo

percorso = "C:\\Users\\marco\\Desktop\\test.txt" #mettere doppie \\ per la sequenza di uscita se il file contiene \ al suo interno

if os.path.exists(percorso):   #va a vedere se il percorso esiste
    print("That location exists!")
    if os.path.isfile(percorso): #verifica se il percorso identifica un file
        print("That is a file")
    elif os.path.isdir(percorso): #verifica se è una directory (cartelle)
        print("That is a directory!")
else:
    print("That location doesn't exist!") #nel caso il file non esiste, o è stato eliminato, fa ciò

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PER LEGGERE UN FILE PRIMA DOBBIAMO SPECIFICARE QUALE FILE E DI CONSEGUENZA IL PERCORSO IN CUI DEVE CERCARE IL FILE
#with open("C:\\Users\\marco\\Desktop\\test.txt"):

#NEL CASO SI STIA LAVORANDO IN UNA CARTELLA BASTERA' FARE COSI'#with open("test.txt") as file: #salviamo il file che dobbiamo aprire in una variabile (file in questo caso)
                                # e lo chiude automaticamente con with open
with open("test.txt") as file:
    print(file.read())

#print(file.closed) #restituirà True se il file è stato chiuso

#CIO' PERO' NON GESTISCE ALCUNE ECCEZIONI, QUINDI E' MEGLIO INSERIRE IL CODICE IN UN TRY,EXCEPTION

try:
    with open("test.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PER SCRIVERE UN FILE
text = input("Cosa vuoi scrivere all'interno del file: ")
with open("test2.txt", "w") as file:   #DI DEFAULT IL SECONDO PARAMETRO DI WITH OPEN E' READ, ("r") MA PER SCRIVERE DOBBIAMO METTERE WRITE ("w")
    file.write(text + "\n")  #si può mandare a capo dopo una stringa facendo + "\n"

#il file viene sostituito (overwrite) nel caso ne esista già uno all'interno della cartella/percorso
#per aggiungere qualcosa al file usiamo APPEND ("a") come modalità nel with open

firma = input("Inserisci la tua firma: ")
with open("test2.txt", "a") as file:
    file.write(firma)
    file.write("\n") #altro modo per mandare a capo

#PER CREARE UNA CARTELLA INVECE

os.mkdir("Cartella inutile")

#PER CREARE CARTELLE ANNIDATE

percorso_completo = "progetto/output/report"

# Crea tutte le cartelle intermedie se non esistono
os.makedirs(percorso_completo, exist_ok=True) #exist_ok serve a fare un controllo sull'esistenza di un file/cartella prima che venga creato
                                                #così da evitare di creare file/cartelle già esistenti

print(f"Percorso '{percorso_completo}' pronto.")