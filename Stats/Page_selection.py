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

        self.games = get_player_score("dodo").keys()
        self.game_ToSend = self.games[0]

        self.Une_Belle_Liste = Listbox(self.root)
        self.Une_Belle_Liste.place(x = 150, y = 60)
        for elt in self.games:
            self.Une_Belle_Liste.insert(END, elt)
        self.Une_Belle_Liste.bind("<ButtonRelease-1>", self.Select_game)

        self.Une_Autre_Belle_Liste = Listbox(self.root)
        self.Une_Autre_Belle_Liste.place(x = 400, y = 60)
        self.Une_Autre_Belle_Liste.insert(END, "Statistiques sur toi")
        self.Une_Autre_Belle_Liste.insert(END, "Statistiques globales")
        self.Une_Autre_Belle_Liste.bind("<ButtonRelease-1>", self.Select_mode)
        self.selected_mode = 0

        validate_button = Button(self.root, text = "validate", command = self.launch)

        #app = Graph_3(self.root)

        self.root.mainloop()

    def Select_game(self, event = None):
        a  =self.Une_Belle_Liste.curselection()
        self.game_ToSend = self.Une_Belle_Liste.get(a)

    def Select_mode(self, event = None):
        self.selected_mode = self.Une_Autre_Belle_Liste.curselection()
    
    def launch(self):
        print(self.game_ToSend, self.Select_mode)