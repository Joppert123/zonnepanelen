import tkinter as tk

class Pagina(tk.Frame):
    def __init__(self, args):
        tk.Frame.__init__(self, args)
    def show(self):
        self.lift()

class Algemeen(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       label_instellingen = tk.Label(self, text="Instellingen", font="Verdana 16")
       label_naam = tk.Label(self, text="Naam", font="Verdana 10")
       entry_naam = tk.Entry(self)
       label_instellingen.place(x=10, y=15)
       label_naam.place(x=10, y=50)
       entry_naam.place(x=60, y=50)

class Temperatuursensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       label = tk.Label(self, text="This is Pagina 2")
       aanknop = tk.Button(self, text="Aan", width=10, height=5)
       aanknop.pack(side="left")
       label.pack(side="top", fill="both", expand=True)

class Lichtsensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       label = tk.Label(self, text="This is Pagina 3")
       label.pack(side="top", fill="both", expand=True)

class Ultrasonoorsensor(Pagina):
   def __init__(self, args):
       Pagina.__init__(self, args)
       label = tk.Label(self, text="This is Pagina 4")
       label.pack(side="top", fill="both", expand=True)

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
