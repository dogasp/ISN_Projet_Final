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

        self.listbox_1 = Listbox(self.root)
        self.listbox_1.place(x = 50, y = 60)
        self.listbox_1.insert(END, "Statistiques sur toi")
        self.listbox_1.insert(END, "Statistiques globales")
        self.listbox_1.bind("<ButtonRelease-1>", self.get_variable_1)
        self.selected_mode = 0

        self.games = get_player_score("dodo").keys()
        self.game_ToSend = "Flappy"

        dict_games = {'Tete': [1, 0, 0, 0, 1, 0, 0, 0], 'Pendu': [1, 0, 0, 0, 1, 0, 0, 0], 'Ghost': [1, 0, 0, 0, 1, 0, 0, 0],'Space': [1, 0, 0, 0, 1, 0, 0, 0],
        'Snake': [1, 2, 3, 0, 1, 2, 3, 0],'Minesweeper': [1, 0, 0, 0, 1, 0, 0, 0], 'Tetris': [1, 0, 0, 0, 1, 0, 0, 0], 'Pong': [1, 0, 0, 0, 1, 0, 0, 0],  'Flappy': [1, 0, 0, 0, 1, 0, 0, 0]}
        liste_attente = [1, 0, 0, 0, 1, 0, 0, 0]

        self.liste_jeux_app = ["tous les jeux"]
        for elt in self.games:
            self.liste_jeux_app.append(elt)
            liste_attente += dict_games[elt]
        self.select_graph_liste_game = np.array([liste_attente])
        self.select_graph_liste_game.resize((10,2,4))

        #Statistiques sur toi / Statistiques globales
        self.select_graph_liste_stat = np.array([
        1, 0, 0, 4, 1, 0, 0, 4,  #stat1
        1, 0, 0, 4, 1, 0, 0, 4,  #stat2
        1, 0, 0, 4, 1, 0, 0, 4,  #stat3
        1, 0, 0, 0, 1, 0, 0, 0,])#stat4
        self.select_graph_liste_stat.resize((4,2,4))

        validate_button = Button(self.root, text = "validate", command = self.launch)
        validate_button.place(x = 500, y = 300)

        Reset_button = Button(self.root, text = "Reset", command = self.Reset)
        Reset_button.place(x = 700, y = 300)


        data = get_statistics()[0]
        moyennes = {}
        total = {}
        total_parties_joueur = {}

        for game in data.keys():
            moyennes[game] = data[game]["moyenne"][0]
            total[game] = data[game]["moyenne"][1]

            total_parties_joueur[game] = data[game]["player_count"]["dodo"][1]

        print(total_parties_joueur)

        self.root.mainloop()

    def get_variable_1(self, event = None):
        a = self.listbox_1.curselection()
        self.selected_mode = self.listbox_1.get(a)
        self.variable = self.listbox_1.index(a)
        self.Select_mode0()

    def Select_mode0(self, event = None):
        self.listbox_2 = Listbox(self.root)
        self.listbox_2.place(x = 200, y = 60)
        self.listbox_2.insert(END, "Statistiques sur Application")
        self.listbox_2.insert(END, "Statistiques sur jeu")
        self.listbox_2.bind("<ButtonRelease-1>", self.Select_mode)
        self.selected_mode2 = 0

    def Select_mode(self, event = None):
        a  = self.listbox_2.curselection()
        self.selected_mode2 = self.listbox_2.get(a)

        if self.selected_mode2 == "Statistiques sur Application":
            self.listbox_3 = Listbox(self.root)
            self.listbox_3.place(x = 350, y = 60)
            if self.selected_mode == "Statistiques sur toi":
                self.listbox_3.insert(END, "stat1")
                self.listbox_3.insert(END, "stat2")
                self.listbox_3.insert(END, "stat3")
                self.listbox_3.insert(END, "stat4")
            else:
                self.listbox_3.insert(END, "stat1")
                self.listbox_3.insert(END, "stat2")
                self.listbox_3.insert(END, "stat3")
                self.listbox_3.insert(END, "stat4")
            self.listbox_3.bind("<ButtonRelease-1>", self.get_variable_3)
        else:
            self.listbox_3_bis = Listbox(self.root)
            self.listbox_3_bis.place(x = 350, y = 60)
            self.listbox_3_bis.insert(END, "tous les jeux")
            for elt in self.games:
                self.listbox_3_bis.insert(END, elt)
            self.listbox_3_bis.bind("<ButtonRelease-1>", self.get_variable_2)

    def get_variable_2(self, event = None): #pour les jeux
        a = self.listbox_3_bis.curselection()
        self.selected_mode3 = self.listbox_3_bis.get(a)
        self.variable2 = self.listbox_3_bis.index(a)
        self.Select_graphType()

    def get_variable_3(self, event = None): #pour l'app
        a = self.listbox_3.curselection()
        print(self.listbox_3.index(a))
        self.selected_mode3 = self.listbox_3.get(a)
        self.variable2_bis = self.listbox_3.index(a)
        self.Select_graphType()


    def Select_graphType(self, event = None):
        self.listbox_4 = Listbox(self.root)
        self.listbox_4.place(x = 500, y = 60)

        if self.selected_mode2 == "Statistiques sur jeu":
            for z in range(4):
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 1:
                    self.listbox_4.insert(END, "Graph_1")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 2:
                    self.listbox_4.insert(END, "Graph_2")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 3:
                    self.listbox_4.insert(END, "Graph_3")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 4:
                    self.listbox_4.insert(END, "Graph_4")

        else:
            for z in range(4):
                if self.select_graph_liste_stat[self.variable2_bis][self.variable][z] == 1:
                    self.listbox_4.insert(END, "Graph_1")
                if self.select_graph_liste_stat[self.variable2_bis][self.variable][z] == 2:
                    self.listbox_4.insert(END, "Graph_2")
                if self.select_graph_liste_stat[self.variable2_bis][self.variable][z] == 3:
                    self.listbox_4.insert(END, "Graph_3")
                if self.select_graph_liste_stat[self.variable2_bis][self.variable][z] == 4:
                    self.listbox_4.insert(END, "Graph_4")

        self.listbox_4.bind("<ButtonRelease-1>", self.Select_graphType2)


    def Select_game(self, event = None):
        a  = self.listbox_3.curselection()
        self.game_ToSend = self.listbox_3.get(a)

    def Select_graphType2(self, event = None):
        a = self.listbox_4.curselection()
        self.type_stats = self.listbox_4.get(a)
        if self.type_stats == "Graph_1":
            self.Graph_1(self.selected_mode, self.selected_mode2, self.selected_mode3)
        if self.type_stats == "Graph_2":
            self.Graph_2(self.selected_mode, self.selected_mode2, self.selected_mode3)
        if self.type_stats == "Graph_3":
            self.Graph_3(self.selected_mode, self.selected_mode2, self.selected_mode3)
        if self.type_stats == "Graph_4":
            self.Graph_4(self.selected_mode, self.selected_mode2, self.selected_mode3)


    def Graph_1(self, sur_qui, sur_quoi, lequel):
        print(sur_qui, sur_quoi, lequel)
        x0 = [] #Correspond au meilleur score
        y = []  #Correspond au titre ne bas ex: G1, G2
        x1 = [] #Correspond au score moyen
        title = 'Titre'
        Legend1 = 'Legend1'
        Legend2 = 'Legend2'
        if sur_quoi == "Statistiques sur jeu": #si la personne veut un graphique sur les Jeux
            Legend1 = "Score max"
            Legend2 = "Score moyen"
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel != "tous les jeux": #si c'est un jeu spécifique
                    title = "Top 10 du jeu {}".format(lequel)
                    for player in get_game_score_list(lequel):
                        y.append(player[0])
                        x0.append(player[1])
                else: #le classement général tout jeux confondus
                    title = "Classement général"
                    for player in get_score_list():
                        y.append(player[0])
                        x0.append(player[1])

            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel != 'tous les jeux': #si c'est un jeu spécifique
                    #Score max et moyen de l'utilisateur pour un jeu donné + nombre de parties
                    #Score max du jeu, moyenne de scores des gens sur le jeu +nombre moyen de parties jouées
                    y = ["{}   Parties: {}".format(self.user,20), "Reste des joueurs   Parties: {}".format(10)]
                    title = "Statistiques de {} en comparaison au reste des joueurs".format(self.user)
                else:
                    #Le meilleur score de l'utilsateur dans chaque jeu
                    #Avec sa moyenne dans de score dans chaque jeu
                    #Nombre de parties du joueur dans chaque jeu
                    pass

        elif sur_quoi == "Statistiques sur Application":
            if lequel == "stat1":
                pass
            elif lequel == "stat2":
                pass
            elif lequel == "stat3":
                pass
            elif lequel == "stat4":
                pass

                pass

        else: #si la personne veut des stats globales
            pass

        x0 =[5000, 4000]
        x1 =[2500, 2000]
        Graph_1_exe(self.root,x0, y, x1,title, Legend1, Legend2)

    def Graph_2(self):
        pass


    def Graph_3(self):
        pass


    def Graph_4(self):
        pass


    def Reset(self):
        self.root.destroy()
        self.root.quit()
        Stats(self.user)


    def launch(self):
        pass
        print(self.game_ToSend, self.selected_mode)

        if self.selected_mode == "Statistiques sur toi": #si la personne veut un graphique sur elle
            pass

        else: #si la personne veut des stats globales
            if self.type_stats == "Application":
                pass


            else:
                if self.game_ToSend != "tout les jeux": #si c'est un jeu spécifique
                    x = []
                    y = []
                    for players in get_game_score_list(self.game_ToSend):
                        x.append(players[0])
                        y.append(players[1])

                    Graph_3(self.root,y, x)

                else: #le classement général tout jeux confondus
                    pass


    def show_selected_grap(self):
        pass
