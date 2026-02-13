import random as rm
while True:
    choices = ["rock", "paper", "scissors"]

    computer = rm.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock, papaer or scissors? ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Pareggio")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hai perso")
        elif computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hai vinto")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hai vinto")
        elif computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hai perso")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hai perso")
        elif computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hai vinto")

    play_again = input("Play again? Y/N ").upper()

    if play_again != "Y":
        break
print("Bye")


