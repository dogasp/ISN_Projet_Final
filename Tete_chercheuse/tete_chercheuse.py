from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from Tete_chercheuse.data import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *

##################----------Variables------------######################################
#'0' correpond à une case vide
#'X' correspond à une case pleine (mur)
#'R' correpond à la case associée au robot
#'P' correpond à la case associée à l'arrivée (drapeau)
#'C' correpond aux palettes, où l'on ajoute un obstacle
#'S' correspond à une (petite) pièce/récompense
#'B' correspond à une (grosse) pièce/récompense
#'E' correspond au robot arrivé
#meilleur score possible: 4163,9
########################################################################################

class application:
    def __init__(self, user):
        self.User_name = user #nom d'utilisateur
        self.rules_game() #on execute les rêgles du jeu et le scoreboard


        self.root_tete = Toplevel() #fenetre principale
        self.root_tete.geometry('700x550')
        self.root_tete.protocol("WM_DELETE_WINDOW",exit)
        self.root_tete.title("Tete Chercheuse")
        self.root_tete.resizable(False,False)
        self.root_tete.focus_force()
        #############------------variables----------########################
        self.score = [50] #initialisation de la liste des scores
        self.index_robot = 0 #la ou le robot regarde
        self.nbcases_width = self.nbcases_height = 10 #dimensions
        self.cell_width = 500/self.nbcases_width #dimensions des cellules
        self.cell_height = 500/self.nbcases_height
        self.score_star = 0            #bonnus des pièces
        self.time_game = 0
        self.nbx = 0
        self.nbl = 0

        self.table = [[0 for i in range(self.nbcases_width)] for j in range(self.nbcases_height)]#tableau
        self.level = 1 #niveau

        ########---------Import Photos------------------###############################################
        self.robot = [PhotoImage(file = "Tete_chercheuse/image/robot_right.png"), PhotoImage(file = "Tete_chercheuse/image/robot_front.png"), PhotoImage(file = "Tete_chercheuse/image/robot_left.png"), PhotoImage(file = "Tete_chercheuse/image/robot_back.png")]
        self.restart_button_image = PhotoImage(file = "Tete_chercheuse/image/start.png")
        self.Flag = PhotoImage(file = "Tete_chercheuse/image/flag.png")
        self.End = PhotoImage(file = "Tete_chercheuse/image/robot_flag.png")
        self.Caisse = PhotoImage(file = "Tete_chercheuse/image/caisse.png")
        self.Wall = PhotoImage(file = "Tete_chercheuse/image/mur.ppm")
        self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
        self.Yellow_Coin = PhotoImage(file = "Tete_chercheuse/image/yellow_coin.ppm")
        self.Red_Coin = PhotoImage(file = "Tete_chercheuse/image/red_coin.ppm")
        self.Guide_tete = PhotoImage(file = "Tete_chercheuse/image/brain.png")
        self.Bulle_image = PhotoImage(file = "Tete_chercheuse/image/bulle.png")


        ########------------Frames Pricipaux-------------########################################
        self.Frame_top = Frame(self.root_tete, width = 700, height = 50, bg = 'lightgrey')
        self.Frame_right = Frame(self.root_tete, width = 500, height = 500)
        self.Frame_left = Frame(self.root_tete, width = 200, height = 500, bg = 'red')

        ########-----------Frames Secondaires-----------######################################
        self.Frame1 = Frame(self.Frame_left, width = 200, height =200, bg = 'gold')
        self.Frame2 = Frame(self.Frame_left, width = 200, height =300, bg = 'black')

        self.Title_level = Label(self.Frame_top, text = "Level 1", font=("Helvetica", 20), relief = GROOVE)
        self.Table = Canvas(self.Frame_right,width = 500, height = 500, bg ='white', highlightthickness=0)

        self.Canvas_dessine = Canvas(self.Frame2, bg = 'white',width = 187, height =290)

        #######-----------Package des Frames-------------##################################
        self.Frame_top.pack(side = TOP)
        self.Frame_right.pack(side = RIGHT)
        self.Frame_left.pack(side = LEFT)

        self.Frame1.pack(side = TOP)
        self.Frame2.pack(side = BOTTOM)
        self.Canvas_dessine.place(x = 3, y =4)

        self.Table.pack(fill = BOTH)
        self.Title_level.place(x = 315, y = 5)

        #########------------Labels et autres-----------##################################

        self.Button_start = Button(self.Frame1,relief = GROOVE,activebackground = 'black' ,bg = 'black', cursor ='hand2', image = self.restart_button_image,command = self.start)
        self.Button_start.place(x = 20, y = 27)

        self.Button_quit = Button(self.Frame_top, text = 'QUIT' ,relief = GROOVE ,font = ("Helvetica", 10), cursor ='hand2',command = self.exit)
        self.Button_quit.place(x = 550, y = 19)

        self.Button_restart = Button(self.Frame_top, text = "RESTART", relief = GROOVE,cursor ='hand2', font = ("Helvetica", 10),command = self.restart_button)
        self.Button_restart.place(x = 600, y = 19)

        self.show_time = Label(self.Frame1, text = "Time: %s" %str(0), font = ("Helvetica", 10), relief =GROOVE)
        self.show_time.place(x = 110, y = 170)

        self.show_score = Label(self.Frame1, text = "Score: %s" %str(sum(self.score)), font = ("Helvetica", 10), relief = GROOVE)
        self.show_score.place(x = 25, y = 170)

        self.show_count = Label(self.Frame1, text = "Nombre de palettes: %s" %str(0), font = ("Helvetica", 10), relief = GROOVE)
        self.show_count.place(x = 31, y = 130)

        self.Canvas_dessine.create_image(86,215 ,image = self.Guide_tete)
        self.Canvas_dessine.create_image(100,68, image= self.Bulle_image)

        self.show_conseils = Label(self.Canvas_dessine, text = "Conseil: Je te propose \n d'être sûr de ton trajet \n avant de commencer",bg = 'white', font = ("Helvetica", 9))
        self.show_conseils.place(x = 32, y =38 )

        ###############-----------Lancement des fonctions-------------######################
        self.time_num()
        self.restart()
        self.update()

        self.root_tete.mainloop()

    #fonction pour afficher les regles du jeu
    def rules_game(self):
        self.show_rules = Toplevel()

        self.show_rules.title('Règles')
        self.show_rules.geometry('670x530')
        self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking)
        self.show_rules.focus_force()
        self.show_rules.resizable(False,False)

    ################-----------Création des Frames de la fenetre secondaire----------##############
        self.Frame_main1_wind2 = Canvas(self.show_rules, relief = GROOVE)
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 530)

        self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
        self.Frame_main1_wind2.create_image(335,265,image =self.Fond_Frame_main1_wind2)

        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
        self.Frame_main2_wind2.place(x = 60, y = 45)
    ###############---------Création des regles avec animations--------------####################

        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)

    #------------------1----------------------------------------------------------------
        #détail d'une rêgle
        self.Rules2 = Label(self.Frame_main2_wind2, text = "Le but est que le robot arrive au drapeau.\n\
         ", font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(500, lambda: self.Rules2.place(x = 45, y = 70)) #affichage après un délais

        self.CANVAS1 = Canvas(self.Frame_main2_wind2, width = 150, height = 60) #canvas pour afficher l'image
        self.Frame_main2_wind2.after(1000, lambda: self.CANVAS1.place(x = 380, y = 60 )) #placement du canvas
        self.first_photo1 = PhotoImage(file = "Tete_chercheuse/image/first_photo.png") #import de l'image
        self.CANVAS1.create_image(75, 30,image = self.first_photo1) #création de l'image

    #------------------2-----------------------------------------------------------------
        self.Rules3 = Label(self.Frame_main2_wind2, text = 'Pour cela, tu as à disposition des caisses \n\
        qui te permettront de dévier le robot.',font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(2000, lambda: self.Rules3.place(x = 40, y = 150))

        self.CANVAS2 = Canvas(self.Frame_main2_wind2,  width = 130, height = 72)
        self.Frame_main2_wind2.after(2500, lambda: self.CANVAS2.place(x = 390, y = 140 ))
        self.first_photo2 = PhotoImage(file = "Tete_chercheuse/image/second_photo.png")
        self.CANVAS2.create_image(65, 36,image = self.first_photo2)

    #------------------3------------------------------------------------------------------
        self.Rules4 = Label(self.Frame_main2_wind2, text = "A chaque fois que le robot rencontre un obstacle,\n il tourne à SA droite sinon il va toujours tout droit.",font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(3500, lambda: self.Rules4.place(x = 20, y = 240))

        self.CANVAS3 = Canvas(self.Frame_main2_wind2, width = 190, height = 72)
        self.Frame_main2_wind2.after(4000, lambda: self.CANVAS3.place(x = 350, y = 230 ))
        self.first_photo3 = PhotoImage(file = "Tete_chercheuse/image/third_photo.png")
        self.CANVAS3.create_image(95, 36,image = self.first_photo3)

    #------------------4-------------------------------------------------------------------
        self.Rules5 = Label(self.Frame_main2_wind2, text = "Enfin tu peux rencontrer des pièces rouges et \n\
        jaunes, en passant dessus tu gagneras des points. \n\
        Les rouges rapportent plus de points que les jaunes.",font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(5000, lambda: self.Rules5.place(x = 17, y = 320))

        self.CANVAS4 = Canvas(self.Frame_main2_wind2, width = 150, height = 86)
        self.Frame_main2_wind2.after(5500, lambda: self.CANVAS4.place(x = 380, y = 320 ))
        self.first_photo4 = PhotoImage(file = "Tete_chercheuse/image/four_photo.png")
        self.CANVAS4.create_image(75, 43,image = self.first_photo4)

    #--------------5------------------------------------
        self.Bouton_skip = Button(self.Frame_main2_wind2, text = '-Skip-',font = ("Helvetica", 10),cursor ='hand2', relief = GROOVE,command = self.warning)
        self.Bouton_skip.place(x = 200, y = 390)

        self.show_rules.mainloop()

    def quit_ranking(self): #fonction pour quitter la fenetre des rêgles et du classement
        self.show_rules.destroy()
        self.show_rules.quit()

    def quit_rules(self): #fonction pour quiter les rêgles et aller sur les classements
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Tete", self.User_name) #appel de la classe du scoreboard

    def warning(self): #warning appelé au moment du clique sur le bouton skip au niveau des rêgles
        showwarning("Attention", "Attention !! La partie commencera quand tu \n appuyeras sur le bouton 'Continuer' \n et le temps est compté donc prépare-toi.")
        self.quit_rules()

    """######################------------------Début du Jeu---------------------------########################################"""

    def click(self, event): #fonction appelée lors du clique de la souris sur le canvas
        x = event.x #on récupère la position de la souris sur l'écran
        y = event.y

        i = int(x//self.cell_width) #on convertit la position de la souris en indice pour le tableau
        j = int(y//self.cell_height)

        if self.table[i][j] == "0":   # si on se trouve sur une case vide
            self.table[i][j] = "C"    # on ajoute une caisse
            self.box_placed+=1        # et on incrémente le nombre de caisses en actualisant l'affichage
            self.show_count['text'] = "Nombre de palettes: %s" %str(self.box_placed)
        elif self.table[i][j] == "C": # si on clique sur une caisse
            self.table[i][j] = "0"    # on l'enlève
            self.box_placed-=1        # on décrémente le compteur en actualisant l'affichage
            self.show_count['text'] = "Nombre de palettes: %s" %str(self.box_placed)
        elif self.table[i][j] == "P":
            self.nbx +=1
        self.update()

    def click2(self, event):
        x = event.x #on récupère la position de la souris sur l'écran
        y = event.y

        i = int(x//self.cell_width) #on convertit la position de la souris en indice pour le tableau
        j = int(y//self.cell_height)
        if self.table[i][j] == "R":
            self.nbl +=1
        self.update()

    def update(self, Print_Score = True): #fonction pour regénérer l'affichage
        self.Table.delete("all") #on supprime tout ce qu'il y a sur le canvas

        for i in range(self.nbcases_width): #recréation des lignes
            self.Table.create_line((self.cell_width)*i,0,(self.cell_width)*i,500)
        for j in range(self.nbcases_height):
            self.Table.create_line(0,(self.cell_width)*j,500,(self.cell_width)*j)

        self.Table.create_rectangle(2,2,500,500) #contours
        for i in range(10): #pour chaques cases, on regarde ce qu'il y a dans le tableau et on crée l'affichage correspondant
            for j in range(10):
                if (self.table[i][j])=='X':
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.Wall)
                elif self.table[i][j] == "C":
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.Caisse)
                elif (self.table[i][j])=='R':
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.robot[self.index_robot])
                elif (self.table[i][j])=='P':
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.Flag)
                elif (self.table[i][j])=='S':
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.Yellow_Coin)
                elif (self.table[i][j])=='B':
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.Red_Coin)
                elif self.table[i][j] == "E":
                    self.Table.create_image(self.cell_width* i + self.cell_width/2, self.cell_height* j + self.cell_height/2, image = self.End)
        self.root_tete.update()

        if Print_Score == True: #on peut appeler la fonction update sans actualiser le score
            self.show_score["text"] = "Score: %s" %str(int(sum(self.score))) #actualisation du score

    def end_game(self): #fonction appelée quand la partie se termine
        if self.nbx == 3 and self.nbl == 2:
            self.score_temp = 10000 + (10000/(self.box_placed*10 + self.time_game*0.2) + self.score_star) * self.level
        else:
            self.score_temp = (10000/(self.box_placed*10 + self.time_game*0.2) + self.score_star) * self.level #calcul du score
        self.show_score["text"] = "Score: %s"%str(int(sum(self.score + [self.score_temp]))) #on actualise l'affichage
        self.Button_restart["state"] = "disabled" #désactivation du bouton restart
        self.update(False)

        self.question = Toplevel()
        self.question.geometry("300x125")
        self.question.protocol("WM_DELETE_WINDOW", self.exit_menu) #on demande les actions a faire
        self.question.focus_force()
        self.question.resizable(False,False)
        Button(self.question, text = "Restart", command = self.restart_question,cursor ='hand2', font = ("Helvetica", 10)).place(x = 30, y = 45)
        Button(self.question, text = "Main Menu", command = self.exit_menu,cursor ='hand2', font = ("Helvetica", 10)).place(x = 210, y = 45)
        Button(self.question, text = "Next Level", command = self.next,cursor ='hand2', font = ("Helvetica", 10)).place(x = 110, y = 45)

    def restart_question(self): # fonction executée si le joueur veut recommencer le niveau
        self.question.destroy()
        self.question2 = askquestion("RESTART", "Est-tu-sur de recommencer ? Tu perdras à chaque fois 50 points multiplié par le niveau où tu es")
        if self.question2 == "yes": #si l'utilisateur veut recommencer, on regenère l'affichage
            self.restart()
        else: #sinon on redemande l'action a executer
            self.end_game()

        self.box_placed = 0 #nombre de box que l'utilisateur a posé sur la map
        self.time_game = 0 #temps pris par le joueur pour résoudre l'agnime

    def time_num(self): #fonciton pour incrémenter le temps
        self.time_game+=1 # incrémentation de la variable
        self.show_time['text'] = "Temps: %s" %str(self.time_game) #actualisation de l'affichage
        self.root_tete.after(1000,self.time_num) #rappel de la fonction après 1 seconde (1000 ms)

    def next(self): #fonction pour passer au niveau suivant
        self.score[-1] += self.score_temp     # on atribue au dernier niveau joué le score gardé en mémoire
        self.score.append(50*(self.level+1))  # création d'un nouveau slot dans la liste des scores pour le nouveau niveau initié avec une valeur car il y a un malus appliqué dans la foction restart
        self.question.destroy()
        self.level += 1                  # incrémentation du niveau
        if self.level == len(Levels)+1:  # si le joueur a atteint la fin de la liste des niveaux
            self.score[-1] = 0           # le dernier score ne doit pas avoir d'offset
            self.exit()                  # on quitte le jeu en arretant la fonction
            return
        self.Title_level["text"] = "Level {}".format(self.level) #actualisation de l'affichage
        self.restart()                   # régénération de l'affichage

    def start(self): #fonction pour faire bouger le robot
        self.Table.unbind("<Button-1>")          # on désactive le clique et le bouton start
        self.Button_start["state"] = "disabled"
        dir = [1, 0]                        # matrice de mouvement, par défaut, on va a droite
        for i in range(self.nbcases_width):
            for j in range(self.nbcases_height): # on récupère la position du robot en parcourant la liste
                if self.table[i][j] == "R":
                    pos = [i, j]
                    break
        reminder = {} # pour vérifier le nombre de fois qu'on est passé a un meme endroit
        self.run = True    # variable vraie tant qu'on execute la boucle
        while self.run == True:
            sleep(0.4) #on fait avancer le robot toutes les 0.5 secondes
            self.table[pos[0]][pos[1]] = "0" # on remplace la case où il était par une case vide
            x = pos[0] + dir[0] #calcul de la prochaine position
            y = pos[1] - dir[1]
            if self.nbcases_width > x >= 0 and self.nbcases_height > y >= 0 and self.table[x][y] == "0": #si la prochaine position est dans le tableau et que la prochaine case est libre
                pos = [x, y] #on lui assigne la nouvelle position
                try:
                    reminder[(pos[0], pos[1])] += 1     # on essaye d'ajouter 1 à la position actuelle
                    if reminder[(pos[0], pos[1])] > 4:  # si on est passé plus de 4 fois au meme endroit, on restart
                        run = False
                        self.restart()
                        return
                except:
                    reminder[(pos[0], pos[1])] = 1 #si impossible de ajouter 1 c'est que la clef n'est pas crée, on l'initialise a 1

            elif self.nbcases_width > x >= 0 and self.nbcases_height > y >= 0 and self.table[x][y] == "S": #si la prochaine case est une petite pièce
                pos = [x, y]        # on lui atribue la nouvelle position
                self.score_star += 50    # ajout du bonnus
                self.table[x][y] = "0"   # et on vide la case

            elif self.nbcases_width > x >= 0 and self.nbcases_height > y >= 0 and self.table[x][y] == "B": #même chose si la prochaine case est une grosse pièce
                pos = [x, y]
                self.score_star += 150
                self.table[x][y] = "0"


            elif self.nbcases_width > x >= 0 and self.nbcases_height > y >= 0 and self.table[x][y] == "P": #si la prochaine case est le drapeau
                self.table[x][y] = "E" #on change la case actuelle à réussi pour afficher avec le drapeau
                self.run = False #on arrete la boucle
                self.end_game()  #fin du jeu
                return      # fin de la fonction

            else:                                   # sinon, on a un obstacle devant le robot
                dir = [dir[1], -dir[0]]             # rotation d'une matrice [a, b] par -PI/2 en faisant [b, -a]
                self.index_robot = (self.index_robot + 1)%4   # affichage de la rotation
            self.table[pos[0]][pos[1]] = "R"             # on place la robot dans la grille à sa position actuelle
            self.update()

    def restart_button(self): #si on clique sur le bouton pour restart
        self.run = False #on arrete la boucle
        self.restart()   #restart de l'application

    def restart(self): #fonction appelée pour redémarer la partie
        self.Button_restart["state"] = "normal" #on réactive le bouton restart
        self.nbl = 0
        self.nbx = 0
        self.index_robot = 0 #on repositionne le robot à droite
        self.score[-1] -= 50*self.level #pénalité
        self.Button_start["state"] = "normal" #réactivation du bouton start
        self.time_game = self.box_placed = self.score_star = 0 #on réinitaialise des variables de jeu
        self.Table.bind("<Button-1>", self.click)  #rebind du clique droit
        self.Table.bind("<Button-2>", self.click2)
        self.show_time['text'] = "Temps: %s" %str(self.time_game) #actualisation des affichages
        self.show_count['text'] = "Nombre de palettes: %s" %str(self.box_placed)

        for i in range(self.nbcases_width):
            for j in range(self.nbcases_height):
                self.table[i][j] = Levels[self.level-1][(j*self.nbcases_width)+i] #réinitialisation de la table
        self.update()

    def exit_menu(self): #fonction pour quiter le jeu à partir des questions
        self.score[-1] += self.score_temp # on lui attribue le score gardé en mémoire
        self.exit()                  # et on quitte l'application

    def exit(self): #fonction pour quitter, elle se charge de détruire les fenètres lancées
        try:
            self.question.destroy()
        except: pass
        self.root_tete.quit()
        self.root_tete.destroy()

def Tete(user): #fonction principale
    jeu = application(user)
    return sum(jeu.score) #retour du score total du joueur sur tout les niveaux joués
