#Cicli While
#Il While ripete le operazioni al suo interno FINCHE' la condizione viene rispettata

'''count = 0
while count < 10:
    print(count)
    count+=1
'''

'''Chiedere all'utente di che numero vuole sapere la tabellina
e stampare la tabellina di quel numero'''

number = int(input("Di quale numero vuoi sapere la tabellina? "))
index = 0
while index <=10:
    print(number * index)
    index += 1

#per interrompere ogni tipo di ciclo utilizziamo "break"

i = 1

while i < 6:
    print(i)

    if i == 3:   #dopo aver stampato i (3) uscire dal ciclo while
        break    #tutto quello che c'è dopo non viene fatto

    i+=1

#per tornare all'inizio del ciclo saltando le funzioni sotto si usa "continue"

i = 0

while i < 6:
    i += 1

    if i == 3:
        continue     #si ferma qua e torna sopra nella condizione senza stampare sotto il numero
    
    print(i)

#per saltare un'iterazione usiamo pass

for i in range(1,20):
    if i == 13:
        pass
    else:
        print(i)


