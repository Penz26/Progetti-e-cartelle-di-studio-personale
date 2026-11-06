---
date: 2026-11-06
tags:
  - Linux
subject: Sistemi
module: Boot Sequence
source:
---
# **BIOS vs UEFI**

## **Basic Input Output System (BIOS)**
>Lavora su 16bit , ideato per sistemi a 16bit

>**Sequenza**
>- pulsante di accessione
>- va in POST (Power on Self Test) verifica che ci sia l'hardware funzionate e collegato integro
>- carica il bootloader (GRUB stage 1)
>- GRUB stage 2 (monta il /boot, caricando il kernel e l'initramfs)
>- Monta la root
>- kernel avvia systemd (processo padre di tutti PID 1)
>- systemd lancia il resto dei servizi

![[BIOS boot sequence.excalidraw]]

**Come modificare la password di uno user direttamente dal kernel tramite l'interfaccia di GRUB**

>- Tenere premuto Shift all'avvio
>- schiacciare e per raggiungere questa schermata

>In questo caso il kernel avvierebbe in read only (ro) systemd senza farci vedere i vari passaggi (quiet) mostrando uno schermo nero, con in aggiunta l'immagine della distro (splash)
![[GRUB-normal.png]]

>Per far avviare una shell invece che systemd in modo read write dobbiamo fare:

![[GRUB-init-bash.png]]


## **Unified extensible Firmware Interfaces**
>Ideato per sostituire BIOS

![[Uefi Sequence]]


---

# **System V**
>lavora per runlevels, script in sequenza

0. Spegnimento
1. Single user mode
2. Multi user mode
3. Multi user mode + networking
4. MAI USATO :D 
5. Full Mode (multi user mode con interfaccia grafica)
# **Systemd**
>Lavora con boot targets

1. poweroff.target
2. rescue.target -->rescue service
3. multi-user.target --> sshd.service, docker.service
4. graphical.target --> display-manager.service, pulseaudio.service
5. reboot.target

>Vi è anche un default.target che è un link al .target attualmente impostato come predefinito

>Per vedere il default.target
```bash
systemctl get-default
```

>Per settare invece il default.target
```bash
systemctl set-default multiuser.target
```

>I file di ogni target sono in:
```bash
/etc/systemd/system
```

>I servizi da lanciare per ogni target sono in:
```bash
/usr/lib/systemd/system
```

>La parte più importante dei service è ExecStart:

>Una volta fatte delle modifiche bisogna fare il reload del demone system
```bash
systemctl daemon-reload
```


```bash
systemctl list-unit-files
```

>Per mascherare un servizio
```bash
systemctl mask ssh.service
```

>Crea un file in /etc/systemd/system/ssh.service.
>**==🔴QUESTO FILE ESSENDO IN UNA CARTELLA CON UNA PRIORITA' MAGGIORE FA L'OVERRIDE DEL FILE IN /usr/lib/systemd/system/sshd.service==**

>Per togliere il mask al servizio
```bash
systemctl unmask ssh.service
```


>Per configurare servizi a livello di user bisogna creare nella directory:
```bash
~/.config/systemd/user/nome.service
```

>Questi servizi esistono solo per quello user, per far si che possano esistere anche quando lo user non è loggatto:
```bash
userctl enable-lingering
```

