# **Il Problema**
>Con MkDocs creiamo la pagina della nostra documentazione, però non è online. Abbiamo il sito in locale.

>Con il comando mkdocs build il sistema crea una cartella site/ con i veri file HTML e CSS pronti per essere pubblicati

# **Soluzione**
>GitHub Pages con GitHub Actions

>Usiamo GitHub pages, un servizio che prende i file HTML dalla repository e li trasforma in un sito web pubblico.

![[github-page-setting.png]]

---

# **Automatizzazione**
>CI/CD

# **CI - Continuos Integration**
>Ogni volta che un programmatore aggiunge del codice (o un file MarkDown), un sistema automatico lo scarica e lo controlla per assicurarsi che non ci siano errori.

# **CD - Continuos Deployment**
>Se i controlli sono superati, il sistema prende quel codice e lo pubblica automaticamente su internet.

---

# **CI/CD GitHub**
>GitHub Actions

>GitHub ti mette a disposizione un computer vuoto