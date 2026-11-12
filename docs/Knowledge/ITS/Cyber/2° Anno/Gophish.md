---
date: 2026-11-12
tags:
  - CyberSecurity
subject: Attack
module: Gophish
source: https://drive.osaspace.it/index.php/apps/onlyoffice/19251?filePath=%2FITS_SANDBOX%2FSANDBOX%20-%20MATERIALI%20DOCENTI%2FSECONDO%20ANNO%2FCybersecurity%2FLezione06%2FLezione06.pdf
---
# **Cosa Serve?**
>Serve per fare campagne di phishing 

>Cosa bisogna fare:

Installiamo Gophish per gestire la campagna e mailpit che invece si occuperà da fare server SMTP
```bash
docker pull gophish/gophish
docker run -d --name gophish --restart unless-stopped -p 3333:3333 -p 8080:8080 gophish/gophish:latest

#Creiamo la network con cui comunicheranno i due container
docker network create phishing-lab

#Aggiungiamo il container di gophish
docker network connect phishing-lab gophish

#Scarichiamo mailpit e lo eseguiamo dentro la network giusta
docker pull axllent/mailpit
docker run -d --name mailpit --restart unless-stopped --network phishing-lab \\n-p 127.0.0.1:8025:8025 axll
```

>Ora avremo sulla porta 3333:3333 la dashboard di gophish
>Per loggare dovremo vedere lo user e la password dai log del container:
```bash
docker logs gophish

#vedremo un campo simile a questo
time="2026-11-12T10:05:32Z" level=info msg="Please login with the username admin and the password 3cee4db60ff2e79a
```

>Una volta loggati dentro avremo una pagina come questa:


Ci sono 4 principali cose da fare:
- settare un sending profiles
- email template
- landing page
- user & groups

## **Sending Profiles**
>Name: nome del profilo di sending
>SMTP From: dominio da cui mandare la mail

Salvare il profilo

## **Email template**
>Name: nome del template
>Envelope sender: Prova@example.com
>Subjcet: Titolo della mail
>Text: Testo contenuto nella mail

## **Landing Page**
>Name: Nome della landing page
>HTML: pagina a cui verrà indirizzato l'utente con la mail


## **User & Groups**
>email: phisher@example.com

>Una volta fatto tutto questo avviamo la campaign

## **New Campaign**
>Name: Nome campagna
>Email template: selezionamo dal menù a tendina
>Landing Page: selezionamo dal menù a tendina
>URL: url del server SMTP (con mailpit http://localhost:1025)
>Sending Profile: Profilo del sender


