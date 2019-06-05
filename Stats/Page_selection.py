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

        self.titre = Label(self.root, text = "Page de sélection des graphs à afficher")
        self.titre.place(x = 200, y = 20)

        self.games = get_player_score("dodo").keys()
        self.game_ToSend = "Flappy"

        self.listbox_1 = Listbox(self.root)
        self.listbox_1.place(x = 50, y = 60)
        self.listbox_1.insert(END, "Statistiques sur toi")
        self.listbox_1.insert(END, "Statistiques globales")
        self.listbox_1.bind("<ButtonRelease-1>", self.get_variable_1)
        self.selected_mode = 0

        self.listbox_2 = Listbox(self.root)
        self.listbox_2.place(x = 200, y = 60)
        self.listbox_2.insert(END, "Statistiques sur Application")
        self.listbox_2.insert(END, "Statistiques sur jeu")
        self.listbox_2.bind("<ButtonRelease-1>", self.Select_mode)
        self.selected_mode2 = 0

        self.select_graph_liste_game = np.array([
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 2, 3, 0, 1, 2, 3, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0])

        self.select_graph_liste_game.resize((8,2,4))

        self.liste_jeux_app = ["tout les jeux","Tete","Snake","Ghost","Minesweeper","Tetris","Pendu","Pong","Space"]
        self.liste_mode_listbox_1 = ["Statistiques sur toi","Statistiques globales"]

        validate_button = Button(self.root, text = "validate", command = self.launch)
        validate_button.place(x = 500, y = 300)

        self.root.mainloop()

    def get_variable_1(self, event = None):
        a = self.listbox_1.curselection()
        self.selected_mode = self.listbox_1.get(a)
        self.variable2 = self.liste_mode_listbox_1.index(self.selected_mode)

    def Select_mode(self, event = None):
        a  = self.listbox_2.curselection()
        self.selected_mode2 = self.listbox_2.get(a)

        if self.selected_mode2 == "Statistiques sur Application":
            self.listbox_3 = Listbox(self.root)
            self.listbox_3.place(x = 350, y = 60)
            self.listbox_3.insert(END, "stat1")
            self.listbox_3.insert(END, "stat2")
            self.listbox_3.insert(END, "stat3")
            self.listbox_3.insert(END, "stat4")
            self.listbox_3.bind("<ButtonRelease-1>", self.get_variable_3)
        else:
            self.listbox_3_bis = Listbox(self.root)
            self.listbox_3_bis.place(x = 350, y = 60)
            self.listbox_3_bis.insert(END, "tout les jeux")
            for elt in self.games:
                self.listbox_3_bis.insert(END, elt)
            self.listbox_3_bis.bind("<ButtonRelease-1>", self.get_variable_2)

    def get_variable_2(self, event = None):
        a = self.listbox_3_bis.curselection()
        self.selected_mode3 = self.listbox_3_bis.get(a)
        self.variable = self.liste_jeux_app.index(self.selected_mode3)
        self.Select_graphType()

    def get_variable_3(self, event = None):
        a = self.listbox_3.curselection()
        self.selected_mode4 = self.listbox_3.get(a)
        self.Select_graphType()


    def Select_graphType(self, event = None):
        self.listbox_4 = Listbox(self.root)
        self.listbox_4.place(x = 500, y = 60)

        for z in range(4):
            if self.select_graph_liste_game[self.variable][self.variable2][z]== 1:
                self.listbox_4.insert(END, "Graph_1")
            if self.select_graph_liste_game[self.variable][self.variable2][z]== 2:
                self.listbox_4.insert(END, "Graph_2")
            if self.select_graph_liste_game[self.variable][self.variable2][z]== 3:
                self.listbox_4.insert(END, "Graph_3")
            if self.select_graph_liste_game[self.variable][self.variable2][z]== 4:
                self.listbox_4.insert(END, "Graph_4")
        self.listbox_4.bind("<ButtonRelease-1>", self.Select_graphType2)


    def Select_game(self, event = None):
        a  = self.listbox_3.curselection()
        self.game_ToSend = self.listbox_3.get(a)

    def Select_graphType2(self, event = None):
        a = self.listbox_4.curselection()
        self.type_stats = self.listbox_4.get(a)

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
