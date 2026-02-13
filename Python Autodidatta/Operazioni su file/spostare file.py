import os

source = "test2.txt"   #File che si vuole spostare
destination = "C:\\Users\\marco\\Desktop\\test.txt" #Destinazione del file (alla fine del percorso va messo anche il nome che gli si vuole dare al file, in questo caso lo chiamerà test.txt)

try:
    if os.path.exists(destination): #controlla se un file con quello stesso nome esiste già
        print("There is already a file there!")
    else:
        os.replace(source,destination)  #con replace il file/cartella va a spostarsi nel percorso che è stato specificato 
        print(f"{source} è stato spostato")

except FileNotFoundError:
    print(f"{source} was not found")
