>- **COMPILAZIONE**
>- Developer sviluppa un nuovo pacchetto in src/
>- Developer ha accesso alla repo di GitLab
>- Developer cambia valori delle variabili: (Nome package, versione, architettura, Maintainer, Descrizione pacchetto e prefisso)
>- Developer Pusha pacchetto (parte gitlab runner su VM-compilazione)
>- Gitlab runner builda container docker con immagine giusta per cui compilare, installa pacchetti necessari per la compilazione
>- Compila il pacchetto in .deb e lo salva come artefatto
>- Uccide il container di compilazione

> - **PUBBLICAZIONE**
> - GitLab runner prende l'artefatto del job di compilazione
> - Crea un container per il trasferimento dei file sul server della repository aptly
> - Configura la connessione 
> - Trasferisce il pacchetto .deb sul server aptly
> - Aggiunge il pacchetto all repo
> - Crea lo snapshot aptly
> - Pubblica lo snapshot aptly

---

# **Passi/Ruoli per l'automazione con Ansible**

