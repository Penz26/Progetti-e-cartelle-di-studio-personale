from tkinter import *  #importa tutto il modulo tkinter

#ELEMENTI DELLA GUI:

#WIDGETS = elementi della GUI: bottoni, caselle di testo, etichette, immagini, ecc...
#WINDOWS = serve come contenitore  per conservare questi widget

window = Tk() # inizializzata un istanza di una finestra
window.geometry("1920x1080") #impostiamo la larghezza e l'altezza della nostra finestra
window.title("Prima GUI")

#Per usare un' immagine come icona dobbiamo prima trasformarla in una PhotoImage
#icon = PhotoImage(file='logo.png') 
#e poi metterla come argomento nella funzione:
#window.iconphoto(True,icon)
window.config(background="azure")


#ETICHETTA: un area widget che contiene testo e/o un immagine all' interno di una finestra

#photo = PhotoImage(file="logo.png")
label = Label(window,text = "Prima etichetta di Manuel", #funziona come un costruttore (finestra,testo/img, altri argomenti (colore,font,ecc))
              font = ("Arial", 20, "italic"), 
              fg="red",bg="black", #fg = colore testo , bg = colore background
              relief=RAISED,    #stile del bordo
              bd=10,   #bordo spessore
              padx=20, #diamo dello spazio sull' asse x per il testo
              pady=50, #diamo dello spazio sull' asse y per il testo
              #image=photo,
              compound="bottom") #posizione dell'immagine rispetto al testo

#Per mostrare effettivamente l'etichetta nella nostra GUI dobbiamo usare pack oppure place
label.pack() #mostra l'etichetta al centro automaticamente
#label.place(x=0, y=0) mentre con place scegliamo noi dove mostrare la nostra label



    
#BOTTONI: pulsanti
count = 0
def click():
    global count 
    count +=1
    print("You clicked the button", count, "times.")
button = Button(window,         #stessa roba per label, funziona come costruttore (finestra, ecc)
                text = "Click Me",
                command = click,   #callback di una funzione
                font = ("Comic Sans", 30),
                fg = "#00FF00",
                bg ="black",
                activeforeground="#00FF00",     #colore del testo quando viene premuto il bottone (stato ACTIVE)
                activebackground= "Black",        #colore del background quando viene premuto il bottone (stato ACTIVE)
                #state = DISABLED,                 #SE volessimo disattivare un bottono mettiamo state DISABLED
                #image = photo,
                compound = "bottom"
                )                 
button.pack()

#ENTRY WIDGET: casella di testo che accetta una singola riga di input dell'utente

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED) #possiamo fare in modo che dopo che l'utente ha inserito il suo nome venga disattivata la casella di testo
def delete():
    entry.delete(0, END) #per eliminare tutto il testo all'interno di una entrybox usiamo
                        # .delete, il primo argomento è la posizione da cui partire mentre il secondo è dove finire

def backspace():
    entry.delete(len(entry.get())-1, END) #prende la lunghezza dell'intera stringa inserita dall'utente e inizia da lì fino alla fine per cancellare


entry = Entry(window,   #diciamo dove vogliamo farla vedere
              font=("Arial", 50), #font etc
              fg="#00FF00",
              bg="black",
              show="*") #possiamo oscurare quello che inseriamo, come una password, con il parametro show=

#entry.insert(0,"Spongebob") #per applicare un testo di default sulla casella di testo
entry.pack(side=LEFT) #per far vedere qualcosa bisogna sempre mettere .pack, e possiamo dirgli dove posizionarla (RIGHT, LEFT)

submit_button = Button(window,text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

#CHECK BOX:
def messaggio():
    if (x.get()==1):
        print("Hai dato il tuo consenso")
    else:
        print("Non hai dato il tuo consenso")
x = IntVar()
check_button = Checkbutton(window,
                        text="Consento",
                        variable=x,
                        onvalue=1,   #Quando è stato cliccato la checkbox
                        offvalue=0,  #Quando non è stato cliccata la checkbox
                        command=messaggio,
                        fg="black",
                        bg="white",
                        padx=25,
                        pady=10
                        )   
check_button.pack()

#RADIO BUTTON: 
food = ["pizza", "pasta", "salame"]
y = IntVar()

def order():
    if(y.get()==0):
        print("Hai ordinato una pizza")
    elif(y.get()==1):
        print("Hai ordinato la pasta")
    else:
        print("Hai ordinato il salame")
for index in range(len(food)):
    radio_button = Radiobutton(window,
    text=food[index],
    value=index,  #assegna ad ogni bottone radio una valore diverso
    variable=y,  
    padx=25,
    pady=10,
    font=("Impact", 20),
    width=275,        #larghezza del bottone su cui cliccare
    indicatoron=0,     #0 equivale a niente pallino del bottone
    command=order
    )
    radio_button.pack(anchor=W)


window.mainloop() # mostra la finestra sullo schermo e ascolta per eventi