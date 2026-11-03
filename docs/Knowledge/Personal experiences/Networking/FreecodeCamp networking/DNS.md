#Networking 

>Un DNS è il processo che mappa nomi umani ad indirizzi IP. Senza di esso dovremmo memorizzare gli indirizzi IP di qualsiasi cosa in rete.

**Domain Name System (DNS)** è strutturato gerarchicamente.
Se un server DNS locale non contiene il record richiesto manderà la richiesta alla catena finchè una risposta non è stata ricevuta.

Il DNS per funzionare richiede un FQDN (Fully qualified domain name)

| www.                  | google.           | com                    |
| --------------------- | ----------------- | ---------------------- |
| il servizio specifico | Il dominio locale | TLD (Top level domain) |

---
# Livelli di server DNS

## Local DNS server
>il server DNS locale che contiene i file HOSTS che mappano l' FQDN ad un indirizzo IP

## Top Level Domain (TLD) server
>Il server che contiene i record per un top level domain
>(es. com, org, net, edu, gov, mil, int)

>Ognuno di questi server contiene tutte le informazioni riguardo i rispettivi domini

>Server TLD delegano a server di secondo livello per gestire il carico ma il server responsabile rimane lui

## Root Server
>Il server che contiene i record dei server TLD

## Autoritativi (Name Server)
>Un server DNS autoritativo risponde a una richiesta per cui è stato specificamente configurato per contenere quella informazione
>Una risposta autoritativa viene dal server DNS che contiene il record originale

## Non autoritativi
>Un server DNS non autoritativo è uno che risponde ad una richiesta con le informazioni DNS che riceve da un altro server DNS
>Una risposta DNS non autoritativa è una risposta che non viene dal name server ufficiale per il dominio. E' una risposta di seconda o terza mano

---
# Record DNS

## A
>Mappa il nome dell'host al loro indirizzo IPv4

## AAAA
>Mappa il nome dell'host al loro indirizzo IPv4

## CNAME
>Mappa un alias al nome dell'host

## PTR
>Punta ad un alias

## MX
>Mappa il mail server che è specificato per un determinato dominio. E' il record che determina come un'email va dal sender al recipiente

---
# Dynamic DNS (DDNS)
>Permette aggiornamenti immediati e leggeri a un database di un DNS locale. Questo è utile quando il FQDN rimane lo stesso ma l'indirizzo IP cambia regolarmente.

>Viene implementato tramite un servizio addizionale DNS

# Aggiornamento DDNS 
>Un metodo di aggiornare name servers senza l'intervento di un amministratore

>Un provider DDNS rilascia un software che monitora gli indirizzi IP referenziati nel sistema ed appena l'indirizzo IP cambia il software manda un aggiornamento al rispettivo server DNS.

