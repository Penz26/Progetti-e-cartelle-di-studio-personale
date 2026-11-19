---
date: 2026-11-19
tags:
  - "#Kubernetes"
subject:
module:
source: https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/
---
# **Che cos'è?**
>Kubernetes è una piattaforma open-source che permette di orchestrare la (programmazione) e l'esecuzione di container dentro e fuori un cluster di computer.

**Kubernetes coordina un cluster di computer in alta disponibilità che sono connessi per lavorare come una singola unità**.
>L'astrazione di Kubernetes ci permette di fare il deploy di applicazioni containerizzate su un cluster senza doverle legare specificamente ad una macchina individuale.

Un cluster Kubernetes consiste di 2 tipi di risorse:
1. **Piano di controllo** coordina il cluster (programmazione,mantenimento dello stato desiderato, scaling e aggiornamenti)
2. **Nodi** sono i worker che fanno andare l'applicazione

![[cluster-kubernetes.png|551]]

>[!NOTE] **Il piano di controllo** organizza il cluster e i nodi che sono usati per hostare l'applicazione

>Un **nodo** è una VM o un computer fisico che serve da **worker** in un **cluster kubernetes**
>Ogni nodo ha un **Kubelet**, un agent per l'amministrazione del nodo e la comunicazione con il piano di controllo.

Quando si fa il deploy di un applicazione con Kubernetes diciamo al **control plane** di inizializzare i container dell'applicazione.
Il control plane pianifica i container che devono essere eseguiti sul nodo del cluster.

>[!NOTE] **I componenti a livello nodo, come i kubelet,** comunicano con il control plane usando le **API di Kubernetes** che il control plane espone.

---
# **Installazione**
>Per fare delle prove useremo **[minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)** che ci permette di spawnare delle VM

>Inizializzamo un cluster minikube:
```bash
minikube start

#Verifichiamo lo status del cluster
minikube status
```

---
# **Deployment Kubernetes**
>Un deployment è responsabile della creazione e l'aggiornamento di istanze dell'applicazione.

Una volta che si ha un cluster kubernetes attivo si possono deployare le proprie applicazioni su di esso.
Per farlo creiamo un **Kubernetes Deployment**

>Un **deployment kubernetes** istruisce Kubernetes sul come creare e aggiornare un'istanza della propria applicazione.
>Una volta creato il **Deployment**, il **control plane** di Kubernetes programma l'istanza dell'applicazione inclusa in quel Deployment da eseguire sui singoli **Nodi** sul cluster.

>Una volta che l'istanze delle applicazioni sono state create un **Kubernetes controller-deployment** monitora continuamente quelle istanze.

>[!IMPORTANT] Se un nodo che sta hostando un istanza va giù o viene eliminato, il **Kubernetes deployment-controller ==rimpiazza==** quell'istanza su un altro Nodo nel cluster.
>**Questo permette un meccanismo di self-healing per controllare il mantenimento e sistemare il fallimento delle macchine**

![[deployment-kubernetes.png]]

Si possono creare e organizzare un Deployment usando **kubectl**

>**kubectl** utilizza le API di Kubernetes per interagire con il cluster.

## **kubectl basics**

>La comune sintassi di un comando kubectl è:
```bash
kubectl action resource
```

Questo comando esegue la specifica **azione** (come ***create***, ***describe*** o ***delete***) sulla **risorsa specificata** (come ***node*** o ***deployment***).
Per ricevere ulteriori informazioni e parametri si può usare ==--help==
(Es. `kubectl get nodes --help`)

>Per vedere i nodi sul cluster eseguire:
```bash
kubectl get nodes
```
Successivamente Kubernetes sceglierà dove fare il deployment della nostra applicazione basandosi sulle risorse disponibili dei Nodi.


>Primo deployment di un app con `kubectl create deployment`.
>Questo comando necessita di:
>- **nome deployment**
>- **app image location**
```bash
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

Questo ha fatto un paio di robe:
- cercato per un nodo adatto dove un'istanza dell'applicazione possa eseguirsi
- programmata l'applicazione per essere eseguita su quel nodo
- configurato il cluster per riprogrammare l'istanza su un nuovo Nodo se necessita.

>Per vedere i deployment usare il comando:
```bash
kubectl get deployments
```

I **container** che sono in esecuzione dentro Kubernetes sono dentro una **rete privata isolata**. Di default **sono visibili dagli altri container e servizi all'interno dello stesso cluster Kubernetes**, ma non fuori da quella rete.

Il comando `kubectl proxy` crea un proxy che inoltra le comunicazioni alla rete del cluster.

>Apriamo un secondo terminale in cui avviamo il processo del **proxy**:
```bash
kubectl proxy
```

Così abbiamo messo in connessione il nostro computer con il cluster Kubernetes

>[!NOTE] Possiamo vedere tutte le API hostate attraverso l'endpoint del proxy.
```bash
curl http://localhost:8001/version
```

>Il server API crea automaticamente un **endpoint per ogni container** basandosi sul nome del container. Questo nome si può vedere attraverso il proxy.

```bash
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
```

Possiamo poi accedere al container attraverso l'API proxato eseguendo:
```bash
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/
```