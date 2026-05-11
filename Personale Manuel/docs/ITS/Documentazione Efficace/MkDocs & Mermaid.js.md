#GitHub [[Git & GitHub]]

# **Cosa è?**
>MkDocs è un'estensione di Python che permette di creare appunti direttamente in codice e li trasforma in siti.

## *Perchè?*
- **Il problema con Word**
>	Difficile da versionare - Git non legge i .docx. 
- **Usiamo il MarkDown**
>	Formato testuale semplice, leggibile da chiunque e da qualunque macchina. Compatibile con Git.
- **Single Source of Truth***
>	La documentazione vive insieme al codice o all'infrastruttura, sempre sincronizzata con lo stato reale del progetto.
- **Automazione**
>	Il sito con la documentazione si genera automaticamente a ogni modifica.

---
# **1. Installazione e utilizzo**

>Installazione Libreria di MkDocs per Python
```python
pip install mkdocs-material
```

>Creazione della cartella docs (con all'interno lo yaml e il md file) per il progetto
```Python
mkdocs new . #crea il progetto nella cartella specifica, in questo                   caso nella cartella attuale
```

>Avvia il server e lo aggiorna
```Python
mkdocs serve

--livereload permette di aggiornare continuamente la pagina in tempo reale
```

---

# **2. Configurazione**
>Attraverso il file mkdocs.yml si può configurare il sito

```Mermaid.js
site_name: "Documentazione Progetto ITS"
theme:
name: material
palette:
scheme: slate
primary: teal
nav:
  - Home: index.md
  - Git & GitHub:
      - Introduzione: "Comandi Git & GitHub/Comandi di Git Basilari.md"
markdown_extensions:
- pymdownx.superfences:
custom_fences:
- name: mermaid
class: mermaid
```

- site_name = titolo del sito di documentazione
- scheme: slate = tema scuro
- superfences = abilita il rendering dei blocchi Mermaid come immagini
---
# **Diagrammi Mermaid (mermaid.js)

>Grazie a Mermaid possiamo definire le relazioni logiche e lui si crea i diagrammi. Tutto ciò che sta tra '''mermaid e ''' viene reinderizzato come immagine.

>Sintassi Base:
>- **graph TD / graph LR**
>  Direzione del grafo: Top Down (Dall'alto al basso), Left or Right (Da sinistra a destra)
>- **A-->B**
>  Collegamento base
>- **A(["Testo"])**
>  Nodo a pillola
>- **A{Decisione}**
>  Nodo a diamante per i punti decisionali
>- **A[testo]**
>  Nodo rettangolare standard
>- **subgraph**
>- Per raggruppare componenti, ad esempio reti diverse

>**Esempio 1 - Flowchart Logico:**
![[flowchar_mermaid.png]]

>**Esempio 2 - Network Diagram:**
![[network_diagram_mermaid.png]]