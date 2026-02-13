import time

print(time.ctime(0))    #Converte un tempo espresso in secondi dall' epoca in una stringa leggibile
                        #epoca = quando il tuo computer pensa che sia iniziato il tempo (punto di riferenza)

print(time.time()) #printa quanti secondi sono passati dall' epoca

print(time.ctime(time.time())) #prende come argomento la funzione time di time (time.time) e viene poi covertita in una stringa leggibile con time.ctime
#Dà la data odierna

time_object = time.localtime()
#print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) #time.strftime formatta il tempo in stringa in base a un formato specifico che si sceglie
print(local_time)
#Codice,Significato, Esempio
#%d, Giorno del mese (01-31),09
#%m, Mese            (01-12),01
#%Y, Anno a 4 cifre,    2026
#%H, Ora             (00-23),19
#%M, Minuto          (00-59),15
#%S, Secondo         (00-59),30
#%A, Nome del giorno 
#    della 
#    settimana,        Friday
#%B, Nome del mese 
#       completo,     January

time_object2 = time.gmtime() #time.gmtime() trova l' UTC ovvero il Tempo Coordinato Universale da cui ci si basa per tutti gli orari 
print(time_object2)
time_string = "9 January, 2026"
time_object3 = time.strptime(time_string, "%d %B, %Y") #converte una stringa con una data/valore di tempo in un oggetto temporale 
#                                                       time.struct_time(tm_year=2026, tm_mon=1, tm_mday=9, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=9, tm_isdst=-1)
print(time_object3)
#Anno :  Mese : Numero Giorno : Ore : Minuti : Secondi : Giorno Settimanale partendo da 0 con Lunedì
time_tuple = (2020, 4, 20, 16, 20, 59, 1, 7, 4)
time_string2 = time.asctime(time_tuple) #converte una tupla di valori temporali in una stringa leggibile
print(time_string2)

#con time.mktime invece prende una tupla di valori temporali e trova quanti secondi sono trascorsi dall' epoca
#time_string2 = time.mktime(time_tuple) 
#print(time_string2)