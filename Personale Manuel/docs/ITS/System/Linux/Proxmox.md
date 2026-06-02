#Linux 

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