import pandas as pd

df_Pokemon_2 = pd.read_csv("Pokemon.csv", index_col="Name")


#PULIZIA DATI: Rimozione (Drop)

#Cancellare Colonne
df_Pokemon_2.drop(columns=["Type2"], inplace=True)  #inplace=True per modificare direttamente il DataFrame originale, senza dover creare una copia

#Senza inplace=True, dobbiamo assegnare il risultato a una nuova variabile o sovrascrivere quella esistente
#Esempio:
#df_Pokemon_2 = df_Pokemon_2.drop(columns=["Type2"])
#oppure
#df_Pokemon_3 = df_Pokemon_2.drop(columns=["Type2"])
print(df_Pokemon_2)

df_Pokemon_2.drop(columns=["Legendary", "No"], inplace=True)
print(df_Pokemon_2)


#RIMETTO LA COLONNA TYPE2,LEGENDARY E NO PER MOSTRARE LA GESTIONE DEI VALORI MANCANTI
df_Pokemon_2 = pd.read_csv("Pokemon.csv", index_col="Name")

#Pulizia Dati: Gestione dei Valori Mancanti

#Sostituisce i valori mancanti con "Nessun secondo Tipo"
df_Pokemon_2["Type2"] = df_Pokemon_2["Type2"].fillna("No Secondary Type")  
print(df_Pokemon_2.to_string()) 

#Rimuovere righe in base a un filtro
#Rimuove i Pokemon con altezza inferiore a 1 metro
df_Pokemon_2 = df_Pokemon_2[df_Pokemon_2["Height"] >= 1.0]
print("\nPokemon alti 1 metro o più:\n", df_Pokemon_2.to_string())

#-----------------------------------------------------------------------
#Standardizzare i Valori e Correzione Tipi

#Testo (lowecase)

#RICORDA CHE NON SI PUO' METTERE COME PARAMETRO "Name" VISTO CHE E' L'INDEX DEL DATAFRAME
df_Pokemon_2["Type1"] = df_Pokemon_2["Type1"].str.lower()  #mette in minuscolo i valori della colonna Type1
print("\nTipo1 dei Pokemon in minuscolo:\n", df_Pokemon_2.to_string())

#Come cambiare il testo dell'index (Name)
df_Pokemon_2.index = df_Pokemon_2.index.str.lower()  #mette in minuscolo i valori dell'indice (i nomi dei Pokemon)
print("\n", "Dataframe con i nomi dei Pokemon in lowercase", df_Pokemon_2.to_string())

#Sostituzione Valori

df_Pokemon_2["Type1"] = df_Pokemon_2["Type1"].replace({"grass": "GRASS"}) #è grass ora type1 perchè abbiamo fatto lowercase l'intera colonna Type1
print("\n", "Dataframe con Type1 Grass sostituito:\n", df_Pokemon_2.to_string())

#Conversione Tipi di Dati (astype)
df_Pokemon_2["Legendary"] = df_Pokemon_2["Legendary"].astype(bool)  #converte la colonna Legendary in booleano (0 diventa False, 1 diventa True)
print("\n", "Dataframe con Legendary convertito in booleano:\n", df_Pokemon_2.to_string())


#Rimozione Duplicati
#Errori di copia/incolla possono creare righe identiche

df_Pokemon_2 = df_Pokemon_2.drop_duplicates()  #rimuove le righe duplicate, mantenendo solo la prima occorrenza
print("\n", "Dataframe senza Duplicati (NON SUCCEDE NULLA)", df_Pokemon_2.to_string())