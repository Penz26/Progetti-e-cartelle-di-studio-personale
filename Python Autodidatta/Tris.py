# --- Funzione 1: Inizializza e Visualizza il Tabellone ---
def disegna_tabellone(tabellone):
    """
    Stampa il tabellone del Tris nella console.
    
    Il tabellone è rappresentato come una lista di 9 elementi,
    dove l'indice corrisponde alla posizione.
    Esempio:
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """
    print(f" {tabellone[0]} | {tabellone[1]} | {tabellone[2]} ")
    print("---+---+---")
    print(f" {tabellone[3]} | {tabellone[4]} | {tabellone[5]} ")
    print("---+---+---")
    print(f" {tabellone[6]} | {tabellone[7]} | {tabellone[8]} ")
    print()
# --- Funzione 2: Verifica della Vittoria ---
def controlla_vittoria(tabellone, marcatore):
    """
    Controlla se il marcatore (X o O) ha vinto il gioco.
    """
    # Tutte le possibili combinazioni vincenti (linee orizzontali, verticali, diagonali)
    combinazioni_vincenti = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Orizzontali
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticali
        (0, 4, 8), (2, 4, 6)             # Diagonali
    ]
    
    # Verifica ogni combinazione
    for a, b, c in combinazioni_vincenti:
        if tabellone[a] == tabellone[b] == tabellone[c] == marcatore:
            return True
    return False

# --- Funzione 3: Gioco Principale ---
def gioca_tris():
    """
    Gestisce il flusso principale del gioco del Tris.
    """
    # Inizializza il tabellone con i numeri da 1 a 9 come indicatori di posizione
    # L'utente penserà ai numeri, ma in realtà stiamo usando gli indici 0-8.
    tabellone = [str(i+1) for i in range(9)] 
    giocatore_corrente = 'X'
    mosse_effettuate = 0
    gioco_in_corso = True

    print("🎉 Benvenuti al Tris! 🎉")
    print("Il Giocatore 1 è 'X', il Giocatore 2 è 'O'.")
    print("Scegli un numero da 1 a 9 per posizionare il tuo marcatore.")

    while gioco_in_corso:
        # 1. Visualizza il tabellone corrente
        disegna_tabellone(tabellone)

        # 2. Richiedi la mossa al giocatore corrente
        mossa_valida = False
        while not mossa_valida:
            try:
                scelta = input(f"Giocatore {giocatore_corrente}, scegli la posizione (1-9): ")
                # L'input dell'utente è 1-9, quindi sottraiamo 1 per l'indice 0-8
                indice_scelto = int(scelta) - 1

                # Controlla se l'indice è valido (0-8) e la posizione è libera
                if 0 <= indice_scelto <= 8 and tabellone[indice_scelto] in [str(i) for i in range(1, 10)]:
                    mossa_valida = True
                else:
                    print("❌ Posizione non valida o già occupata. Riprova.")
            except ValueError:
                print("❌ Input non valido. Inserisci un numero tra 1 e 9.")
            
        # 3. Aggiorna il tabellone e il contatore delle mosse
        tabellone[indice_scelto] = giocatore_corrente
        mosse_effettuate += 1

        # 4. Controlla la vittoria
        if controlla_vittoria(tabellone, giocatore_corrente):
            disegna_tabellone(tabellone)
            print(f"🥳 CONGRATULAZIONI! Il Giocatore {giocatore_corrente} ha vinto!")
            gioco_in_corso = False
        
        # 5. Controlla il pareggio
        elif mosse_effettuate == 9:
            disegna_tabellone(tabellone)
            print("🤝 Partita finita: Pareggio!")
            gioco_in_corso = False
        
        # 6. Cambia giocatore
        else:
            giocatore_corrente = 'O' if giocatore_corrente == 'X' else 'X'

# --- Esecuzione del Gioco ---
if __name__ == "__main__":
    gioca_tris()