import random #genera numeri pseudo randomici

x = random.randint(1,6)  #genera numeri randomici da 1 a 3
y = random.random() #genera un numero in virgola mobile

print(x)
print(y)

myList = ["rock","paper","scissors"]
z = random.choice(myList)  #fa una scelta randomica tra i valori della lista

print(z)

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

print(f"Scala {cards}")

random.shuffle(cards) #mescola gli elementi all'interno della lista

print(f"Carte mescolate {cards}")


