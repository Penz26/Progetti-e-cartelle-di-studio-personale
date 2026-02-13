#daemon thread = un thread che viene eseguito in background, non importante per il programma se è in esecuzione
#                il programma NON ASPETTERA' che i daemon threads finiscano per uscire
#                non deamon-threads non possono essere normalmente uccisi, rimangono in vita fin quando l' obbiettivo non è stato compleatato
#
#                esempi: task in background, aspettare input, processi lunghi

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Sei entrato da ",count, "secondi")
        print()

x = threading.Thread(target=timer, daemon=True) #Per rendere un thread normale in thread daemon basta mettere questa flag
x.start()

#possiamo anche trasformare un thread normale in un deamon thread 
#ATTENZIONE PERO' NON POSSIAMO TRASFORMARLO IN DEAMON THREAD SE E' GIA' IN ESECUZIONE

#x.setDaemon(True)
#print(x.isDaemon())

answer = input("Do you wish to exit? ")
if answer.lower() == "yes":
    exit




