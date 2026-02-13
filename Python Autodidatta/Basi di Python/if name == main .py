#*************************************
#
#if __name__ == "__main__"
#
#*************************************
#
#
#Perche?
#1. Il modulo può essere eseguito come un programma da solo
#2. Il modulo può essere importato e usato in altri moduli

#L' interprete di Python setta delle "variabili speciali", una di queste è __name__
#Python assegnerò la variabile speciale __name__ il valore __main__ se è il modulo iniziale che ha fatto partire
# quindi Python eseguirà il codice trovato dentro __main__

print(__name__) #essendo il file principale originario che stiamo facendo partire questo, uscirà __main__
import  Index
print(Index.__name__) #essendo questo il modulo importato uscirà il nome del file quindi Index

if __name__ == "__main__":
    print("Questo è il modulo originario")
else:
    print("Questo è il modulo secondario")


