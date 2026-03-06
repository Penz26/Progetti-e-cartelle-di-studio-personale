# Thread = è la più piccola unità di elaborazione che può essere gestita da uno scheduler del sistema operativo. 
#          È un'entità che vive all'interno di un processo e ne condivide le risorse, ma possiede una propria identità di esecuzione.
#          Ogni thread viene eseguito a turno così da arrivare alla Concorrenza

# Concurrency (Concorrenza): Su una CPU con un singolo core, il sistema operativo esegue il context switching (scambio di contesto) 
# così velocemente tra un thread e l'altro da dare l'illusione della simultaneità.


#In Python (specificamente nell'implementazione standard CPython), esiste il GIL (Global Interpreter Lock). 
# È un mutex che permette a un solo thread alla volta di eseguire il bytecode Python.

#Effetto: Anche su un PC con 16 core, un programma Python puramente computazionale (CPU-bound) non andrà più veloce usando i thread.

#Eccezione: I thread in Python sono utilissimi per operazioni I/O-bound (come richieste di rete o lettura di file), 
# dove il thread "rilascia" il lock mentre aspetta i dati, permettendo ad altri thread di lavorare.

#I thread servono a non far "Congelare" i programmi. Ecco due esempi comuni:

#In un browser (come Chrome): Mentre un thread scarica le immagini di una pagina pesante, un altro thread ti permette di continuare a scorrere la pagina o cliccare sui tasti senza che tutto si blocchi.

#In un videogioco: 
# Un thread si occupa di calcolare i movimenti dei nemici,  1
# uno di gestire il suono                                   2
# e un altro di disegnare la grafica sullo schermo.         3

#Processo: È un'unità di esecuzione indipendente. Ogni processo ha il suo spazio di indirizzamento virtuale privato. 
# Il sistema operativo garantisce che un processo non possa accedere alla memoria di un altro (isolamento), garantendo stabilità: 
# se un processo crasha, gli altri continuano a girare.

#Thread: È un'unità di esecuzione interna a un processo. Più thread appartenenti allo stesso processo condividono lo stesso spazio di indirizzamento. 
# Se un thread scrive in una zona di memoria, gli altri thread dello stesso processo vedono immediatamente la modifica. 
# Se un thread genera un segmentation fault, l'intero processo muore.

import threading
import time

print(threading.active_count()) #printa quanti thread ci sono in esecuzione
print(threading.enumerate())    #printa quali thread sono in esecuzione

def eat_breakfast():
    time.sleep(10)
    print("You ate breakfast")

def drink_coffe():
    time.sleep(5)
    print("You finished drinking coffe")

def study():
    time.sleep(20)
    print("You finished studying")

#Senza multithreading il codice farà una funzione una volta seguendo una scaletta
#eat_breakfast() #Prima chiama ed esegue il codice di questa funzione
#drink_coffe() # dopo aver finito il codice della funzione prima chiama ed esegue questo
#study() # e così via

#NOI INVECE VOGLIAMO FARLE FARE TUTTE ASSIEME IN CONCORRENZA
#COME SE STESSIMO FACENDO MULTITASKING

#E lo facciamo così
x = threading.Thread(target = eat_breakfast)
x.start()

y = threading.Thread(target = drink_coffe)
y.start()

z = threading.Thread(target = study)
z.start()

print(threading.active_count()) #printa quanti thread ci sono in esecuzione (in questo caso uscirà 4 perchè oltre ai 3 che si occupano delle funzioni 
#                               c'è ovviamente il Thread principale che non aspetta gli altri thread)
print(threading.enumerate())    #printa quali thread ci sono in esecuzione
print(time.perf_counter())      #printa quanto ci impiega in secondi il nostro mainthread


#SE INVECE VOGLIAMO CHE IL NOSTRO THREAD PRINCIPALE ASPETTI GLI ALTRI THREAD DOBBIAMO SPECIFICARLO CON join()
x.join()
y.join()
z.join()

print(threading.active_count()) #visto che ora i nostri thread lavorano tutti allo stesso momento e il nostro main thread li aspetta
#                               il nostro counter tornerà ad 1
print(time.perf_counter())