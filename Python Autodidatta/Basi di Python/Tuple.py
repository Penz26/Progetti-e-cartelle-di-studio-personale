#Le tuple sono una collezione di dati ordinati e non cambiabili
#utilizzate per raggruppare dati in relazione

student = ("Bro" ,21, "Male")

print(student.count("Bro"))  #conta quante volte appare questo valore all' interno della tupla
print(student.index("Male")) #stampa a quale indice della tupla è il valore 0 = "Bro" , 1 = 21 , 2 = "Male"

for x in student:
    print(x)  #stampa uno ad uno i valori della tupla

print()
if "Male" in student:
    print("Lo Studente è di genere maschile")