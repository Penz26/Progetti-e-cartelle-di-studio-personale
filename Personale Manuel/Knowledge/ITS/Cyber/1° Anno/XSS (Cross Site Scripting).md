#CyberSecurity 

# **Cos' è un attacco di Cross Site  Scripting?**
>Un malintenzionato college un codice a un sito web legittimo che verrà eseguito quando la vittima carica il sito-web. Il codice può essere caricato in diversi modi, solitamente alla fine di un URL o su una pagina che visualizza contenuti generati dagli utenti (sezione commenti, profilo, descrizione, ecc...)
```txt
htttp://banca-legittima.com/index.php?user=<script> Codice Malevolo </script>

Una volta che l'utente schiaccia sul link il codice viene eseguito dal browser oltre che aprire la pagina web legittima
```

>Il codice lato client è un codice JavaScript che viene eseguito sulla macchina di un utente dal browser web dopo che il browser ha caricato una pagina Web.

---
# **Come si Fixa?**
>Sanificare l'input e convalidarli in modo che non possa essere letto il codice come eseguibile ma solo come plain text.

>Esempio:
>Un utente pubblica un commento sotto un forum, la sezione dei commenti non è stata sanificata quindi il browser interpreta il codice come eseguibile e lo esegue. Una volta che un altro utente  carica quella pagina con quel commento il browser aprendo quella pagina e leggendo il codice ed il testo che lo compone esegue anche lo <script></script> malevolo.