import time
import threading
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from protocol import *
from connect import *
from graph_protocol import *

from tkinter import *
import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

# De klasse Pagina is de hoofdklasse van de verschillende 'pagina's' van de Centrale. Er wordt een frame gemaakt wat elke 'pagina' kan gebruiken.

Connect()
Main()


class Pagina(tk.Frame):
    def __init__(self, args):
        tk.Frame.__init__(self, args)

    def show(self):
        self.lift()


class Algemeen(Pagina):
    def __init__(self, args):
        Pagina.__init__(self, args)

        sunscreenText = ""
        sunscreenManualText = ""

        def getSunscreenStatus():
            command = "get_sunscreen_status"
            sunscreenStatus = int(
                Transmit(connections[0].ser, command).hex(), 16)

            if sunscreenStatus == 0:
                sunscreenText = "Closed"

            else:
                sunscreenText = "Opened"

            getSunscreenStatusField.config(text=sunscreenText)

        def getSunscreenMinExtend():
            command = "get_sunscreen_min_extend"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getSunscreenMinExtendField.config(text=response)

        def getSunscreenMaxExtend():
            command = "get_sunscreen_max_extend"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getSunscreenMaxExtendField.config(text=response)

        def setSunscreenMinExtend():
            command = ("set_sunscreen_min_extend="
                       + setSunscreenMinExtendField.get())
            response = int(Transmit(connections[0].ser, command).hex(), 16)

        def setSunscreenMaxExtend():
            command = ("set_sunscreen_max_extend="
                       + setSunscreenMaxExtendField.get())
            response = int(Transmit(connections[0].ser, command).hex(), 16)

        def getManualMode():
            command = "get_sunscreen_manual"
            sunscreenManualmode = int(
                Transmit(connections[0].ser, command).hex(), 16)

            if sunscreenManualmode == 0:
                sunscreenManualText = "Auto mode"

            else:
                sunscreenManualText = "Manual mode"

            getSunscreenStatusField.config(text=sunscreenManualText)

        def setManualMode():
            command = ("set_sunscreen_manual" + setManualModeField.get())
            response = int(Transmit(connections[0].ser, command).hex(), 16)

        def sunscreenExtend():
            command = "sunscreen_extend"
            response = int(Transmit(connections[0].ser, command).hex(), 16)

        def sunscreenRetract():
            command = "sunscreen_retract"
            response = int(Transmit(connections[0].ser, command).hex(), 16)

        # Label voor de titel van de 'pagina'
        label_titel = tk.Label(self, text="Algemeen", font="Verdana 16 bold")

        # Labels voor instellingen, naam en een invulveld voor de naam van de besturingseenheid
        label_sunscreen = tk.Label(self, text="Sunscreen", font="Verdana 16")

        # Sunscreen fields for get
        getSunscreenStatusField = tk.Label(self, text="")
        getSunscreenMinExtendField = tk.Label(self, text="")
        getSunscreenMaxExtendField = tk.Label(self, text="")
        getManualModeField = tk.Label(self, text="")

        # Sunscreen button for get
        getSunscreenStatusButton = tk.Button(
            self, text="Get Sunscreen Status", width="30", height="2", command=getSunscreenStatus)
        getSunscreenMinExtendButton = tk.Button(
            self, text="Get Sunscreen Mininmal Extend", width="30", height="2", command=getSunscreenMinExtend)
        getSunscreenMaxExtendButton = tk.Button(
            self, text="Get Sunscreen Maximum Extend", width="30", height="2", command=getSunscreenMaxExtend)

        # Sunscreen button for set
        setSunscreenMinExtendButton = tk.Button(
            self, text="Set Sunscreen Mininmal Extend", width="30", height="2", command=setSunscreenMinExtend)
        setSunscreenMaxExtendButton = tk.Button(
            self, text="Set Sunscreen Maximum Extend", width="30", height="2", command=setSunscreenMaxExtend)

        # Sunscreen manual functions
        sunscreenExtendButton = tk.Button(
            self, text="Extend Sunscreen", width="30", height="2", command=sunscreenExtend)
        sunscreenRetractButton = tk.Button(
            self, text="Retract Sunscreen", width="30", height="2", command=sunscreenRetract)

        # Sunscreen button for manual
        getManualModeButton = tk.Button(
            self, text="Get Manual Mode", width="30", height="2", command=getManualMode)
        setManualModeButton = tk.Button(
            self, text="Set Manual Mode", width="30", height="2", command=setManualMode)

        # Set fields
        setSunscreenMinExtendField = tk.Entry(self)
        setSunscreenMaxExtendField = tk.Entry(self)
        setManualModeField = tk.Entry(self)

        # Het plaatsen van de objecten in het frame
        label_titel.place(x=10, y=15)
        label_sunscreen.place(x=10, y=60)
        getSunscreenStatusButton.place(x=10, y=150)
        getSunscreenMinExtendButton.place(x=10, y=220)
        getSunscreenMaxExtendButton.place(x=10, y=290)
        getSunscreenStatusField.place(x=300, y=150)
        getSunscreenMinExtendField.place(x=300, y=220)
        getSunscreenMaxExtendField.place(x=300, y=290)

        setSunscreenMinExtendButton.place(x=10, y=360)
        setSunscreenMaxExtendButton.place(x=10, y=430)
        sunscreenExtendButton.place(x=10, y=500)
        sunscreenRetractButton.place(x=10, y=570)

        setSunscreenMinExtendField.place(x=250, y=370)
        setSunscreenMaxExtendField.place(x=250, y=440)

        getManualModeButton.place(x=10, y=640)
        setManualModeButton.place(x=10, y=710)

        getManualModeField.place(x=250, y=650)
        setManualModeField.place(x=250, y=730)


