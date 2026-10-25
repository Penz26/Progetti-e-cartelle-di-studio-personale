#CyberSecurity 

# **Cos'è un attacco SSRF?**
>In un attacco SSRF contro un server un malintenzionato fa sì che l'applicazione effettui una richiesta HTTP al server che ospita l'applicazione, tramite la sua interfaccia di rete di loopback. Questo in genere comporta la fornitura di un URL con un nome Host come 127.0.0.1 o localhost. 


>In un attacco SSRF contro il server, l'utente malintenzionato fà si che l'applicazione effettui una richiesta HTTP al server che ospita l'applicazione, tramite la sua interfaccia di rete di loopback.

>Esempio:
```http
`POST /product/stock HTTP/1.0 
Content-Type: application/x-www-form-urlencoded 
Content-Length: 118 
stockApi=http://localhost/admin`
```

>In questo modo il web-server recupera il contenuto del /admin URL e lo restituisce all'utente visto che secondo il server la richiesta viene da se stesso

--- 
## **Come si Fixa?**
>- Restringendo gli URL che il server API possa utilizzare
>- Validando la richiesta
>- bloccare solo determinati tipi di URL
>- limitare a solo https://