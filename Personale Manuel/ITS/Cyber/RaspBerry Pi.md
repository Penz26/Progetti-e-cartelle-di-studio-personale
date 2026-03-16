
>Abbiamo collegato un nuovo raspberry pi sulla rete e d'ora in poi lo useremo per farci da server e fare i nostri test/attacchi.

# Come trovare un dispositivo nuovo che si è collegato sulla rete?

- Il Raspberry ha installato su ssh, che opera sulla porta 22, con --open guardiamo quali dispositivi sulla rete hanno aperto quelle porte.

```Shell
sudo nmap -p 22,443,80 --open 192.168.100.0/24
```


- Raspberry ha "comprato" il prefisso MAC ADDRESS B8:27:EB, quindi possiamo scannerizzare la rete per vedere quel dispositivo

```Shell
sudo nmap -p 22,443,80 --open 192.168.100.0/24 | grep B8:27:EB  
```

## Come facciamo a vedere il nome della macchina?


---

# Bettercap per attacchi MITM
>Bettercap è un framework che permette di analizzare e attaccare reti wifi, bluetooth, IPv4/IPv6