class Temperatuursensor(Pagina):
    def __init__(self, args):
        Pagina.__init__(self, args)

        def getTemperature():
            command = "get_temp"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getTemperatureField.config(text=response)

        def getMinTemp():
            command = "get_min_temp"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getMinTempField.config(text=response)

        def getMaxTemp():
            command = "get_max_temp"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getMaxTempField.config(text=response)

        def setMinTemp():
            command = ("set_min_temp=" + setMinTempField.get())
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            setMinTempField.config(text=response)

        def setMaxTemp():
            command = ("set_max_temp=" + setMaxTempField.get())
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            setMaxTempField.config(text=response)

        # Labels for get Temperature
        getTemperatureField = tk.Label(self, text="")
        getMinTempField = tk.Label(self, text="")
        getMaxTempField = tk.Label(self, text="")

        # Label voor de titel van de 'pagina'
        label_titel = tk.Label(
            self, text="Temperatuursensor", font="Verdana 16 bold")

        # Temperature buttons for get
        getTemperatureButton = tk.Button(
            self, text="Get Temperature", width="30", height="2", command=getTemperature)
        getMinTempButton = tk.Button(
            self, text="Get Minimum Temperature", width="30", height="2", command=getMinTemp)
        getMaxTempButton = tk.Button(
            self, text="Get Maximum Temperature", width="30", height="2", command=getMaxTemp)

        # Fields for set Temperature
        setMinTempField = tk.Entry(self)
        setMaxTempField = tk.Entry(self)

        # Sunscreen button for set
        setMinTempButton = tk.Button(
            self, text="Set Minimum Temperature", width="30", height="2", command=setMinTemp)
        setMaxTempButton = tk.Button(
            self, text="Set Maximum Temperature", width="30", height="2", command=setMaxTemp)

        # Variabele voor de dropdownbox voor het instellen van de refreshrate van de sensor, momenteel is de functie nog niet geïmplementeerd
        tkvar = StringVar(root)

        # De verschillende refreshrates die de gebruiker kan kiezen plus de standaardwaarde
        refresh_opties = ('30 seconden', '40 seconden',
                          '50 seconden', '60 seconden')
        tkvar.set('30 seconden')

        # Dropdownbox aanmaken
        popupMenu = OptionMenu(self, tkvar, *refresh_opties)

        # Grafiek maken
        connection = connections[0]
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], connection.data[0])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        def P():
            canvas.draw()

        for i in range(100):
            P()

        # Toolbar voor grafiek
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # Plaatsen van het label object in het frame
        label_titel.place(x=10, y=15)

        # Dropdownbox plaatsen in het frame
        popupMenu.place(x=630, y=650)

        # Place buttons in frame
        getTemperatureButton.place(x=630, y=200)
        getMinTempButton.place(x=630, y=270)
        getMaxTempButton.place(x=630, y=340)
        setMinTempButton.place(x=630, y=410)
        setMaxTempButton.place(x=630, y=480)

        # Place fields in frame for get
        getTemperatureField.place(x=920, y=200)
        getMinTempField.place(x=920, y=270)
        getMaxTempField.place(x=920, y=340)

        # Place fields in frame for set
        setMinTempField.place(x=870, y=420)
        setMaxTempField.place(x=870, y=490)

        # Grafiek plaatsen in het frame
        canvas.get_tk_widget().place(x=50, y=200)


