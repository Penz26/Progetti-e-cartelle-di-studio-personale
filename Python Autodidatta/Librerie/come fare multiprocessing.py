#***************************************
#
#Python MultiProcessing
#
#***************************************
#multiprocessing = eseguire task in parallelo su diversi core della cpu, bypassa il GIL
#                  multiprocessing = migliore per cpu bound task (gran utilizzo di cpu)
#                  multithreading = migliore per io bound task (aspettano)

#Usa il Multithreading se il tuo codice deve fare una richiesta web o leggere un file mentre l'utente continua a usare i bottoni della GUI. 
# I thread sono perfetti per mantenere la GUI reattiva.

#Usa il Multiprocessing se il tuo codice deve fare calcoli matematici che durano 30 secondi. 
# Se usassi i thread, il GIL bloccherebbe comunque tutto; con il multiprocessing, il calcolo va su un altro core e la GUI resta fluida.

from multiprocessing import Process, cpu_count
import time

def counter(number):
    count = 0
    while count < number:
        count += 1
def main():
    print(cpu_count()) #stampa quanti core abbiamo sulla nostra cpu

    a = Process(target=counter, args=(10000000,))
    a.start()

    b = Process(target=counter, args=(10000000,))
    b.start()



    print("Finished in ", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()




