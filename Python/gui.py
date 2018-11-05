from tkinter import *
import tkinter as tk

# De klasse Pagina is de hoofdklasse van de verschillende 'pagina's' van de Centrale. Er wordt een frame gemaakt wat elke 'pagina' kan gebruiken.

class Pagina(tk.Frame):
    def __init__(self, args):
        tk.Frame.__init__(self, args)
    def show(self):
        self.lift()

class Algemeen(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       # Labels voor instellingen, naam en een invulveld voor de naam van de besturingseenheid
       label_instellingen = tk.Label(self, text="Instellingen", font="Verdana 16")
       label_naam = tk.Label(self, text="Naam", font="Verdana 10")
       entry_naam = tk.Entry(self)

       # Het plaatsen van de objecten in het frame
       label_instellingen.place(x=10, y=15)
       label_naam.place(x=10, y=50)
       entry_naam.place(x=60, y=50)

class Temperatuursensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       # Aan- en uitknop voor het inschakelen van de sensor
       aanknop = tk.Button(self, text="Aan", background="Green", width=20, height=4)
       uitknop = tk.Button(self, text="Uit", background="Red", width=20, height=4)

       # Voorlopige invulling van de grafiek, het is nu nog alleen een label maar hier komt later een volledige grafiek met data van de sensor
       grafiek = tk.Label(self, text="Hier komt de grafiek", font="Verdana 14")

       # Label voor het instellen van de refreshrate van de sensor
       refreshrate_tekst = tk.Label(self, text="Refreshrate:", font="Verdana 14")

       # Variabele voor de dropdownbox voor het instellen van de refreshrate van de sensor, momenteel is de functie nog niet geïmplementeerd
       tkvar = StringVar(root)

       # De verschillende refreshrates die de gebruiker kan kiezen plus de standaardwaarde
       refresh_opties = ('30 seconden', '40 seconden', '50 seconden', '60 seconden')
       tkvar.set('30 seconden')

       # Dropdownbox aanmaken
       popupMenu = OptionMenu(self, tkvar, *refresh_opties)

       # Dropdownbox plaatsen in het frame
       popupMenu.place(x=800, y=250)

       # Aan- en uitknop plaatsen in het frame
       aanknop.place(x=50, y=50)
       uitknop.place(x=225, y=50)

       # Label van dummygrafiek en refreshrate label plaatsen in het frame
       grafiek.place(x=125, y=400)
       refreshrate_tekst.place(x=800, y=200)

class Lichtsensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       aanknop = tk.Button(self, text="Aan", background="Green", width=20, height=4)
       uitknop = tk.Button(self, text="Uit", background="Red", width=20, height=4)
       aanknop.place(x=50, y=50)
       uitknop.place(x=225, y=50)

class Ultrasonoorsensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       aanknop = tk.Button(self, text="Aan", background="Green", width=20, height=4)
       uitknop = tk.Button(self, text="Uit", background="Red", width=20, height=4)
       aanknop.place(x=50, y=50)
       uitknop.place(x=225, y=50)

class Modus(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       label = tk.Label(self, text="This is Pagina 5")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, args):
        tk.Frame.__init__(self, args)
        p1 = Algemeen(self)
        p2 = Temperatuursensor(self)
        p3 = Lichtsensor(self)
        p4 = Ultrasonoorsensor(self)
        p5 = Modus(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        b1 = tk.Button(buttonframe, text="Algemeen", command=p1.lift, width=20, font="Verdana 8")
        b2 = tk.Button(buttonframe, text="Temperatuursensor", command=p2.lift, width=20, font="Verdana 8")
        b3 = tk.Button(buttonframe, text="Lichtsensor", command=p3.lift, width=20, font="Verdana 8")
        b4 = tk.Button(buttonframe, text="Ultrasonoorsensor", command=p4.lift, width=20, font="Verdana 8")
        b5 = tk.Button(buttonframe, text="Modus", command=p5.lift, width=20, font="Verdana 8")

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Centrale")
    root.wm_geometry("400x400")
    root.mainloop()
