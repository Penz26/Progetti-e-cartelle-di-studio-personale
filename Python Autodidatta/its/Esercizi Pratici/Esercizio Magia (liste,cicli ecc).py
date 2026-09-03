power = []
print("Benvenuto nel nostro inventario delle spell di combattimento\n\n")
scelta= "Play"

while scelta!= "Quit":
    scelta = input("Per aggiungere un potere scrivi 'Add', per rimuovere un potere 'Erase',\nper sostituire un potere 'Sub', per mostrare lista 'Show', e infine per uscire Quit  ") 
    if scelta == "Add":
        power.append(input("\n\nChe potere vuoi aggiungere: "))
        print("Potere aggiunto con successo\n\n")

    elif scelta == "Erase":
        power_to_remove = input("Che potere vuoi rimuovere? ")  #oppure con il codice e successivamente del
        if power_to_remove in power:
            power.remove(power_to_remove)
            print(power_to_remove, "Rimosso con successo\n\n")
        else:
            print("Potere non trovato\n\n")

    elif scelta == "Sub":
        i = 0
        while i < len(power):
            print("Codice: " ,i, "-" , power[i])
            i+=1
        code = int(input("Inserisci il codice di quello che vuoi sostituire: "))
        substitute = input("\nInserisci il nuovo potere con cui sostituirlo: ")
        power[code] = substitute
        
    elif scelta == "Show":
        print("\n\nQuesta è la tua lista ", power , "\n\n")
    elif scelta == "Quit":
        print("\nAlla prossima volta\n\n")
        break
    else:
        print("\nHai sbagliato a inserire l'opzione\n\n")
        continue

#CALCOLI

i = 0
count_8 = 0
count_fire = 0
count_ice = 0
count_storm = 0
somma = 0

while i < len(power):
    #Il controllo di Fire, Ice o Storm è case sensitive, ovvero deve trovare scritta la maiuscola
    if "Fire"  in power[i]:
        count_fire+=1
    if "Ice" in power[i]:
        count_ice+=1
    if "Storm" in power[i]:
        count_storm+=1

    if len(power[i]) > 8:
        count_8+=1

    if i == 0:
        potere_più_lungo = power[0]
    else:
        if len(power[i]) > len(power[i-1]):
            potere_più_lungo = power[i]

    somma+=len(power[i])
    i+=1


print("Ci sono " ,count_fire , "poteri col fuoco")
print("Ci sono " ,count_ice , "poteri col ghiaccio")
print("Ci sono " ,count_storm , "poteri di tipo storm ")
print("La media di lunghezza degli elementi nella lista è: " ,somma/len(power))
print("Il Potere più lungo è " + potere_più_lungo)
print("La percentuale di poteri con più di 8 caratteri è " , (count_8/len(power)*100) ,"%")