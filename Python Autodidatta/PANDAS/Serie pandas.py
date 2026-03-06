import pandas as pd

voti = [100, 102, 104]

#Una serie è una lista potenziata, possiede un indice (sinistra) e i Valori (destra)
series = pd.Series(voti)

print(series)
print()
#Gli indici nonn devono essere per forza numeri. Possiamo usare etichette significative

#Assegnazione di etichette personallizate (Index)
series = pd.Series(voti, index=["Alunno A", "Alunno B", "Alunno C"])

#Possiamo accedere ai dati tramite l'etichetta
print(series["Alunno A"])

#Un DataFrame è una griglia bidimensionale di righe e colonne.
#Si crea facilmente da un dizionario Python.

data = {
    "Nome": ["Spongebob",
             "Patrick", "Squiddy"],
    "Età": [30,35,50]
}

df = pd.DataFrame(data)
print(df)
print()

#Le chiavi del dizionario diventa le colonne. 
#Gli indici (0,1,2) sono generati automaticamente e saranno gli index predefiniti.

#Per aggiungere una Colonna al DataFrame
df["Lavoro"] = ["Cuoco", "Disoccupato", "Cassiere"]

#Aggiungere una Riga (Concatenazione)
nuova_riga = pd.DataFrame([{"Nome": "Sandy", "Età": 28, "Lavoro": "Scienziata"}])
df = pd.concat([df, nuova_riga], ignore_index=True)

print(df)
print()

