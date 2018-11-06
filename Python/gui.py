from tkinter import *
import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import *

# De klasse Pagina is de hoofdklasse van de verschillende 'pagina's' van de Centrale. Er wordt een frame gemaakt wat elke 'pagina' kan gebruiken.

class Pagina(tk.Frame):
    def __init__(self, args):
        tk.Frame.__init__(self, args)
    def show(self):
        self.lift()

class Algemeen(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       #Label voor de titel van de 'pagina'
       label_titel = tk.Label(self, text="Algemeen", font="Verdana 16 bold")

       # Labels voor instellingen, naam en een invulveld voor de naam van de besturingseenheid
       label_instellingen = tk.Label(self, text="Instellingen", font="Verdana 16")
       label_naam = tk.Label(self, text="Naam", font="Verdana 10")
       entry_naam = tk.Entry(self)

       # Het plaatsen van de objecten in het frame
       label_titel.place(x=10, y=15)
       label_instellingen.place(x=10, y=60)
       label_naam.place(x=10, y=100)
       entry_naam.place(x=60, y=100)

class Temperatuursensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       #Label voor de titel van de 'pagina'
       label_titel = tk.Label(self, text="Temperatuursensor", font="Verdana 16 bold")

       # Aan- en uitknop voor het inschakelen van de sensor
       aanknop = tk.Button(self, text="Aan", background="Green", width="20", height="4")
       uitknop = tk.Button(self, text="Uit", background="Red", width="20", height="4")

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

       #Plaatsen van het label object in het frame
       label_titel.place(x=10, y=15)

       # Dropdownbox plaatsen in het frame
       popupMenu.place(x=800, y=250)

       # Aan- en uitknop plaatsen in het frame
       aanknop.place(x=50, y=60)
       uitknop.place(x=225, y=60)

       # Label van dummygrafiek en refreshrate label plaatsen in het frame
       grafiek.place(x=125, y=400)
       refreshrate_tekst.place(x=800, y=200)

       # #grafiek
       # f = Figure(figsize=(5,5), dpi=100)
       # a = f.add_subplot(111)
       # a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
       #
       # canvas = FigureCanvasTkAgg(f, self)
       # canvas.show()
       # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
       #
       # toolbar = NavigationToolbar2TkAgg(canvas, self)
       # toolbar.update()
       # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Lichtsensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       #Label voor de titel van de 'pagina'
       label_titel = tk.Label(self, text="Lichtsensor", font="Verdana 16 bold")

       # Aan- en uitknop voor het inschakelen van de sensor
       aanknop = tk.Button(self, text="Aan", background="Green", width="20", height="4")
       uitknop = tk.Button(self, text="Uit", background="Red", width="20", height="4")

       # Voorlopige invulling van de grafiek, het is nu nog alleen een label maar hier komt later een volledige grafiek met data van de sensor
       grafiek = tk.Label(self, text="Hier komt de grafiek", font="Verdana 14")

       # Label voor het instellen van de refreshrate van de sensor
       refreshrate_tekst = tk.Label(self, text="Refreshrate:", font="Verdana 14")

       # Variabele voor de dropdownbox voor het instellen van de refreshrate van de sensor, momenteel is de functie nog niet geïmplementeerd
       tkvar = StringVar(root)

       # De verschillende refreshrates die de gebruiker kan kiezen plus de standaardwaarde
       refresh_opties = ('30 seconden', '40 seconden', '50 seconden', '60 seconden')
       tkvar.set('40 seconden')

       # Dropdownbox aanmaken
       popupMenu = OptionMenu(self, tkvar, *refresh_opties)

       # Dropdownbox plaatsen in het frame
       popupMenu.place(x=800, y=250)

       #Plaatsen van het label object in het frame
       label_titel.place(x=10, y=15)

       # Aan- en uitknop plaatsen in het frame
       aanknop.place(x=50, y=60)
       uitknop.place(x=225, y=60)

       # Label van dummygrafiek en refreshrate label plaatsen in het frame
       grafiek.place(x=125, y=400)
       refreshrate_tekst.place(x=800, y=200)

class Ultrasonoorsensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       #Label voor de titel van de 'pagina'
       label_titel = tk.Label(self, text="Ultrasonoorsensor", font="Verdana 16 bold")

       # Aan- en uitknop voor het inschakelen van de sensor
       aanknop = tk.Button(self, text="Aan", background="Green", width="20", height="4")
       uitknop = tk.Button(self, text="Uit", background="Red", width="20", height="4")

       # Voorlopige invulling van de grafiek, het is nu nog alleen een label maar hier komt later een volledige grafiek met data van de sensor
       grafiek = tk.Label(self, text="Hier komt de grafiek", font="Verdana 14")

       # Label voor het instellen van de refreshrate van de sensor
       refreshrate_tekst = tk.Label(self, text="Refreshrate:", font="Verdana 14")

       # Variabele voor de dropdownbox voor het instellen van de refreshrate van de sensor, momenteel is de functie nog niet geïmplementeerd
       tkvar = StringVar(root)

       # De verschillende refreshrates die de gebruiker kan kiezen plus de standaardwaarde
       refresh_opties = ('30 seconden', '40 seconden', '50 seconden', '60 seconden')
       tkvar.set('50 seconden')

       # Dropdownbox aanmaken
       popupMenu = OptionMenu(self, tkvar, *refresh_opties)

       # Dropdownbox plaatsen in het frame
       popupMenu.place(x=800, y=250)

       #Plaatsen van het label object in het frame
       label_titel.place(x=10, y=15)

       # Aan- en uitknop plaatsen in het frame
       aanknop.place(x=50, y=60)
       uitknop.place(x=225, y=60)

       # Label van dummygrafiek en refreshrate label plaatsen in het frame
       grafiek.place(x=125, y=400)
       refreshrate_tekst.place(x=800, y=200)

class Modus(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)

       #Label voor titel 'pagina'
       label_titel = tk.Label(self, text="Modus", font="Verdana 16 bold")

       #Label voor de jaargetijden
       label_jaarg = tk.Label(self, text="Jaargetijde")

       #Label voor de weertypes
       label_weertype = tk.Label(self, text="Weertype")

       #Knoppen voor jaargetijden
       button_lente = tk.Button(self, text="Lente", width="20", height="4")
       button_zomer = tk.Button(self, text="Zomer", width="20", height="4")
       button_herfst = tk.Button(self, text="Herfst", width="20", height="4")
       button_winter = tk.Button(self, text="Winter", width="20", height="4")

       #Knoppen voor weertype
       button_droog = tk.Button(self, text="Droog", width="20", height="4")
       button_regen = tk.Button(self, text="Regen", width="20", height="4")
       button_sneeuw = tk.Button(self, text="Sneeuw", width="20", height="4")
       button_storm = tk.Button(self, text="Storm", width="20", height="4")

       #Plaatsen van labels
       label_titel.place(x=10, y=15)
       label_jaarg.place(x=200, y=100)
       label_weertype.place(x=800, y=100)

       #Plaatsen van buttons voor jaargetijden
       button_lente.place(x=200, y=150)
       button_zomer.place(x=375, y=150)
       button_herfst.place(x=200, y=250)
       button_winter.place(x=375, y=250)

       #Plaatsen van buttons voor weertypes
       button_droog.place(x=800, y=150)
       button_regen.place(x=975, y=150)
       button_sneeuw.place(x=800, y=250)
       button_storm.place(x=975, y=250)



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


        b1 = tk.Button(buttonframe, text="Algemeen", command=p1.lift, width="20", font="Verdana 8")
        b2 = tk.Button(buttonframe, text="Temperatuursensor", command=p2.lift, width="20", font="Verdana 8")
        b3 = tk.Button(buttonframe, text="Lichtsensor", command=p3.lift, width="20", font="Verdana 8")
        b4 = tk.Button(buttonframe, text="Ultrasonoorsensor", command=p4.lift, width="20", font="Verdana 8")
        b5 = tk.Button(buttonframe, text="Modus", command=p5.lift, width="20", font="Verdana 8")

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
