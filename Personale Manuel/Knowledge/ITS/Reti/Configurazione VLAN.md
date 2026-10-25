#Ret-ITS 
# **Step 1. Firewall (Sophos)**

>Il Firewall agirà come gateway per la nuova VLAN, gestendo il routing e gli indirizzi IP.

## **1. Creazione Interfaccia VLAN (Router)**
>- Andare su Network > Interfaces
>- Cliccare su Add Interface e selezionare VLAN
>- Scegliere il VLAN ID: (solitamente 1 è per il management mentre il resto da decimali interi, 10 , 20, 30, ecc). Noi abbiamo usato 60
>- Interfaccia Fisica: selezionare la LAN collegata allo switch Zyxel
>- Zone: solitamente LAN
>- IP Address: assegnate un IP statico al firewall in questa sottorete (192.168.60.1/24)

## **2. DHCP**
>Andare su Network > DHCP
>Aggiungere un nuovo server DHCP associato all'interfaccia VLAN appena creata per fornire IP ai client

---
# **Step 2. Switch (Zyxel Nebula)**
>Ora dobbiamo "istruire" lo switch a riconoscere e trasportare il traffico della VLAN 60

## **1. Definizione VLAN a livello di Sito**
>In Nebula andare su:
>- Site-wide > Configure > Switches > VLAN configuration
## **2. Configurazione delle Porte**
>- Porta Uplink (verso il Sophos): deve essere impostata come Trunk. Assicurarsi che la VLAN 60 sia inclusa nelle "Allowed VLANs"
>- Porta Access Point: Se l'AP deve trasmettere più SSID su diverse VLAN, anche questo porta deve essere un Trunk. La VLAN di gestione dell' AP sarà la "Native" (Untagged), mentre la VLAN 60 sarà Tagged, quindi tutti i pacchetti che passano per quella VLAN saranno di tipo 60.

---

# **Step 3. Configurazione WIFI su Nebula (SSID)**
>Per associare il segnale WIFI alla VLAN creata:

>1. Creazione SSID:
>  - Andare su Site-Wide > Configure > Access Points > SSID settings
>  - Abilitare un nuovo SSID e dategli un nome

>2. Tagging VLAN:
>   - Andare su Site-wide > Configure > Access points > SSID advanced settings
>   - Cercare la sezione VLAN ID
>   - Selezionare Static e inserire il numero della VLAN (es. 60)

---

# **Step 4. Regole di Firewall (Sophos Firewall rules)**
>Di default, il traffico tra VLAN diverse o verso internet potrebbe essere bloccato. Dovete creare delle regole delle regole specifiche in Protections > Rules and policies:

>**A - Accesso a Internet**
>- Source Zone: WiFi Guest ( o la zona scelta)
>- Source Network VLAN 60 Subnet.
>- Destination Zone: WAN
>- Services: Any 
>- NAT: Abilita il Masquerading 

>**B - Isolamento o Comunicazione Inter-VLAN**
>Se volete che i clienti WiFi non vedano i server sulla LAN principale: non create nessuna regola che colleghi le due zone.

>Se invece serve accesso a una risorsa specifica (es. stampante):
>- Source: VLAN 60
>- Destination: LAN
>- Destination IP: IP_Stampante

---

# **Step 5. Regola di Firewall tipo filtro**

## **1. Crea l'oggetto "Sito Web"**
>Dobbiamo dire a Sophos quale sito vogliamo bloccare
>1. Andare su Onbjects > Content > URL Groups
>2. Cliccare su Add
>3. Dare un nome alla regola
>4. Inserire il dominio (es. apple.com, ecc...)

## **2. Creare o modificare la Web Policy**
>Ora dobbiamo creare la "legge" che proibisce l'accesso a quel gruppo
>1. Andare su Web > Policies
>2. Potete modificarne una esistente o cliccare su Add policy
>3. Cliccate su Add Rule:
>   - Activities: Selezionate l'URL Group creata prima
>   - User: Anybody
>   - Action: block
>4. Assicuratevi che questa regola sia in alto
>5. Cliccate su Save

## **3. Applicare la Policy alla regola del Firewall**
>Questa è la fase cruciale: la regola che avete creato nel post precedente per far navigare il WiFi deve usare questa protezione.
>1. Andare su Rules and Policies > Firewall rules
>2. Aprire la regola che permette il traffico dalla VLAN WiFi verso la WAN
>3. Scendere fino alla sezione Web Filtering
>4. Nel menù a tendina Web Policy, selezionare la policy creata prima
>5. Importante: spuntate la casella Scan HTTP and decrypted HTTPS (se avete la decifratura attiva) o assicuratevi che il Web proxy sia attivo

>[!NOTE] Ci sono anche delle categorie predefinite di regole su Sophos (es. Social Media, Gambling, Pornografia, ecc...)

