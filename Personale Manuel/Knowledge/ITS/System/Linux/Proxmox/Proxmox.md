#Linux #Proxmox 

>Non credo ci sia da spiegare cosa sia Proxmox ma per correttezza spreco 2 righe nel dire cos'è.

# **Cos'è Proxmox VE?**
>Proxmox VE è un ambiente di virtualizzazione open source che permette di creare Container LXC e Virtual Machines per virtualizzare diverse macchine per un'organizzazione aziendale scalabile e funzionale su una singola macchina.
>Tramite la loro web GUI è possibile accedere al server e gestire le macchine in modo veloce ed intuitivo.

>La macchina sui cui è stato installato l' ISO di Proxmox viene identificato come nodo principale. Si possono avere più nodi creando di conseguenza un cluster Proxmox.
>Dal nodo principale si possono dare comandi per controllare i Container e VM dall'esterno. Molto utile per eventuali script di automazione (es. autoaggiornamento)

---
# **Comandi Pct (Proxmox container tool)**
>Esistono vari comandi Pct che permettono di fare le cose elencate prima. Ne elenco un paio di quelli che ho usato e mi sono risultati più utili per automazioni.

>==**$vmid indica l'ID del Container Lxc**==

- **Pct list**
  >Elenca tutti i container sulla macchina (sia accesi che spenti)
- **Pct status $vmid**
  >Riporta lo stato di un container specificandone l'ID
- **Pct config $vmid**
  >Elenca la configurazione generale del container specificandone l'ID
- **Pct exec $vmid -- bash -c "comando_che_si_vuole_eseguire"**
  >Permette di eseguire comandi all'interno di un container direttamente dal nodo principale specificandone l'ID
  
  ---
Installazione proxmox su una vm,
network interna in modo che il server proxmox possa accedere solo
2 schede una in NAT una in host only
Le schede di rete devono essere utilizzate collengandole a degli switch virtuali su proxmox:

---
# **Snapshot**
>Fotografia dell'immagine attuale dello stato del server

# **Backup**
>

>Su proxmox copia anche gli snapshot

---
# **Network**
>Una scheda di rete collegato ad uno switch
![[rete-proxmox.png]]


## **Masquerade sul nodo proxmox**

```bash
ip route | grep default
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -s 192.168.56.0 -o <NIC_NAT> -j MASQUERADE

#Per renderlo operativo al riavvio
post-up echo 1 > /proc/sys/net/ipv4/ip_forward
post-up iptables -t nat -a POSTROUTINNG -s 192.168.56.0 -o <NIC_NAT> -j MASQUERADE
```

Dalla gui di proxmox
Net0 campo gateway 192.168.56.10
DNS server 1.1.1.1

Di nuovo dentro la CT
```shell
ip route
ping 1.1.1.1
ping google.com
```


---

# **Utenti ruoli e permessi**

| realm   | chi                       | per cosa              |
| ------- | ------------------------- | --------------------- |
| **pam** | utenti di sistema         | shell, emergenza      |
| **pve** | utenti interni di Proxmox | GUI e API ogni giorno |
Catena: gruppo --> Ruolo --> permesso per path -->API token

>**Perchè non da root@pam**:

Un utente per persona --> in un gruppo --> con un ruolo su un path
Dai solo i permessi che servono: **minimum privilege**



# **Repository e aggiornamenti**

Usando un proxmox senza enterprise subscription serve una repo **no-subscription**

Si può fare da GUI nella sezione:
**datacenter --> pve --> updates --> repositories**

Disabilitare:
1. pve-enterprise.sources
2. ceph.sources

>Per attivare invece la repository no-subscription

add --> no-subscription

Da terminale bisogna andare in /etc/apt/sources.list.d:

# **Firewall**

Su Proxmox ci sono tre piani, dal più largo al più stretto:

- **Dataceenter:** vale per tutto
- **Nodo:** l'host
- **Guest:** la singola VM/CT

>Se si accednde un firewall senza una regola d'accesso ci si chiude fuori.

Controllare prima di avviare:
1. **snapshot del nodo**
2. consentire porta 22 (SSH) e 8006 (GUI) dalla tua rete
3. **Poi** abilito

---
## **Quorom -- maggioranza (almeno 3 nodi , sempre dispari per la question della maggioranza)**
>Il cluster decide a **maggioranza dei dati** dei voti

>2 nodi: se uno muore l'altro resta in minoranza 
>Soluzione un terzo voto esterno, il QDevice


# **Replica dischi (almeno 2 nodi)**
>Copia schedulativa di un CT/VM su un secondo nodo
>Asincrona: ogni N minuti, non in tempo reale
>Nodo A muore: su B c'è una copia recente delle VM e CT

>Dal vivo: CT --> Replication --> job, schedulazione, nodo di destinazione

---

|         | Cos'è                   | Quando               |
| ------- | ----------------------- | -------------------- |
| Backup  | copia nel tempo esterno | ripristino, disastro |
| Replica |                         |                      |
| HA      |                         |                      |
