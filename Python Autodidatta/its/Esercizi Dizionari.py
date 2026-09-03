#Esercizio 1

temperature = [
    {"Citta": "Milano", "gradi": 12},
    {"Città": "Roma","gradi": 15},
    {"Città": "Napoli", "gradi": 18}
    ]

print(temperature[2]["gradi"])   #possiamo concatenare le parentesi quadre quando ci sono liste/dizionari all' interno di altri dizionari/liste


#Esercizio 2
print()
#materiale =["Matita","Penna","Quaderno"]
materiale_1 =[{
    "strumento": "Matita", "prezzo": "0.50€"
},{
    "strumento": "Penna", "prezzo": "1.20€"
},{
    "strumento": "Quaderno", "prezzo": "2.90€" 
}]

'''prezzo ={
    materiale[0]: "0.50€",
    materiale[1]: "1.20€",
    materiale[2]: "2.90€"
}'''

print(materiale_1[1]["prezzo"])
'''for i in prezzo:
    print(i, "---->", "prezzo", prezzo[i])'''

#Esercizio 3

'''ruolo = ["Attaccante","Difensore","Portiere"]
Alunni = {
    "Alice": ruolo[0],
    "Marco": ruolo[1],
    "Luca": ruolo[2]
}
'''
Alunni_1 = [{
    "Nome": "Alice",
    "ruolo": ",ruolo",
    "posizione": "Attaccante"
},{
    "Nome": "Marco",
    "ruolo": ",ruolo",
    "posizione": "Difensore"
},{
    "Nome": "Luca",
    "ruolo": ",ruolo",
    "posizione": "Portiere"
}]

print()
print(Alunni_1[1]["posizione"])
'''for i in Alunni:
    print(i, ",ruolo:" ,Alunni[i])
'''

#Esercizio 4
voto = [(7,8,9),(6,6),("nessun voto")]
Amico ={
    "Sara": voto[0],
    "Thomas": voto[1],
    "Elena": voto[2]
}
print()
for i in Amico:
    print(i,":", Amico[i])

voti = {
    "Sara": [7,8,9],
    "Thomas": [6,6],
    "Elena": []  #mettiamo un vettore vuoto così da poi poter usare len nel caso in cui
}

#Esercizio 5
print()

posts = [
    {
        "contenuto": "Programmare è come fare magia con la tastiera ✨",
        "like": 90,
        "commenti": [
            {"utente": "Martina","contenuto": "Bellissimo!" },
            {"utente": "Giacomo","contenuto": "Condivido!" },
            {"utente": "Elena","contenuto": "Grande lavoro ragazzi" }
        ]
    },
    {
        "contenuto": "Coding lesson #1",
        "like": 120,
        "commenti": [
            {"utente": "Martina","contenuto": "Pila!" },
            {"utente": "Giacomo","contenuto": "Condivido!" },
            {"utente": "Elena","contenuto": "Ottimo video" }
        ]
    }

]
somma = 0
for post in posts:
    somma += post["like"]
media = somma / len(posts)
print(media)