import pandas as pd

#ACQUISIZIONE DATI: Leggere CSV e JSON

#Lettura CSV
df_Pokemon = pd.read_csv("Pokemon.csv", index_col="Name")

#Lettura JSON
#df_soldi = pd.read_json()

print(df_Pokemon)

#Panda nasconde le righe centrali per risparmiare spazio. 
#Usa to_string() per vedere tutto

print()
print()
print(df_Pokemon.to_string())

#Per selezionare solo alcune colonne possiamo metterle come argomento

#Così stamperà solo l'altezza dei Pokemon (N.B. SE SI CAMBIA L'INDEX DELLA TABELLA NON SI PUO' SELEZIONARE QUEL PARAMETRO NELLA VISUALIZZAZIONE, VISTO CHE VERRA' VISTA SEMPRE)
print("\n", df_Pokemon["Height"])

#Ma ovviamente possiamo selezionare più colonne
print("\n", df_Pokemon[["Type1","Height","Weight"]])

#Navigare le Righe

#LOC (Location by Label), cerca tramite l'etichetta dell'indice(Stringa)

print("\n", df_Pokemon.loc["Pikachu"])

#ILOC(Integer Location), cerca tramite la posizione numerica assoluta (0-N)
print("\n", df_Pokemon.iloc[25])

#Slicing e Ricerca Sicura

#Elencherà tutti i Pokemon da Charizard a Blastoise

print("\n", df_Pokemon.loc["Charizard":"Blastoise"])

#Esempio per la gestione degli errori:
try:
    name = input("\nDi che Pokemon vuoi sapere le statistiche? ")
    print("\n", df_Pokemon.loc[name])
except KeyError:
    print("\nPokemon non trovato!")

#Filtraggio Logico
#Il filtraggio restituisce solo le righe che soddisfano una condizione logica

altezza = df_Pokemon.loc[df_Pokemon["Height"] >= 2.0]
print("\nPokemon alti 2 metri o più:\n", altezza)

leggendari = df_Pokemon.loc[df_Pokemon["Legendary"] == 1]
print("\nPokemon Leggendari:\n", leggendari)

#Filtraggio Combinato
#Per combinare più condizioni logiche, usiamo & (AND) e | (OR)

#OR (Unione)

pokemon_acqua = df_Pokemon[(df_Pokemon["Type1"] == "Water") | (df_Pokemon["Type2"] == "Water")]

#Stamperà solo i Pokemon che hanno come Tipo1 o Tipo2 acqua
print("\nPokemon di tipo Acqua:\n", pokemon_acqua)


#AND (Intersezione)

draghi_fuoco = df_Pokemon.loc[(df_Pokemon["Type1"] == "Fire") & (df_Pokemon["Type2"] == "Flying")]

#Stampa solo i Pokemon che sono tipo1 fuoco e di tipo2 volo
print("\nPokemon di tipo Fuoco e Volante:\n", draghi_fuoco)

#Analisi Statistica: Aggregazione
#Pandas offre funzioni di aggregazione 
#per calcolare statistiche come media, somma, conteggio, ecc.

#MEDIA (mean)
media = df_Pokemon.mean(numeric_only=True)
#Stampa la media delle statistiche numeriche (es. altezza media, peso medio, ecc.)
print("\nMedia delle statistiche numeriche:\n", media)

#Calcolo della media di una colonna specifica (es. altezza media dei Pokemon)
media_altezza = df_Pokemon["Height"].mean()
print("\nAltezza media dei Pokemon:", media_altezza)

#SOMMA (sum)
peso  = df_Pokemon["Weight"].sum()
print("\nPeso totale dei Pokemon:", peso)

#Estremi (min e max)
min_peso = df_Pokemon["Weight"].min()
max_peso = df_Pokemon["Weight"].max()
print(f"\nPeso minimo: {min_peso}, Peso massimo: {max_peso}")

#CONTEGGIO (count)
conteggio = df_Pokemon.count()
#Stampa il conteggio dei dati per colonna (es. quante righe ha ogni colonna, utile per verificare se ci sono valori mancanti)
print("\nConteggio dei dati per colonna:\n", conteggio)

conteggio_tipo1 = df_Pokemon["Type1"].value_counts()
#Stampa il conteggio di quanti Pokemon ci sono per ogni Tipo1 (es. quanti Pokemon di tipo Acqua, Fuoco, Erba, ecc.) 
print("\nConteggio per tipo1:\n", conteggio_tipo1)

#Conteggio con filtro
conteggio_acqua = df_Pokemon[df_Pokemon["Type1"] == "Water"].count()
print("\nConteggio dei Pokemon di tipo Acqua:\n", conteggio_acqua)


#GROUPBY: ANALISI PER GRUPPI
#Il metodo groupby permette di raggruppare i dati in base a una o più colonne e applicare funzioni di aggregazione su ciascun gruppo.

#Esempio: Calcolare l'altezza media dei Pokemon per ogni Tipo1
#Raggruppa i Pokemon in base al loro tipo1 (water,fire,dragon, ecc.) e calcola la media dell'altezza per ciascun gruppo
altezza_gruppi = df_Pokemon.groupby("Type1")["Height"].mean()
print("\nAltezza media per tipo1:\n", altezza_gruppi)