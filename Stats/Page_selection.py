from tkinter import *

sys.path.append("../Reseau")
from Stats.Page_stat import *
from Reseau.client import *

class Stats:
    def __init__(self, user):
        self.user = user
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.titre = Label(self.root, text = "Page de sélection des graphs à afficher")
        self.titre.place(x = 200, y = 20)

        self.listbox_1 = Listbox(self.root)
        self.listbox_1.place(x = 50, y = 60)
        self.listbox_1.insert(END, "Statistiques sur toi")
        self.listbox_1.insert(END, "Statistiques globales")
        self.listbox_1.bind("<ButtonRelease-1>", self.get_variable_1)
        self.selected_mode = 0

        self.games = []
        self.data = get_statistics()
        for games in self.data[0] :
            self.games.append(games)

        dict_games = {'Tete': [1,0,0,0,5,1,0,0,0,5], 'Pendu': [1,0,0,0,5,1,0,0,0,5], 'Ghost': [1,0,0,0,5,1,0,0,0,5],
        'Snake': [1,2,3,0,5,1,2,3,0,5],'Minesweeper': [1,2,3,0,5,1,2,3,0,5], 'Tetris': [1,0,0,0,5,1,0,0,0,5], 'Pong': [1,2,3,0,5,1,2,3,0,5],  'Flappy': [1,2,3,0,5,1,2,3,0,5]}
        liste_attente = [1,0,0,4,5,1,0,0,4,5]

        self.liste_jeux_app = ["tous les jeux"]
        for elt in self.games:
            self.liste_jeux_app.append(elt)
            liste_attente += dict_games[elt]
        self.select_graph_liste_game = np.array([liste_attente])
        self.select_graph_liste_game.resize((9,2,5))

        #Statistiques sur toi / Statistiques globales
        self.select_graph_liste_stat = np.array([
        1, 0, 0, 4, 5, 1, 0, 0, 4, 5,  #stat1
        1, 0, 0, 4, 5, 1, 0, 0, 4, 5,  #stat2
        1, 0, 0, 4, 5, 1, 0, 0, 4, 5,  #stat3
        1, 0, 0, 0, 5, 1, 0, 0, 0, 5])#stat4
        self.select_graph_liste_stat.resize((4,2,5))

        Reset_button = Button(self.root, text = "Reset", command = self.Reset)
        Reset_button.place(x = 700, y = 300)
        self.root.mainloop()

    def exit(self):
        self.root.quit()
        self.root.destroy()

    def get_variable_1(self, event = None):
        a = self.listbox_1.curselection()
        self.selected_mode = self.listbox_1.get(a)
        self.variable = self.listbox_1.index(a)
        try:
            self.listbox_2.destroy()
            self.listbox_3.destroy()
            self.listbox_4.destroy()
        except: pass
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
        except: pass

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
        try: self.listbox_4.destroy()
        except: pass
        self.Select_graphType()

    def Select_graphType(self, event = None):
        self.listbox_4 = Listbox(self.root)
        self.listbox_4.place(x = 500, y = 60)
        if self.selected_mode2 == "Statistiques sur jeu":
            for z in range(len(self.select_graph_liste_game[0][0])):
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 1:
                    self.listbox_4.insert(END, "Graph_1")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 2:
                    self.listbox_4.insert(END, "Graph_2")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 3:
                    self.listbox_4.insert(END, "Graph_3")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 4:
                    self.listbox_4.insert(END, "Graph_4")
                if self.select_graph_liste_game[self.variable2][self.variable][z]== 5:
                    self.listbox_4.insert(END, "Graph_5")

        elif self.selected_mode2 == "Statistiques sur Application":
            for z in range(len(self.select_graph_liste_stat[0][0])):
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 1:
                    self.listbox_4.insert(END, "Graph_1")
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 2:
                    self.listbox_4.insert(END, "Graph_2")
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 3:
                    self.listbox_4.insert(END, "Graph_3")
                if self.select_graph_liste_stat[self.variable2][self.variable][z] == 5:
                    self.listbox_4.insert(END, "Graph_5")

        self.listbox_4.bind("<ButtonRelease-1>", self.Select_graphType2)

    def Select_game(self, event = None):
        a  = self.listbox_3.curselection()
        self.game_ToSend = self.listbox_3.get(a)

    def Select_graphType2(self, event = None):
        a = self.listbox_4.curselection()
        self.type_stats = self.listbox_4.get(a)
        if self.type_stats == "Graph_1":
            self.Graph_1(self.selected_mode, self.selected_mode2, self.selected_mode3)
        elif self.type_stats == "Graph_2":
            self.Graph_2(self.selected_mode, self.selected_mode2, self.selected_mode3)
        elif self.type_stats == "Graph_3":
            self.Graph_3(self.selected_mode, self.selected_mode2, self.selected_mode3)
        elif self.type_stats == "Graph_4":
            self.Graph_4(self.selected_mode, self.selected_mode2, self.selected_mode3)
        elif self.type_stats == "Graph_5":
            self.Graph_5(self.selected_mode, self.selected_mode2, self.selected_mode3)

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
                            label += " " + str(self.data[0][lequel]['player_count'][player[0]][0])
                            score_moyen = self.data[0][lequel]['player_count'][player[0]][1]
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
                        for jeu in self.data[0].keys():
                            try:
                                moyenne.append(self.data[0][jeu]["player_count"][player[0]][1])
                                somme += self.data[0][jeu]["player_count"][player[0]][0]
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
                        data_game = self.data[0][lequel]["player_count"][self.user]
                        x1.append(data_game[1])
                        parties = data_game[0]
                        x0.append(get_player_score(self.user)[lequel])
                    except:
                        x0.append(0)
                        x1.append(0)

                    moyenne_max = []     #moyenne des maximums
                    moyenne_parties = [self.data[0][lequel]["moyenne"][1]] #moyenne des parties

                    for joueur in self.data[0][lequel]["player_count"].keys():
                        if joueur != self.user:
                            moyenne_max.append(get_player_score(joueur)[lequel])
                    x1.append(self.data[0][lequel]["moyenne"][0])

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
                    for jeu in self.data[0].keys():
                        try:
                            x1.append(self.data[0][jeu]["player_count"][self.user][1])
                            y.append(jeu + " " + str(self.data[0][jeu]["player_count"][self.user][0]))
                            x0.append(get_player_score(self.user)[jeu])
                        except:
                            x1.append(0)
                            x0.append(0)
                            y.append(jeu + " " + str(0))
                    title = "Meilleur score et moyenne de {} dans chaque jeu".format(self.user)
        elif sur_quoi == "Statistiques sur Application":
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel == "stat1":   #Nombres de parties en fonction de jeu
                    name_y_axe = "Nombre de parties"
                    title = "Nombres de parties lancées en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    for games in self.data[0]:
                        y.append(games)
                        x0.append(self.data[0][games]["moyenne"][1])
                elif lequel == "stat2": #Meilleur score en fonction du jeu
                    name_y_axe = "Score"
                    title = "Score Maximum en fonction du Jeu"
                    Legend1 = "Score max"
                    for games in self.data[0]:
                        x0.append(get_game_score_list(games)[0][1])
                        y.append(games)
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    name_y_axe = "Score"
                    title = "Score Moyen en fonction du Jeu"
                    Legend1 = "Score max"
                    for game in self.data[0].keys():
                        y.append(game)
                        x0.append(self.data[0][game]["moyenne"][0])
                elif lequel == "stat4":
                    name_y_axe = "Temps en seconde"
                    title = "Différentes stats sur la durée des parties"
                    Legend1 = "Temps passé en moyenne"
                    Legend2 = "Temps passé par le meilleur"
                    for game in self.data[2].keys():
                        y.append(game)
                        x0.append(self.data[2][game]["moyenne"][0])
                        try: x1.append(self.data[2][game][get_game_score_list(lequel)[0][0]])
                        except: x1.append(0)

            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu
                    name_y_axe = "Nombre de parties"
                    title = "Nombres de parties lancées de {} en fonction du Jeu".format(self.user)
                    Legend1 = "Nb de parties"
                    for games in self.data[0].keys():
                        y.append(games)
                        try:
                            x0.append(self.data[0][games]["player_count"][self.user][0])
                        except:
                            x0.append(0)

                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    name_y_axe = "Score"
                    title = "Score maximum en fonction des jeux"
                    Legend1 = "Score max"
                    #Score max de chaque jeu en comparaison
                    for jeu in self.data[0].keys():
                        x0.append(get_player_score(self.user)[jeu])
                        y.append(jeu)
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    name_y_axe = "Score"
                    title = "Score Moyen en fonction du Jeu"
                    Legend1 = "Score Moyen"
                    moyenne_moyenne = [] #moyenne des moyennes
                    for jeu in self.data[0].keys():
                        x0.append(self.data[0][jeu]["moyenne"][0])
                        y.append(jeu)
                elif lequel == "stat4":
                    name_y_axe = "Temps en seconde"
                    title = "Différentes stats sur la durée des parties"
                    Legend1 = "Temps passé en moyenne par {}".format(self.user)
                    Legend2 = "Temps passé par le meilleur"
                    for game in self.data[2].keys():
                        y.append(game)
                        x0.append(self.data[2][game][self.user])
                        try: x1.append(self.data[2][game][get_game_score_list(lequel)[0][0]])
                        except: x1.append(0)
        #x0 =[5000, 4000]
        #x1 =[2500, 2000]
        Graph_1_exe(self.root,self.user,x0, y, x1,title, Legend1, Legend2,name_y_axe)

    def Graph_2(self, sur_qui, sur_quoi, lequel, tree = False):
        x0 = {} #Correspond au meilleur score
        y = []  #Correspond au titre ne bas ex: G1, G2
        x1 = [] #Correspond au score moyen
        title = f"Disposition des morts dans {lequel}"
        title2 = 'Titre2'
        Legend1 = "Nb de morts"
        Legend2 = 'Legend2'
        name_y_axe = 'Score'
        if sur_quoi == "Statistiques sur jeu": #si la personne veut un graphique sur les Jeux
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                for value in self.data[1][lequel].values():
                    for pos in value.keys():
                        try:
                            x0[pos] += value[pos]
                        except:
                            x0[pos] = value[pos]

            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                x0 = self.data[1][lequel][self.user]

        elif sur_quoi == "Statistiques sur Application":

            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu*
                    pass
                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    pass
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    pass
                elif lequel == "stat4":
                    pass

            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu*
                    pass
                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    pass
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    pass
                elif lequel == "stat4":
                    pass
        if tree:
            Graph_3_exe(self.root,self.user,x0,title,Legend1)
        else:
            Graph_2_exe(self.root,self.user,x0,title,Legend1)

    def Graph_3(self, sur_qui, sur_quoi, lequel):
        self.Graph_2(sur_qui, sur_quoi, lequel, True)

    def Graph_4(self, sur_qui, sur_quoi, lequel):
        x0 = [] #Correspond au meilleur score
        y = []  #Correspond au titre ne bas ex: G1, G2
        x1 = [] #Correspond au score moyen
        title = 'Titre'
        title2 = 'Titre2'
        Legend1 = 'Legend1'
        Legend2 = 'Legend2'
        name_y_axe = 'Score'
        if sur_quoi == "Statistiques sur jeu": #si la personne veut un graphique sur les Jeux
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel == "tous les jeux":
                    for jeu in self.data[0].keys():
                        y.append(jeu)
                        x0.append(get_game_score_list(jeu)[0][1])
                    title = "Meilleur score de chaque jeu"
                    title2 = "Jeux"
                elif lequel != "tous les jeux":
                    pass
            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel != "tous les jeux":
                    pass
                elif lequel == "tous les jeux":
                    for jeu in self.data[0].keys():
                        try:
                            moyenne = self.data[0][jeu]["player_count"][self.user][1]
                            somme = self.data[0][jeu]["player_count"][self.user][0]
                            best = get_player_score(self.user)[jeu]
                        except:
                            moyenne = 0
                            best = 0
                            somme = 0
                        x0.append(best)
                        x1.append(moyenne)
                        y.append(jeu + " " + str(somme))
                    title = "Meilleur score et moyenne de {} dans chaque jeu".format(self.user)
                    title2 = "Jeux"
        elif sur_quoi == "Statistiques sur Application":
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu*
                    title = "Nombres de parties lancées en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    x0_att =[]
                    title2 = "Jeux"
                    for games in self.data[0].keys():
                        x0_att =[]
                        y.append(games)
                        if len(self.data[0][games]["player_count"]) != 0:
                            for players in self.data[0][games]["player_count"]:
                                x0_att.append(self.data[0][games]["player_count"][players][0])
                            x0.append(sum(x0_att))
                        else:
                            x0.append(0)
                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    title = "Score Maximum en fonction du Jeu"
                    Legend1 = "Score max"
                    title2 = "Jeux"
                    for games in self.data[0].keys():
                        x0.append(get_game_score_list(games)[0][1])
                        y.append(games)
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    title = "Score Moyen en fonction du Jeu"
                    Legend1 = "Score max"
                    title2 = "Jeux"
                    moyenne_moyenne = [] #moyenne des moyennes
                    for game in self.data[0].keys():
                        y.append(game)
                        for joueur in self.data[0][game]["player_count"].keys():
                            moyenne_moyenne.append(self.data[0][game]["player_count"][joueur][1])
                        if len(moyenne_moyenne) == 0: x0.append(0)
                        else: x0.append(sum(moyenne_moyenne)/len(moyenne_moyenne))
                        moyenne_moyenne = []
                elif lequel == "stat4":
                    pass
            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu*
                    title = "Nombres de parties lancées du joueur en fonction du Jeu"
                    Legend1 = "Nb de parties"
                    title2 = "Jeux"
                    for games in self.data[0].keys():
                        y.append(games)
                        try:
                            x0.append(self.data[0][games]["player_count"][self.user][0])
                        except:
                            x0.append(0)
                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    title = "Score maximum en fonction des jeux"
                    Legend1 = "Score max"
                    title2 = "Jeux"
                    #Score max de chaque jeu en comparaison
                    for jeu in self.data[0].keys():
                        x0.append(get_player_score(self.user)[jeu])
                        y.append(jeu)
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    title2 = "Jeux"
                    title = "Score Moyen en fonction du Jeu"
                    Legend1 = "Score Moyen"
                    moyenne_moyenne = [] #moyenne des moyennes
                    for jeu in self.data[0].keys():
                        x0.append(self.data[0][jeu]["moyenne"][0])
                        y.append(jeu)
                elif lequel == "stat4":
                    pass

        Graph_4_exe(self.root,self.user,x0,y, x1,title,title2, Legend1, Legend2,name_y_axe)

    def Graph_5(self, sur_qui, sur_quoi, lequel):
        x0 = [] #Correspond au meilleur score
        y = []  #Correspond au titre ne bas ex: G1, G2
        x1 = [] #Correspond au score moyen
        title = 'Titre'
        title2 = 'Titre2'
        Legend1 = 'Legend1'
        Legend2 = 'Legend2'
        name_y_axe = 'Score'
        label_y = "none"
        if sur_quoi == "Statistiques sur jeu": #si la personne veut un graphique sur les Jeux
            if sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur les gens
                if lequel == "tous les jeux":
                    title = "Différentes stats sur les Scores Max en fonction des Jeux"
                    Legend1 = " Score total"
                    label_y = "score"
                    x0 ={"Score moyen de {}".format(self.user): {},"Score maximum": {},"Score max de {}".format(self.user): {},"Score moyen": {}}
                    for parametters in x0:
                        for games in self.data[0].keys():
                            if parametters == "Score moyen de {}".format(self.user):
                                try: x0[parametters][games] = self.data[0][games]["player_count"][self.user][1]
                                except: x0[parametters][games] = 0
                            elif parametters == "Score maximum":
                                x0[parametters][games] = get_game_score_list(games)[0][1]
                            elif parametters == "Score max de {}".format(self.user):
                                try: x0[parametters][games] = get_player_score(self.user)[games]
                                except: x0[parametters][games] = 0
                            elif parametters == "Score moyen":
                                x0[parametters][games] = self.data[0][games]["moyenne"][0]
                elif lequel != "tous les jeux":
                    title = "Différentes stats sur les Scores Max en fonction des Jeux"
                    Legend1 = " Score total"
                    label_y = "score"
                    x0 ={"Score moyen": {},"Score maximum": {}}
                    for parametters in x0:
                        for i,players in enumerate(get_game_score_list(lequel)):
                            if parametters == "Score maximum":
                                try: x0[parametters][players[0]+':'+ str(i+1)] = players[1]
                                except: x0[parametters][players[0]+':'+ str(i+1)] = 0
                            elif parametters == "Score moyen":
                                try:x0[parametters][players[0]+':'+ str(i+1)] =self.data[0][lequel]['player_count'][players[0]][1]
                                except: x0[parametters][players[0]+':'+ str(i+1)] = 0
            elif sur_qui == "Statistiques globales": #si la personne veut un graphique sur ses données
                if lequel != "tous les jeux":
                    x0 = {}
                    for i,players in enumerate(get_game_score_list(lequel)):
                        x0[players[0]+':'+ str(i+1)] = {}
                        try: x0[players[0]+':'+ str(i+1)]["Score moyen"] = self.data[0][lequel]['player_count'][players[0]][1]
                        except: x0[players[0]+':'+ str(i+1)]["Score moyen"] = 0
                        try: x0[players[0]+':'+ str(i+1)]["Score max"] = players[1]
                        except: x0[players[0]+':'+ str(i+1)]["Score max"] = 0
                elif lequel == "tous les jeux":
                    title = "Différentes stats sur les Scores Max en fonction des Jeux"
                    Legend1 = " Score total"
                    label_y = "score"
                    x0 = {}
                    for games in self.data[0]:
                        x0[games] = {}
                        try: x0[games]["Score moyen de {}".format(self.user)] = self.data[0][games]["player_count"][self.user][1]
                        except: x0[games]["Score moyen de {}".format(self.user)] = 0
                        try: x0[games]["Score maximum"] = get_game_score_list(games)[0][1]
                        except: x0[games]["Score maximum"] = 0
                        try:x0[parametters]["Score max de {}".format(self.user)] = get_player_score(self.user)[games]
                        except:x0[games]["Score max de {}".format(self.user)] = 0
                        try: x0[games]["Score moyen"] = self.data[0][games]["moyenne"][0]
                        except: x0[games]["Score moyen"] = 0

        elif sur_quoi == "Statistiques sur Application":
            if sur_qui == "Statistiques globales": #si la personne veut un graphique sur les gens
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu*
                    Legend1 = "Nb de parties"
                    label_y = "parties"
                    title = "Différentes stats sur les nombres de parties en fonctions des jeux"
                    x0 ={"Nb parties moyenne": {},"Nb parties {}".format(self.user): {},"Nb parties du meilleur joueur du jeu": {}}
                    title2 = "Jeux"
                    for parametters in x0:
                        for games in self.data[0].keys():
                            if parametters == "Nb parties moyenne":
                                if len(self.data[0][games]["player_count"]) != 0:
                                    x0[parametters][games] = self.data[0][games]["moyenne"][1]/len(self.data[0][games]["player_count"])
                                else: x0[parametters][games] = 0
                            elif parametters == "Nb parties {}".format(self.user):
                                try:x0[parametters][games] = self.data[0][games]["player_count"][self.user]
                                except: x0[parametters][games] = 0
                            elif parametters == "Nb parties du meilleur joueur du jeu":
                                try: x0[parametters][games] = self.data[0][games]["player_count"][get_game_score_list(games)[0][0]]
                                except: x0[parametters][games] = 0
                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    title = "Différentes stats sur les Scores Max en fonction des Jeux"
                    Legend1 = " Score total"
                    label_y = "score"
                    x0 ={"Score maximum": {},"Score max de {}".format(self.user): {},"Score moyen": {}}
                    for parametters in x0:
                        for games in self.data[0].keys():
                            if parametters == "Score maximum":
                                x0[parametters][games] = get_game_score_list(games)[0][1]
                            elif parametters == "Score max de {}".format(self.user):
                                try:x0[parametters][games] = get_player_score(self.user)[games]
                                except:x0[parametters][games] = 0
                            elif parametters == "Score moyen":
                                x0[parametters][games] = self.data[0][games]["moyenne"][0]
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    title = "Différentes stats sur les Scores Moyens en fonction des Jeux"
                    Legend1 = " Score total"
                    label_y = "score"
                    x0 ={"Score moyen de {}".format(self.user): {},"Score max de {}".format(self.user): {},"Score moyen": {}}
                    for parametters in x0:
                        for games in self.data[0].keys():
                            if parametters == "Score moyen de {}".format(self.user):
                                try:x0[parametters][games] = self.data[0][games]["player_count"][self.user][1]
                                except:x0[parametters][games] = 0
                            elif parametters == "Score max de {}".format(self.user):
                                try:x0[parametters][games] = get_player_score(self.user)[games]
                                except:x0[parametters][games] = 0
                            elif parametters == "Score moyen":
                                try: x0[parametters][games] = self.data[0][games]["moyenne"][0]
                                except: x0[parametters][games] = 0
                elif lequel == "stat4": #Moyenne des temps
                    label_y = "temps"
                    title = "Différentes stats sur les Scores Moyens en fonction des Jeux"
                    Legend1 = " Score total"
                    x0 ={"Temps moyen passé par {}".format(self.user): {},"Temps passé par {} (Meilleur partie)".format(self.user): {},"Temps passé en moyenne": {},"Temps passé par le meilleur du jeu": {}}
                    for parametters in x0:
                        for games in self.data[2].keys():
                            if parametters == "Temps moyen passé par {}".format(self.user):
                                try: x0[parametters][games] = self.data[0][games][self.user][0]
                                except: x0[parametters][games] = 0
                            elif parametters == "Temps passé par {} (Meilleur partie)".format(self.user):
                                try: x0[parametters][games] = self.data[0][games][self.user][1]
                                except: x0[parametters][games] = 0
                            elif parametters == "Temps passé en moyenne":
                                try: x0[parametters][games] = self.data[0][games]["moyenne"][0]
                                except: x0[parametters][games] = 0
                            elif parametters == "Temps passé par le meilleur du jeu":
                                try: x0[parametters][games] = self.data[0][games]["moyenne"][1]
                                except: x0[parametters][games] = 0
            elif sur_qui == "Statistiques sur toi": #si la personne veut un graphique sur ses données
                if lequel == "stat1": #Nombres de parties du joueur en fonction de jeu*
                    Legend1 = "Nb de parties"
                    label_y = "score"
                    title = "Différentes stats sur les nombres de parties en fonctions des jeux"
                    x0 ={'Tete': {}, 'Pendu': {}, 'Ghost': {},'Space': {}, 'Snake': {},'Minesweeper': {}, 'Tetris': {}, 'Pong': {},  'Flappy': {}}
                    for games in x0:
                        if len(self.data[0][games]["player_count"]) != 0:
                            x0[games]["Moyenne de parties"] = self.data[0][games]["moyenne"][1]/len(self.data[0][games]["player_count"])
                        else:
                            x0[games]["Moyenne de parties"] = 0
                        x0[games]["Nb de parties du meilleur"] = self.data[0][games]["player_count"][get_game_score_list(lequel)[0][1]]
                        x0[games]["Nb parties {}".format(self.user)] = self.data[0][games]["player_count"][self.user]
                elif lequel == "stat2": #Meilleur score du joueur en fonction du jeu
                    Legend1 = "score"
                    label_y = "score"
                    title = "Différentes stats sur les Scores Max en fonction des Jeux"
                    x0 ={'Tete': {}, 'Pendu': {}, 'Ghost': {},'Space': {}, 'Snake': {},'Minesweeper': {}, 'Tetris': {}, 'Pong': {},  'Flappy': {}}
                    for games in x0:
                        x0[games]["Score maximum"] = get_game_score_list(games)[0][1]
                        x0[games]["Score moyen"] = self.data[0][games]["moyenne"][0]
                        try: x0[games]["Score max de {}".format(self.user)] =  get_player_score(self.user)[games]
                        except: x0[games]["Score max de {}".format(self.user)] = 0
                elif lequel == "stat3": #Moyenne de score du joueur en fonction du jeu
                    Legend1 = "Nb de parties"
                    label_y = "score"
                    title = "Différentes stats sur les Scores Moyens en fonction des Jeux"
                    x0 ={'Tete': {}, 'Pendu': {}, 'Ghost': {},'Space': {}, 'Snake': {},'Minesweeper': {}, 'Tetris': {}, 'Pong': {},  'Flappy': {}}
                    for games in x0:
                        try: x0[games]["Score moyen de {}".format(self.user)] = self.data[0][games]["player_count"][self.user][1]
                        except: x0[games]["Score moyen de {}".format(self.user)] = 0
                        x0[games]["Score moyen"] = self.data[0][games]["moyenne"][0]
                        try: x0[games]["Score max de {}".format(self.user)] =  get_player_score(self.user)[games]
                        except: x0[games]["Score max de {}".format(self.user)] = 0
                elif lequel == "stat4":
                    title = "Différentes stats sur les Scores Moyens en fonction des Jeux"
                    Legend1 = " Score total"
                    label_y = "temps"
                    x0 ={'Tete': {}, 'Pendu': {}, 'Ghost': {},'Space': {}, 'Snake': {},'Minesweeper': {}, 'Tetris': {}, 'Pong': {},  'Flappy': {}}
                    for games in x0:
                        try: x0[games]["Temps moyen passé par {}".format(self.user)] = self.data[0][games][self.user][0]
                        except: x0[games]["Temps moyen passé par {}".format(self.user)] = 0
                        try: x0[games]["Temps passé par {} (Meilleur partie)".format(self.user)] = self.data[0][games][self.user][1]
                        except: x0[games]["Temps passé par {} (Meilleur partie)".format(self.user)] = 0
                        try: x0[games]["Temps passé en moyenne"] = self.data[0][games]["moyenne"][0]
                        except: x0[games]["Temps passé en moyenne"] = 0
                        try: x0[games]["Temps passé par le meilleur du jeu"] = self.data[0][games]["moyenne"][1]
                        except: x0[games]["Temps passé par le meilleur du jeu"] = 0

        Graph_5_exe(self.root,self.user,x0,title,label_y)

    def Reset(self):
        self.root.destroy()
        self.root.quit()
        Stats(self.user)
