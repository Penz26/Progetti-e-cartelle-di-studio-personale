#copyfile() = copia i contenuti di un file
#copy() = copyfile() + modalità di permessi + la destinazione può essere una directory
#copy2() = copy() + copia i metadati (data e ora della creazione/modifica del file)

#TUTTE E 3 LE FUNZIONI HANNO GLI STESSI ARGOMENTI (source e destination)
import shutil

shutil.copyfile("test.txt","copy.txt") #sorgente e destinazione come argomenti
                                        # se siamo nella cartella e vogliamo spostare la copia all'interno della stessa cartella in cui siamo
                                        #possiamo mettere direttamente solo il nome del file nella destinazione
                                        #altrimenti se il file che copiamo non è nella cartella in cui stiamo lavorando dobbiamo mettere il percorso
                                        #stessa roba per la destinazione
