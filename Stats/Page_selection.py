from tkinter import *

sys.path.append("../Reseau")
from Stats.Page_stat import *
from Reseau.client import *

class Stats:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.protocol()

        self.Gros_Titre_Sa_Mere = Label(self.root, text = "Page de sélection des graphs à afficher")
        self.Gros_Titre_Sa_Mere.place(x = 200, y = 20)

        app = Graph_3(self.root)

        self.root.mainloop()
