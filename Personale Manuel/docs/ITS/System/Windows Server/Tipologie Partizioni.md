#Windows 

# **Cosa è una Partizione?**
>Una partizione è una divisione logica di questo spazio fisico in sezioni distinte e indipendenti. Anche se il disco o l'unità SSD è una sola il sistema operativo tratta ogni partizione come se fosse un disco fisso separato. 
>Esempio:
>C: e D: su Windows


---
# **Tipologie**

## **MBR (Legacy)**
>E' il sistema usato per decenni per partizionare i dischi in unità accessibili dai sistemi operativi.
>Funziona solo con dischi di dimensioni fino a 2TB

>Contiene la sequenza di comandi/istruzioni necessarie all'avvio (boot) del sistema operativo, tipicamente il boot loader del sistema e la tabella delle partizioni dei file system presenti nel disco. 

>Lo spazio viene diviso in tre tipologie principali:
>-**Partizione Primaria**
>>E' la sezione principale, progettata per ospitare i file del sistema operativo. Può essere resa "attiva" per consentire l'avvio del computer. Massimo 4
>
>**Partizione Estesa**
>>Poichè il sistema tradizionale permetteva di creare al massimo quattro partizioni primarie, la partizione estesa è stata creata per aggirare il limite. Non può essere resa "attivare" per consentire l'avvio di un S.O
>
>**Partizione Logica**
>>Sono le sotto-sezioni create all'interno della partizione estesa. Non possono avviare un sistema operativo ma sono perfette per archiviare dati personali


## **GPT**
>Standard per la definizione della tabella delle partizioni di un disco fisso che rappresenta l'evoluzione dell' MBR.

>Offre un meccanismo più flessibile per il partizionamento dei dischi, fa parte dello standard EFI il cui scopo è quello di sostituire il "vecchio" BIOS.

>GPT è la parte integrante dello standard UEFI ed utilizza degli identificativi gloabli (**GUID**) per riferirsi al contenuto di ciascuna partizione presente all'interno del disco.
>Supporta unità di archiviazione virtualmente illimitate
>E' inoltre possibile creare un numero illimitato di partizioni anche se la maggior parte dei sistemi operativi ne riduce il numero a 128.

>GPT memorizza anche i valori di controllo della ridondanza (CRC) per verificare che i dati siano intatti. 
---
# **Differenza tra backup e disk-image**
>Il termine backup si usa in generale per indicare un salvataggio dati o di sistema.
>Col termine disk-image si indica il salvataggio dell'intera struttura del disco fisico.

>Tool per disk-image
>**Macrium Reflect** o **Veeam Agent Free**