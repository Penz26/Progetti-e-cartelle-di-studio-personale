import time

for i in range (10):#se mettiamo solo 1 numero nel for verrà considerato così il ciclo
    print(i)        #(i = 0, i < n, i+1) quindi l'indice partirà automatiamente da 0 e avanzerà di 1

for i in range(50,100,2): #parte da 50, arriva a 100 (escluso) e avanza di 2 ogni volta
    print(i)

for i in "Bro Code": #ogni lettera viene stampata su una nuova riga
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)   #ad ogni stampa prende 1 secondo di pausa (da specificare nelle parentesi)