#Venv = ambienti virtuali Isolati
#       è un modulo integrato in python che crea ambienti virtuali isolati
#       Un ambiente virtuale contiene le proprie librerie
#       E ogni ambiente usa in maniera esclusiva le sue librerie, anche se sono presenti librerie globali


#Come CREARE un venv
python -m venv "nome"



#PERCORSO DI INSTALLAZIONE (dove viene specificato):
#IN C:\users\marco\venv




#Per poter essere utilizzato dobbiamo attivarlo
source nome_venv/bin/activate


#dopo averlo attivato noi saremo dentro il venv (si vede perchè c'è il prefisso "nome" davanti)

#per DISATTIVARLO scriviamo
deactivate
#il prefisso scomparirà e si tornerà alla cartella di base

#Per installare pacchetti in venv:
#(con il venv attivato)

pip install "requests"

#OPPURE CON UN FILE REQUIREMENTS

#I pacchetti vengono installati SOLO in questo ambiente
#Andranno installati solo in questo ambiente, andranno installati ogni volta
#che si apre un nuovo progetto venv

#Per esportare le dipendenze si crea un file con tutte le librerie:
pip freeze > requirements.txt
#Questo file elenca tutte le librerie installate e le scrive nel file
#“requirements.txt” alla posizione corrente

#Per condividere il progetto
#1 Condividi il file requirements.txt
#NON CONDIVIDERE LA CARTELLA DEL PROGETTO
#2 Chi riceve il progetto esegue: pip install -r requirements.txt



