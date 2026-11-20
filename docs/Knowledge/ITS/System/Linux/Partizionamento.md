---
date: 2026-11-20
tags:
  - Linux
subject: Sistemi
module: partizioni
source: https://www.alessioligabue.it/blog/lvm-linux-logical-volume-manager
---
# **Tipi di Filesystem**
>Per capire come operano le partizioni dobbiamo capire prima le differenze tra essi:

## **EXT4**
>**Fourth Extended Filesystem**

>- E' lo **standard** di Linux, il filesystem più collaudato
>- **Journaling**: registra le operazioni prima di scriverle, prevenendo corruzioni in caso di crash
>- **Flessibilità**: supporta sia l'estensione (**extend**) che la riduzione (**shrink**) offline tramite resize2fs
>- **Uso**: server generici, desktop e ambienti ad alta stabilità

## **XFS**
>- **Prestazioni altissime**
>- **Parallel I/O**: progettato per gestire carichi di I/O concorrenti elevati e file di grandi dimensioni
>- **Journaling**: integrato e ottimizzato per operazioni pesanti
>- **Uso**: database e carichi enterprise

>[!WARNING] **NON supporta lo shrink** solo l'estensione (xfs_growfs)

## **BTRFS**
>**B-tree File System**

>- **Archittetura Copy-on-Write**: non sovrascrive i blocchi esistenti durante la modifica, ma scrive su blocchi nuovi preservando lo stato precedente
>- **Funzionalità avanzate**: gestione nativa di snapshot, compressione trasparente (zstd) e checksum per proteggere dal data corruption
>- **Flessibilità**: ridimensionabile sia in aumento che in riduzione a caldo
>- **Uso ideale**: sistemi moderni con necessità di backup/rollback istantanei e storage resiliente

---
# **Creazione di una partizione**

```shell
sudo parted /dev/vdb

#Così avviamo la partizione in modo interattivo

mklabel
#scegliamo gpt

mkpart
#Partition name = etichetta a piacere dati
#File system type = ext4
#start = indica il punto di inizio (0% dall'inizio , 1Mib consigliato)
#end = indica la fine della partizione (es. 50GiB)

print
#controlliamo che la tabella elenchi tutte le partizioni
```

>Ora però questo filesystem non è montabile.
>Per poterlo mandare dobbiamo dirgli ==veramente== il Filesystem

```shell
sudo mkfs -t ext4 /dev/vdb1
```

>Ora lo montiamo (temporaneamente) con:
```bash
sudo mkdir -p /mnt/dati
sudo mount /dev/vdb1 /mnt/dati
```

---
# Montare una partizione di swap

```bash
sudo parted /dev/sdX

mkpart
#Partition name = swap
#Filesystem type = linux-swap
#Start = 50GiB
#End = 58GiB
```

>Ora, come prima, dobbiamo scrivergli i metadati e l'UUID nella partizione
```bash
sudo mkswap /dev/sdX2
```

>Attiviamo la partizione
```bash
sudo swapon /dev/sdX2
```

>[!IMPORTANT] **Per ora queste partizioni vivono solo su questo boot, se riavviamo il pc SCOMPARE TUTTO**


---
# **Montare automaticamente un disco**
>Rendiamo persistenti questi mount

Il processo che si occupa di montare in automatico le partizioni al boot è `fstab` i cui file di configurazione sono in `/etc/fstab`

```bash
UUID=inserisci-qui-il-tuo-uuid   mountpoint   type   option   0(dump)   0(pass)
```

**Componenti della configurazione:**
- **UUID**: Identificatore Univoco della partizione (ottenibile con blkid /dev/sdX2)
- **mountpoint**: dove montare la partizione (cartella es. /srv/web_app) 
- **type**: tipo di filesystem (ext4, btrfs, swap)
- **option**: parametri di montaggio (defaults,nofail per i filesystem sw per gli swap)
- **dump**: campo usato di backup (solitamente 0)
- **pass**: stabilisce l'ordine in cui il sistema controlla l'integrità del sistema (1 partizione di root, 2 per tutte le altre partizioni Linux, 0 per gli swap)
---
# **Modificare una partizione**

>[!WARNING] **Prima conviene smontare entrambe le partizioni su cui vogliamo operare**

```bash
sudo umount /dev/sdX1
sudo umount /dev/sdX2

#Controlliamo con lsblk
```

## **Eliminiamo una partizione e allarghiamo la prima**

>[!NOTE] **Prima facciamo il resize della partizione, ==POI== modifichiamo il filesystem**

>Avviamo parted in modalità interattiva (==Resize Partizione== **contenitore**):
```bash
sudo parted /dev/sdX

print

rm 2

resizepart 
#Partition number: 1 
#Warning: yes
#End: 100% (specificare la nuova fine)

print #controlliamo

quit
```

>Ora lo espandiamo (==Resize Filesystem== **contenuto**):
```bash
sudo resize2fs /dev/sdX1
```

## **Riduciamo una partizione (Shrink)**

>[!NOTE] **Prima facciamo il resize del Filesystem, ==POI== modifichiamo la partizione**

>Smontiamo prima il disco da rimpicciolire:
```bash
sudo umount /dev/sdX1
```

>**==Riduciamo prima il filesystem==** (**contenuto**)
```bash
sudo resize2fs /dev/sdX1 48G #ridotto a 48G qualcosina in meno della partizione
```

>**==Riduciamo successivamente la partizione==** (**contenitore**)
```bash
sudo parted /dev/sdX

resizepart
#Partition number: 1
#Warning: yes
#End: 50GiB

print #controlliamo

quit
```

