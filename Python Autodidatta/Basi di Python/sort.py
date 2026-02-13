# sort() method = usato per liste
# sorted() function = usato con iterabili


# Metodo Sort, usato per le liste
students = ["Squiddy", "Marco", "Manuel"]
students.sort()

for i in students:
    print(i)

print()
# possiamo anche ordinare al contrario

students.sort(reverse = True)

for i in students:
    print(i)

print()
#Per altri iterabili come per esempio tuple usiamo la funzione sorted()
objects = (1, 10, 30, 100, 54)
sorted_objects = sorted(objects) # anche qua possiamo invertire l'ordine con reverse = True

for i in sorted_objects:
    print(i)




studenti = [("manuel", "F", 89),
            ("Laura", "B", 43),
            ("Marco", "A", 51),
            ("Luca", "C", 21),
            ]

grade = lambda grades:grades[1] # di per sè da sola non fa nulla, serve la chiamata di una funzione come sort
# che va a collegare la funzione alla lista da cui va a prendere i dati per eseguire i comandi

#studenti = (("manuel", "F", 89),
#            ("Laura", "B", 43),
#            ("Marco", "A", 51),
#            ("Luca", "C", 21),
#            )   



print()

studenti.sort(key = grade) # con key decidiamo per cosa vogliamo ordinare il nostro iterabile

# oppure con la funzione sorted(), che usiamo quando non dobbiamo ordinare una lista ma altri iterabili come una tupla di tuple come: 
#sorted_studenti = sorted(studenti, key = grade)

for i in studenti:
    print(i)

#Quindi in pratica grades diventa la prima tupla della lista, e poi con l'indice 1 va a prendere l'elemento alla posizione 1 nella tupla




