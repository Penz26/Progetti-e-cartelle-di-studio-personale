#module = un file contenente codice python. Può contenere funzioni, classi, etc
    # usato nella programmazione modulare, che consiste nel dividere un programma in parti

#Consiste nel creare un file con funzioni,classi etc che potranno essere utilizzate in altri file
#Esempio
#Creiamo un file messages in cui mettiamo del codice
#Per eseguirlo in questo file ci basterà importare messages
import messages as msg

#si può anche importare solo le funzioni che desideriamo utilizzare senza dover importare tutto il file
from messages import hello,somma

msg.hello()
msg.somma()

#Con from ... import non ci servirà più scrivere il nome del file prima delle funzioni
hello()
somma()

#per avere un insight su tutti i moduli predefiniti di python fare:
#help("modules")

