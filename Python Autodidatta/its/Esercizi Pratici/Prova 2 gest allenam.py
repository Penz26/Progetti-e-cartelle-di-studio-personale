choice = ""
workout_record = {}  #chiave = giorno
while choice.lower() != "quit":
    workout = {}
    print("#" * 60)
    print("\n")
    choice = input("Se vuoi aggiungere un workout inserisci 'Si' oppure 'No' se ti sei riposato altrimenti 'Quit' per uscire: ")
    if choice.lower() == "si":
        day = input("Che giorno ti sei allenato (01/01/20**): ")

        '''Se la giornata che ha inserito l'utente non esiste creiamo una lista
        per quel giorno all' interno del dizionario che ci tiene gli storici degli allenamenti(workout_record{}) con al suo interno
        l'allenamento che andiamo a inserire (workout{})'''

        if day not in workout_record:  
            workout_record[day] = []
        workout["Nome"] = input("\nInserisci l'esercizio: ")
        workout["Rep"] = input("\nInserisci il numero di rep: ")
        workout["Peso"] = input("\nInserisci il peso che hai sollevato: ")
        workout_record[day].append(workout)
        print("\n")

    elif choice.lower() == "no":
        day = input("Che giorno non ti sei allenato (01/01/20**): ")
        if day not in workout_record:
            workout_record[day] = []
        workout["Nome"] = "Riposo"
        workout["Rep"] = "/"
        workout["Peso"] = "/"
        workout_record[day].append(workout)
        print("\n")

    elif choice.lower() == "quit":
        print("Arrivederci")

    else:
        print("\n")
        print("#" * 60)
        print("Hai inserito un comando sbagliato, riprova \n")

print("\n")
print("#" * 60)
print("\n" ,workout_record)