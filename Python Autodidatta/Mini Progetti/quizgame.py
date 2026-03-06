#--------------------------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 0 #contatore che ci servirà per stampare le 4 risposte della domanda rispettiva

    for key in questions:
        print("------------------")
        print(key) #Stampa una domanda alla volta, prende SOLO LE CHIAVI
        for i in options[question_num]:
            print()
            print(i) #stampa le risposte di quella specifica domanda

        while True:  #continua all'infinito finchè non viene fermato
            try:
                guess = input("Enter (A,B,C,or D): ").upper()

                if guess.isdigit(): #se nel guess viene inserito un numero (digit) allora facciamo rilevare ValueError
                    raise ValueError
                if guess in ["A","B","C","D"]: #se il guess rientra nella lista di questi valori allora fermiamo il ciclo
                    break
                else:
                    print("Insert only A,B,C or D")

            except ValueError as e:  #se inserirà valori che non sono stringhe o non rientrano nella lista di valori corretti allora darà ValueError
                print("Insert only letters (A,B,C,D), Error: ", e)

        guesses.append(guess)

        correct_guesses += check_answers(questions.get(key),guess) #con questions.get va a vedere se per quella chiave corrisponde un valore
                                                                    #in questo caso il valore che corrisponde alla chiave al primo ciclo ("Who created Python? ") sarebbe "A"
                                                                    #quindi poi va a vedere se la nostra guess è uguale a questo valore

        question_num += 1 #lo aumentiamo di 1 così andiamo avanti con le altre 4 risposte ma della domanda dopo
    display_score(correct_guesses,guesses)
#--------------------------------------------
def check_answers(answer, guess):
    
    if answer == guess:
        print("Correct!")
        return 1 #ritorna 1 per 1 punto che verrà aggiunto alla variabile correct_guesses
    else:
        print("Wrong!")
        return 0 #ritorna 0 per 0 punti che verrà aggiunto alla variabile correct_guesses

#--------------------------------------------
def display_score(correct_guesses,guesses):
    print("---------------------------")
    print("Results")
    print("---------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=", ") #STAMPA I VALORI DELLA DOMANDA DI CUI CORRISPONDE LA CHIAVE (i)
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i,end=", ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is " , score, "%")
#--------------------------------------------
def play_again():
    response = input("Do you want to play again? (Y/N)").upper()


    if response == "Y":
        return True
    else:
        return False


#In questo dizionario terremo come CHIAVE le domande e come VALORE la lettera che corrisponde alla risposta esatta
questions = {
    "Who created Python? ": "A",
    "What year was Python created? ": "B",
    "Python is tributed to which comedy group? ": "C",
    "Is the Earth round? ": "A"
}

#in questa lista 2D teniamo le 4 risposte a ciascuna domanda (sono le liste all'interno della lista principale)
options = [["A: Guido van Rossum","B: Elon Musk","C: Bill Gates", "D: Mark Zuckerberg"],
           ["A: 1989","B: 1991","C: 2000", "D: 2016"],
           ["A: Lonely Island","B: Smosh","C: Monty Python", "D: SNL"],
           ["A: True","B: False","C: sometimes", "D: What's Earth?"]]

new_game()

while play_again(): #Se ritorna True (che è di default quindi non dobbiamo inserirlo in questa condizione) rifacciamo il gioco
    new_game()

print("Bye")