class Lichtsensor(Pagina):
    def __init__(self, args):
        Pagina.__init__(self, args)

        def getLight():
            command = "get_light"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getLightField.config(text=response)

        def getSonarDistance():
            command = "get_sonar_distance"
            response = int(Transmit(connections[0].ser, command).hex(), 16)
            getSonarDistanceField.config(text=response)

        # Label voor de titel van de 'pagina'
        label_titel = tk.Label(self, text="Lichtsensor",
                               font="Verdana 16 bold")

        # Buttons for get light
        getLightButton = tk.Button(
            self, text="Get Light", width="30", height="2", command=getLight)
        getSonarDistanceButton = tk.Button(
            self, text="Get Sonar Distance", width="30", height="2", command=getSonarDistance)

        # Fields for light getters
        getLightField = tk.Label(self, text="")
        getSonarDistanceField = tk.Label(self, text="")

        # Variabele voor de dropdownbox voor het instellen van de refreshrate van de sensor, momenteel is de functie nog niet geïmplementeerd
        tkvar = StringVar(root)

        # De verschillende refreshrates die de gebruiker kan kiezen plus de standaardwaarde
        refresh_opties = ('30 seconden', '40 seconden',
                          '50 seconden', '60 seconden')
        tkvar.set('40 seconden')

        # Dropdownbox aanmaken
        popupMenu = OptionMenu(self, tkvar, *refresh_opties)

        # Grafiek maken
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        connection = connections[0]
        a.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], connection.data[1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        # Toolbar voor grafiek
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # Dropdownbox plaatsen in het frame
        popupMenu.place(x=630, y=650)

        # Plaatsen van het label object in het frame
        label_titel.place(x=10, y=15)

        # Getters plaatsen in frame
        getLightButton.place(x=630, y=200)
        getSonarDistanceButton.place(x=630, y=270)

        # Field for getters in frame
        getLightField.place(x=870, y=200)
        getSonarDistanceField.place(x=870, y=270)

        # Grafiek plaatsen in het frame
        canvas.get_tk_widget().place(x=50, y=200)


class Ultrasonoorsensor(Pagina):
    def __init__(self, args):
        Pagina.__init__(self, args)

        # Label voor de titel van de 'pagina'
        label_titel = tk.Label(
            self, text="Ultrasonoorsensor", font="Verdana 16 bold")

        # Aan- en uitknop voor het inschakelen van de sensor
        aanknop = tk.Button(
            self, text="Aan", background="Green", width="20", height="4")
        uitknop = tk.Button(
            self, text="Uit", background="Red", width="20", height="4")

        # Refresh handmatig
        refreshknop = tk.Button(self, text="Refresh", width="20", height="4")

        # Label voor het instellen van de refreshrate van de sensor
        refreshrate_tekst = tk.Label(
            self, text="Refreshrate:", font="Verdana 14")

        # Variabele voor de dropdownbox voor het instellen van de refreshrate van de sensor, momenteel is de functie nog niet geïmplementeerd
        tkvar = StringVar(root)

        # De verschillende refreshrates die de gebruiker kan kiezen plus de standaardwaarde
        refresh_opties = ('30 seconden', '40 seconden',
                          '50 seconden', '60 seconden')
        tkvar.set('50 seconden')

        # Dropdownbox aanmaken
        popupMenu = OptionMenu(self, tkvar, *refresh_opties)

        # Grafiek maken
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        connection = connections[0]
        a.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], connection.data[2])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        # Toolbar voor grafiek
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # Dropdownbox plaatsen in het frame
        popupMenu.place(x=800, y=250)

        # Plaatsen van het label object in het frame
        label_titel.place(x=10, y=15)

        # Aan- en uitknop plaatsen in het frame
        aanknop.place(x=50, y=60)
        uitknop.place(x=225, y=60)

        # Refresh handmatig knop plaatsen in het frame
        refreshknop.place(x=800, y=300)

        # Refreshrate label plaatsen in het frame
        refreshrate_tekst.place(x=800, y=200)

        # Grafiek plaatsen in het frame
        canvas.get_tk_widget().place(x=50, y=200)