>Riespandiamo il FileSystem per occupare in modo sicuro la partizione
```bash
sudo resize2fs /dev/sdX1
```

---
# ZRAM
>E' un modulo del kernel che crea un dispositivo  a blocchi compresso in Ram.

Praticamente quando la memoria ram inizia a riempirsi, invece che scrivere sul disco, il kernel le comprime al volo (con zstd) e le conserva in questo blocco di RAM dedicata (zram)

- Rapporto di compressione: I dati in Ram comprimono con un rapporto di 2:1 o 3:1 
- **velocità**: leggere e decomprimere è infinitamente più veloce di leggere su un disco
- **zero usura dei dischi**

---
# **LVM (Logical Volume Manager)**
>Livello di astrazione tra dischi fisici e filesystem

>[!NOTE] LVM unisce lo spazio di uno o più dischi in un unico contenitore flessibile, permettendo di creare, ridimensionare o spostare volumi al volo

## **3 Livelli**
>1. **Physical Volume (PV):** sono i dischi fisici interi (/dev/sdb) o le partizioni inizializzati per essere gestiti da LVM
>   Dona lo spazio fisico al pool di LVM
>   **Comando chiave**: `pvcreate`

>2. **Volume Group (VG):** un unico pool di storage che unisce uno o più Physical Volume sommandone la capacità totale
>   Se si hanno 2 dischi da 1TB si può creare un unico **VG** da 2TB, unica unità da cui attingere lo spazio
>   **Comando chiave:** `vgcreate`

>3. **Logical Volume (LV):** le partizioni virtuali prese dal Volume Group su cui viene creato il filesystem
>   Dal **VG** da 2TB si possono creare un LV da 50GB per `/var`, uno da 100GB `/home` . Questi LV funzionano come le partizioni tradizionali ma **==possono essere ridimensionati==**
>   **Comando chiave:** `lvcreate`

## **Creazione  sistema LVM**
>Esempio con due nuovi dischi **/dev/sdb /dev/sdc**

### **Creazione dei Physical Volumes (PV) Fase 1**

>Prima identifichiamo i dischi con `lsblk`
```bash
lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0  100G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   99G  0 part /
sdb      8:16   0  500G  0 disk 
sdc      8:32   0  500G  0 disk 
```

>Ora li inizializziamo come **PV**
```bash
sudo pvcreate /dev/sdb /dev/sdc
  Physical volume "/dev/sdb" successfully created.
  Physical volume "/dev/sdc" successfully created.
```

>Si può successivamente verificare con `pvs` o `pvdisplay`

### **Creazione del Volume Group (VG) Fase 2**

>Uniamo i due PV in un unico Volume Group con nome `vg_data`
```bash
sudo vgcreate vg_data /dev/sdb /dev/sdc
  Volume group "vg_data" successfully created
```

>Si può successivamente verificare con `vgs` o `vgdisplay`

### **Creazione del Logical Volume (LV) Fase 3**

>Dal VG appena creato creiamo un LV con nome `lv_webapp`
```bash
sudo lvcreate -n lv_webapp -L 100G vg_data
  Logical volume "lv_webapp" created.
```

### **Formattare e Montare il LV Fase 4**

>Creiamo il filesystem su di esso
```bash
sudo mkfs.ext4 /dev/vg_data/lv_webapp
```

>Ora creiamo la directory in cui montarlo
```bash
sudo mkdir -p /srv/webapp
sudo mount /dev/vg_data/lv_webapp /srv/webapp
```

>Ora dobbiamo renderlo permanente modificando /etc/fstab
>(Possiamo usare il percorso o l'UUID)
```bash
sudo nano /etc/fstab

# Aggiungi questa riga in fondo al file:
/dev/mapper/vg_data-lv_webapp  /srv/webapp  ext4  defaults  0  0
```

## **Gestione Avanzata**
>Il motivo migliore per usare LVM sta nella facilità della gestione con comandi come `lvextend` (estendi) `lvreduce` (ridurre)  `vgextend`

### **Come estendere un volume LVM**

>[!NOTE] Estendiamo prima il volume e poi il filesystem

>Estendiamo il **Logical Volume** (contenitore)
```bash
sudo lvextend -L +50G /dev/vg_data/lv_webapp
  Size of logical volume vg_data/lv_webapp changed from 100.00 GiB (25600     extents) to 150.00 GiB (38400 extents).
  Logical volume vg_data/lv_webapp successfully resized.
```

>Estendiamo il Filesystem (contenuto)
```bash
sudo resize2fs /dev/vg_data/lv_webapp
resize2fs 1.45.5 (07-Jan-2020)
Filesystem at /dev/vg_data/lv_webapp is mounted on /srv/webapp; on-line resizing required
old_desc_blocks = 13, new_desc_blocks = 19
The filesystem on /dev/vg_data/lv_webapp is now 39321600 (4k) blocks long.
```

### **Come ridurre un volume LVM**

>Smontiamo il filesystem
```bash
sudo umount /srv/webapp
```

>Riduciamo il filesystem, tenendo un GiB in meno rispetto al LV
```bash
sudo resize2fs /dev/vg_data/lv_webapp 79G
```

>Riduciamo il Logical Volume
```bash
sudo lvreduce -L 80G /dev/vg_data/lv_webapp
```

>Riespandiamo il Filesystem per occupare esattamente gli 80G del Volume
```bash
sudo resize2fs /dev/vg_data/lv_webapp
```

>Rimontiamo
```bash
sudo mount /srv/webapp
```
