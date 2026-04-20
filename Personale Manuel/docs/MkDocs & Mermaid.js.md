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
```

---

# **2. Configurazione**
>Attraverso il file mkdocs.yml si può configurare il sito