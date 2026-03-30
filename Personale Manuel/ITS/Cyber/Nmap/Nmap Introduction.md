#CyberSecurity 

# **Cos' è Nmap?**
>Nmap è un software Open Source per l'esplorazione della rete che permette di rilevare macchine sulla rete, macchine online, porte aperte, servizi in esecuzione e relativi versioni assieme anche ad eventuali vulnerabilità.

# **1. Elencare tutti gli host di una determinate rete**
>Non invia alcun pacchetto ai dispositivi ma parla solo con il server DNS
>Genera l'elenco degli IP della subnet con i relativi nomi HOST
```Shell
nmap -sL subnet_mask
```

# **2. Vedere effettivamente quali macchine sono online**
>Questo comando farà un *ping sweep* ovvero manderà contemporaneamente pacchetti ICMP Echo Request (ping) a una serie di indirizzi IP. Viene utilizzato per avere un idea della mappatura della rete
```Shell
nmap -sn --open subnet_mask

#si possono escludere anche degli ip con --exclude
nmap -sn --open subnet_mask --exclude 192.168.1.1

#si può usare anche un file .txt per fargli cercare solo gli IP specificati al suo interno
nmap -sn --open -iL iplist.txt
```

# **3. Salvare i dati delle nostre scan**
>Una volta fatte le nostre scannerizzazioni possiamo salvare il loro output con delle semplici flag
```Shell
nmap -sn --open subnet_mask -oA output_scan
#Questo comando farà la scannerizzazione dei dispositivi online sulla rete e salverà il suo output in tutte le versioni (A) ovvero .nmap (come si vede da linea di comando) .gnamp (formato "greppabile") e .xml (un file di testo il cui contenuto è organizzato in modo da contenere dati strutturati che possomno essere interpretati da vari programmi)
```

# **4. Vedere che porte sono aperte**
>Con il prossimo comando potremmo vedere che porte ha aperte la macchina di cui specifichiamo l'ip o il nome sulla rete
```Shell
nmap nome_server #(oppure IP)

#mentre se vogliamo anche la versione di cosa ci sia su quella porta usiamo:
nmap -sV nome_server #(Oppure IP)

#Per esempio se il server ha ssh aperto vedremo
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6...

```

# **5. Scannerizzare le porte TCP e UDP più usate**
>Ci sono delle flag che permettono di scannerizzare le porte TCP e UDP più utilizzate generalmente. 
>Vedremo anche come far sì che il computer ci parli mentre fa la scan e incrementare la velocità dello scan
```Shell
sudo nmap -sT -sU -sV -v -T5 nome_server

#sT scannerizza per le porte TCP più comuni
#sU scannerizza per le porte UDP più comuni (serve sudo per le UDP)
#-v abilita il verbose (il computer ci parla mentre fa le cose)
#-T setta la velocità della nostra scannerizzazione (di default è 3, più alto il numero più veloce è lo scan) T5 è il massimo

```

# **6. Usare degli script di default di Nmap**
>Nmap ci dà anche degli script che possiamo usare durante le nostre scan. Questi script sono all'interno di /usr/share/nmap/scripts
```Shell
#sC userà tutti i default script
nmap -sV -sC -v nome_server

#se vogliamo usare degli script nello specifico usiamo        --script
nmap -sV --script=nome_script -p porta_da_attaccare nome_server
```

# **7. Usare lo script vulners per vedere che vulnerabilità ci siano sul target**
>Dopo aver fatto lo scan con -sV il comando da in pasto il risultato al database di vulnerabilità di vulners.com che restituisce un elenco di vulnerabilità note associate a quelle specifiche versioni includendo un punteggio di gravità CVSS.


>**Molte volte però nmap dice che ci sono delle vulnerabilità solo basandosi sul numero della versione ufficiale del servizio, ma non controlla eventuali backporting eseguiti da sviluppatori per il proprio OS che corregono eventuali debolezze. 
>Ciò risulta in "falsi positivi" che quindi ti allertano di eventuali debolezze quando in verità è tutto a posto :)**
```Shell
#darà tutte le vulnerabilità trovate in base ai vari servizi
nmap -sV --script=vulners -v nome_server

#possiamo anche filtrare in base al valore CVSS (in questo caso dal 7 in su)
nmap -sV --script=vulners --script-args mincvss=7.0 -v nome_server
```