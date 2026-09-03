lista_1 = ["M"]
lista_2 = ["Ciao"]


counter_1 = 0
for i in range(0,len(lista_1)):
    counter_1+=len(lista_1[i])

counter_2 = 0
for i in range(0,len(lista_2)):
    counter_2+=len(lista_2[i])

print(counter_1)
print(counter_2)

while counter_1 < counter_2:
    print("La lista 2 è più lunga")
    break

while counter_1 > counter_2:
    print("La lista 1 è più lunga")
    break