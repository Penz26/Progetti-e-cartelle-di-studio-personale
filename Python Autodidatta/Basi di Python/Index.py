#operatore index [] 
#dà accesso alla sequenza in un elemento (str,list,tuples)

name = "manuel bernardelli"

if (name[0].islower()):     #va a vedere se la prima lettera [0] è in lowercase
    name = name.capitalize()

first_name = name[0:6].upper()  #la posizione da cui parte di default è sempre 0 di conseguenza si può omettere [:6]
last_name = name[7:].upper()    #parte dalla settima posizione e va fino alla fine
last_character = name[-1]       #prende l'ultimo character di una stringa
print(first_name) 
print(last_name) 
print(last_character)


