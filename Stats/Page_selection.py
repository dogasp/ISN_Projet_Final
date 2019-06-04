from tkinter import *

sys.path.append("../Reseau")
from Stats.Page_stat import *
from Reseau.client import *

class Stats:
    def __init__(self, user):
        self.user = user
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.protocol()

        self.Gros_Titre_Sa_Mere = Label(self.root, text = "Page de sélection des graphs à afficher")
        self.Gros_Titre_Sa_Mere.place(x = 200, y = 20)

        self.games = get_player_score("dodo").keys()
        self.game_ToSend = "Flappy"
      
        self.listbox_1 = Listbox(self.root)
        self.listbox_1.place(x = 400, y = 60)
        self.listbox_1.insert(END, "Statistiques sur toi")
        self.listbox_1.insert(END, "Statistiques globales")
        self.listbox_1.bind("<ButtonRelease-1>", self.Select_mode)
        self.selected_mode = 0
#------------------------------------------
        self.listbox_2 = Listbox(self.root)
        self.listbox_2.place(x = 150, y = 60)
        self.listbox_2.insert(END, "tout les jeux")
        for elt in self.games:
            self.listbox_2.insert(END, elt)
        self.listbox_2.bind("<ButtonRelease-1>", self.Select_game)

#-----------------------------------------
        validate_button = Button(self.root, text = "validate", command = self.launch)
        validate_button.place(x = 500, y = 300)

        self.root.mainloop()

    def Select_game(self, event = None):
        a  =self.listbox_2.curselection()
        self.game_ToSend = self.listbox_2.get(a)

    def Select_mode(self, event = None):
        a = self.listbox_1.curselection()
        self.selected_mode = self.listbox_1.get(a)

        self.Encore_Une_Autre_Belle_Liste = Listbox(self.root)
        self.Encore_Une_Autre_Belle_Liste.place(x = 500, y = 60)
        self.Encore_Une_Autre_Belle_Liste.insert(END, "Application")
        self.Encore_Une_Autre_Belle_Liste.insert(END, "Thermique")
        self.Encore_Une_Autre_Belle_Liste.bind("<ButtonRelease-1>", self.Select_graphType)
        self.selected_mode = "Application"

    def Select_graphType(self, event = None):
        a = self.Encore_Une_Autre_Belle_Liste.curselection()
        self.type_stats = self.Encore_Une_Autre_Belle_Liste.get(a)
    
    def launch(self):
        print(self.game_ToSend, self.selected_mode)

        if self.selected_mode == "Statistiques sur toi": #si la personne veut un graphique sur elle
            pass

        else: #si la personne veut des stats globales
            if self.type_stats == "Application":
                data = get_statistics()[0]
                moyennes = {}
                total = {}

                for game in data.keys():
                    moyennes[game] = data[game]["moyenne"][0]
                    total[game] = data[game]["moyenne"][1]
                                               
            else:
                if self.game_ToSend != "tout les jeux": #si c'est un jeu spécifique
                    x = []
                    y = []
                    for players in get_game_score_list(self.game_ToSend):
                        x.append(players[0])
                        y.append(players[1])

                    Graph_3(self.root,y, x)

                else: #le classement général tout jeux confondus
                    players = []
                    max_score = []
                    for player in get_score_list():
                        players.append(player[0])
                        max_score.append(player[1])


    def show_selected_grap(self):
        pass

