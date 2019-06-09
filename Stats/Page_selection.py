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

        """validate_button = Button(self.root, text = "validate", command = self.launch)
        validate_button.place(x = 500, y = 300)"""

        Reset_button = Button(self.root, text = "Reset", command = self.Reset)
        Reset_button.place(x = 700, y = 300)
        self.data = get_statistics()[0]
        self.root.mainloop()

    def get_variable_1(self, event = None):
        a = self.listbox_1.curselection()
        self.selected_mode = self.listbox_1.get(a)
        self.variable = self.listbox_1.index(a)
        try:
            self.listbox_2.destroy()
            self.listbox_3.destroy()
            self.listbox_4.destroy()
        except:
            pass
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
        try:
            self.listbox_3.destroy()
            self.listbox_4.destroy()
        except:
            pass

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
            self.listbox_3.bind("<ButtonRelease-1>", self.get_variable_2)
        else:
            self.listbox_3 = Listbox(self.root)
            self.listbox_3.place(x = 350, y = 60)
            self.listbox_3.insert(END, "tous les jeux")
            for elt in self.games:
                self.listbox_3.insert(END, elt)
            self.listbox_3.bind("<ButtonRelease-1>", self.get_variable_2)

    def get_variable_2(self, event = None):
        a = self.listbox_3.curselection()
        self.selected_mode3 = self.listbox_3.get(a)
        self.variable2 = self.listbox_3.index(a)
        try:
            self.listbox_4.destroy()
        except:
            pass
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

        elif self.selected_mode2 == "Statistiques sur Application":
            for z in range(4):
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 1:
                    self.listbox_4.insert(END, "Graph_1")
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 2:
                    self.listbox_4.insert(END, "Graph_2")
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 3:
                    self.listbox_4.insert(END, "Graph_3")
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 4:
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
        x0 = [] #Correspond au meilleur score
        y = []  #Correspond au titre ne bas ex: G1, G2
        x1 = [] #Correspond au score moyen
        title = 'Titre'
        Legend1 = 'Legend1'
        Legend2 = 'Legend2'
        name_y_axe = 'Score'
        if sur_quoi == "Statistiques sur jeu": #si la personne veut un graphique sur les Jeux
            Legend1 = "Score max"
            Legend2 = "Score moyen"
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel != "tous les jeux": #si c'est un jeu spécifique
                    title = "Top 10 du jeu {}".format(lequel)
                    for player in get_game_score_list(lequel):
                        label = player[0]
                        score_moyen = 0
                        try:
                            label += " " + str(self.data[lequel]['player_count'][player[0]][0])
                            score_moyen = self.data[lequel]['player_count'][player[0]][1]
                        except:
                            pass
                        y.append(label)
                        x0.append(player[1])
                        x1.append(score_moyen)

                elif lequel == "tous les jeux": #le classement général tout jeux confondus
                    title = "Classement général"
                    for player in get_score_list():
                        label = player[0]
                        x0.append(player[1])
                        moyenne = []
                        somme = 0
                        for jeu in self.data.keys():
                            try:
                                moyenne.append(self.data[jeu]["player_count"][player[0]][1])
                                somme += self.data[jeu]["player_count"][player[0]][0]
                            except:
                                pass
                        label += " " + str(somme)
                        if len(moyenne) == 0:
                            moyenne.append(0)
                        x1.append(sum(moyenne)/len(moyenne))
                        y.append(label)
            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel != 'tous les jeux': #si c'est un jeu spécifique
                    parties = 0
                    try:
                        data_game = self.data[lequel]["player_count"][self.user]
                        x1.append(data_game[1])
                        parties = data_game[0]
                        x0.append(get_player_score(self.user)[lequel])
                    except:
                        x0.append(0)
                        x1.append(0)

                    moyenne_moyenne = [] #moyenne des moyennes
                    moyenne_max = []     #moyenne des maximums
                    moyenne_parties = [] #moyenne des parties

                    for joueur in self.data[lequel]["player_count"].keys():
                        if joueur != self.user:
                            moyenne_moyenne.append(self.data[lequel]["player_count"][joueur][1])
                            moyenne_parties.append(self.data[lequel]["player_count"][joueur][0])
                            moyenne_max.append(get_player_score(joueur)[lequel])

                    if len(moyenne_moyenne) == 0: x1.append(0)
                    else: x1.append(sum(moyenne_moyenne)/len(moyenne_moyenne))
                    if len(moyenne_max) == 0: x0.append(0)
                    else: x0.append(sum(moyenne_max)/len(moyenne_max))
                    if len(moyenne_parties) == 0: moyenne_parties.append(0)
                    y = ["{}   Parties: {}".format(self.user,parties), "Reste des joueurs   Parties: {}".format(round(sum(moyenne_parties)/len(moyenne_parties)))]
                    #Score max et moyen de l'utilisateur pour un jeu donné + nombre de parties avec x0 et x1 dans yo[0]
                    #Score max du jeu, moyenne de scores des gens sur le jeu + nombre moyen de parties jouées x0 et x1 dans yo[1]
                    title = "Statistiques de {} en comparaison au reste des joueurs".format(self.user)
                elif lequel == 'tous les jeux': #sur tous les jeux
                    #Le meilleur score de l'utilsateur dans chaque jeu avec x0
                    #Avec sa moyenne de score dans chaque jeu avec x1
                    #Tous les jeux Nombre de parties du joueur dans chaque jeu dans y0
                    for jeu in self.data.keys():
                        try:
                            moyenne = self.data[jeu]["player_count"][self.user][1]
                            somme = self.data[jeu]["player_count"][self.user][0]
                            best = get_player_score(self.user)[jeu]
                        except:
                            moyenne = 0
                            best = 0
                            somme = 0
                        x0.append(best)
                        x1.append(moyenne)
                        y.append(jeu + " " + str(somme))
                    title = "Meilleur score et moyenne de {} dans chaque jeu".format(self.user)

        elif sur_quoi == "Statistiques sur Application":
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel == "stat1":   #Nombres de parties en fonction de jeu
                    name_y_axe = "Nombre de parties"
                    title = "Nombres de parties lancées en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    x0_att =[]

                    for games in self.data.keys():
                        x0_att =[]
                        y.append(games)
                        if len(self.data[games]["player_count"]) != 0:
                            for players in self.data[games]["player_count"]:
                                x0_att.append(self.data[games]["player_count"][players][0])
                            x0.append(sum(x0_att))
                        else:
                            x0.append(0)

                elif lequel == "stat2": #Meilleur score en fonction du jeu
                    name_y_axe = "Score"
                    title = "Score Maximum en fonction du Jeu"
                    Legend1 = "Score max"
                    for games in self.data.keys():
                        x0.append(get_game_score_list(games)[0][1])
                        y.append(games)
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    name_y_axe = "Score"
                    title = "Score Moyen en fonction du Jeu"
                    Legend1 = "Score max"
                    moyenne_moyenne = [] #moyenne des moyennes
                    for game in self.data.keys():
                        y.append(game)
                        for joueur in self.data[game]["player_count"].keys():
                            moyenne_moyenne.append(self.data[game]["player_count"][joueur][1])

                        if len(moyenne_moyenne) == 0: x0.append(0)
                        else: x0.append(sum(moyenne_moyenne)/len(moyenne_moyenne))
                        moyenne_moyenne = []
                    ##moyenne de tous les gens dans chaque jeu

                elif lequel == "stat4":
                    pass
            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu
                    name_y_axe = "Nombre de parties"
                    title = "Nombres de parties lancées en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    for games in self.data.keys():
                        y.append(games)
                        try:
                            x0.append(self.data[games]["player_count"][self.user][0])
                        except:
                            x0.append(0)

                    """moyennes = {}
                    total = {}
                    total_parties_joueur = {}

                    for game in self.data.keys():
                        moyennes[game] = self.data[game]["moyenne"][0]
                        total[game] = self.data[game]["moyenne"][1]

                        #total_parties_joueur[game] = data[game]["player_count"]["dodo"][1]"""

                    #Nombre de parties au total de chaque jeu
                    #y0 = les jeux
                    #x0 = le nombres de parties
                    #x1

                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    name_y_axe = "Score"
                    title = "Nombres de parties lancées en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    #Score max de chaque jeu en comparaison
                    for jeu in self.data.keys():
                        x0.append(get_player_score(self.user)[jeu])
                        y.append(jeu)
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    name_y_axe = "Nombre de parties"
                    title = "Nombres de parties lancées en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    for jeu in self.data.keys():
                        x0.append(self.data[games]["moyenne"][1])
                        y.append(jeu)
                elif lequel == "stat4":
                    pass

        #x0 =[5000, 4000]
        #x1 =[2500, 2000]
        Graph_1_exe(self.root,x0, y, x1,title, Legend1, Legend2,name_y_axe)

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
