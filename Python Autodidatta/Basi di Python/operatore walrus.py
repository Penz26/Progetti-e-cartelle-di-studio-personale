#Operatore di Wallrus :=

#Permette di assegnare un valore a una variabile come parte di un espressione più grande

#ESEMPIO
# foods = []
# while True:
#    food = input("What food do you like? ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while (food := input("What food do you like? ")) != "quit":  #assegna e fa il controllo sulla variabile allo stesso tempo
                                                             #RICORDARSI LE () ALTRIMENTI ASSEGNA TRUE OR FALSE ALLA VARIABILE  
    foods.append(food)

print(foods)