class Modus(Pagina):
    def __init__(self, args):
        Pagina.__init__(self, args)

        # Label voor titel 'pagina'
        label_titel = tk.Label(self, text="Modus", font="Verdana 16 bold")

        # Label voor de jaargetijden
        label_jaarg = tk.Label(self, text="Jaargetijde")

        # Label voor de weertypes
        label_weertype = tk.Label(self, text="Weertype")

        # Knoppen voor jaargetijden
        button_lente = tk.Button(self, text="Lente", width="20", height="4")
        button_zomer = tk.Button(self, text="Zomer", width="20", height="4")
        button_herfst = tk.Button(self, text="Herfst", width="20", height="4")
        button_winter = tk.Button(self, text="Winter", width="20", height="4")

        # Knoppen voor weertype
        button_droog = tk.Button(self, text="Droog", width="20", height="4")
        button_regen = tk.Button(self, text="Regen", width="20", height="4")
        button_sneeuw = tk.Button(self, text="Sneeuw", width="20", height="4")
        button_storm = tk.Button(self, text="Storm", width="20", height="4")

        # Plaatsen van labels
        label_titel.place(x=10, y=15)
        label_jaarg.place(x=200, y=100)
        label_weertype.place(x=800, y=100)

        # Plaatsen van buttons voor jaargetijden
        button_lente.place(x=200, y=150)
        button_zomer.place(x=375, y=150)
        button_herfst.place(x=200, y=250)
        button_winter.place(x=375, y=250)

        # Plaatsen van buttons voor weertypes
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

        b1 = tk.Button(buttonframe, text="Algemeen",
                       command=p1.lift, width="20", font="Verdana 8")
        b2 = tk.Button(buttonframe, text="Temperatuursensor",
                       command=p2.lift, width="20", font="Verdana 8")
        b3 = tk.Button(buttonframe, text="Lichtsensor",
                       command=p3.lift, width="20", font="Verdana 8")
        b4 = tk.Button(buttonframe, text="Ultrasonoorsensor",
                       command=p4.lift, width="20", font="Verdana 8")
        b5 = tk.Button(buttonframe, text="Modus",
                       command=p5.lift, width="20", font="Verdana 8")

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
    root.wm_geometry("1920x1080")
    # root.mainloop()
    while True:
        root.update_idletasks()
        root.update()
