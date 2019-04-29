from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import randint
from math import*

class bird:
    def __init__(self,user):
        self.User_name = user
        self.Best_Score = 0
        self.show_rules = Toplevel()
        self.show_rules.title('Règles')
        self.show_rules.geometry('670x530')
        self.show_rules.resizable(False,False)
        self.show_rules.focus_force()
        self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking)

        self.Frame_main1_wind2 = Canvas(self.show_rules, bg = 'red', relief = GROOVE)
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 526)
        #self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Ghost2.png")
        #self.Frame_main1_wind2.create_image(335,263,image =self.Fond_Frame_main1_wind2)
        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
        self.Frame_main2_wind2.place(x = 60, y = 45)
        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)

        self.Jerry_1 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_1.png")
        self.keyboard_fantome = PhotoImage(file = "Fantome/Ressources/Images/keyboard_fantome.png")
        self.Jerry_3 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_3.png")
        self.Jerry_2 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_2.png")

        #détail des rêgles

        self.Rules2 = Label(self.Frame_main2_wind2, text = "Le but est que Jerry puisse arriver \n\
        au fromage sans que Tom l'attrape. \n Pour cela tu pourras utiliser les flèches \n du keyboard afin de déplacer Jerry", font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(500, lambda: self.Rules2.place(x = 40, y = 70))

        self.CANVAS1 = Canvas(self.Frame_main2_wind2, width = 120, height = 70)
        self.CANVAS2 = Canvas(self.Frame_main2_wind2, width = 100, height = 70)
        self.Frame_main2_wind2.after(1000, lambda: self.CANVAS1.place(x = 388, y = 35))
        self.Frame_main2_wind2.after(1000, lambda: self.CANVAS2.place(x = 400, y = 106))
        self.CANVAS1.create_image(60, 35,image = self.Jerry_1)
        self.CANVAS2.create_image(50, 35,image = self.keyboard_fantome)
        self.CANVAS2.create_rectangle(2,2,98,68, outline='black')

    #------------------2-----------------------------------------------------------------
        self.Rules3 = Label(self.Frame_main2_wind2, text = "Mais Attention !! Tom va plus vite que toi car il peut \n\
        se déplacer en diagonale. Tom se déplace par \n rapport à Jerry et fait tout pour se rapprocher." ,font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(2000, lambda: self.Rules3.place(x = 30, y = 202))

        self.CANVAS3 = Canvas(self.Frame_main2_wind2,  width = 100, height = 100)
        self.Frame_main2_wind2.after(2500, lambda: self.CANVAS3.place(x = 400, y = 183 ))
        self.CANVAS3.create_image(50,50, image = self.Jerry_3)

    #------------------3------------------------------------------------------------------
        self.Rules4 = Label(self.Frame_main2_wind2, text = "L'astuce est alors de bloquer le robot grâce\n\
        aux bloques disposés sur la carte",font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(3500, lambda: self.Rules4.place(x = 40, y = 315))

        self.CANVAS4 = Canvas(self.Frame_main2_wind2, width = 130, height = 95)
        self.Frame_main2_wind2.after(4000, lambda: self.CANVAS4.place(x = 388, y = 293 ))
        self.CANVAS4.create_image(65, 47,image = self.Jerry_2)

    #------------------Skip------------------------------------------------------------------
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", cursor ='hand2', command = self.quit_rules)
        self.Button_Skip.place(x = 200, y = 390)
        self.show_rules.mainloop()

        """#################----------------- début du jeu ----------------#################### """
        self.root = Toplevel()
        self.root.geometry("900x620")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.resizable(False,False)
        self.root.title('Flappy Bird')
        self.root.focus_force()

        self.liste_image = []                      #Import des photos du Bird pour les différents angles
        for i in range(2,31):
            self.liste_image.append(PhotoImage(file = 'Flappy_Bird/Ressources/{}.png'.format(i)))

        self.background = []                       #Import des photos du décor mis au hasard
        for k in range(6):
            self.background.append(PhotoImage(file = 'Flappy_Bird/Ressources/decor{}.png'.format(k+1)))

        self.liste_nombres = []                     #Import des photos des nombres pour le score
        for p in range(10):
            self.liste_nombres.append(PhotoImage(file = 'Flappy_Bird/Ressources/u{}.png'.format(p)))

        self.ground_image = PhotoImage(file = 'Flappy_Bird/Ressources/ground.png')
        self.tap = [PhotoImage(file = 'Flappy_Bird/Ressources/tap_right.png'), PhotoImage(file = 'Flappy_Bird/Ressources/tap_left.png')]
        self.hand_image = PhotoImage(file = 'Flappy_Bird/Ressources/hand.png')
        self.image = PhotoImage(file = "Flappy_Bird/Ressources/game_over.png")
        self.build_game()
        self.root.mainloop()

    """##########--------------Fonctions servant aux fenetres--------------------#################"""
    def quit_rules(self):
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Flappy", self.User_name)

    def quit_ranking(self):
        self.show_rules.destroy()
        self.show_rules.quit()

    def exit(self):
        self.root.destroy()
        self.root.quit()

    """#############################################################################################"""

    def test_press(self,  event = None): #Fonction servant à recevoir le click du joueur
        self.play = True
        self.press = True                #Initialisation de press à chaque click servant à ce que l'oiseau monte
        self.i = 0                       #Initialisation de i à chaque click servant à la montée de l'oiseau

    def build_game(self):          #Fonction servant au lancement du jeu (appellée à chaque restart)
        self.root.focus_force()
        self.root.bind("<space>", self.test_press)
        self.root.bind("<Button-1>", self.test_press)

        ########-----------Frames Principaux------------#######################################
        self.Frame_left = Frame(self.root, width = 200, height = 570, bg = 'white')
        self.Frame_top = Frame(self.root, width = 900, height = 50, bg = 'grey')
        self.Frame_right = Frame(self.root, width = 700, height = 570, bg = 'black')

        ########-----------Frames Secondaires------------#######################################
        self.Frame1 = Frame(self.Frame_left, width = 200, height = 200, bg = 'yellow')
        self.Frame2 = Frame(self.Frame_left, width = 200, height = 300, bg = 'red')

        #######-----------Package des Frames-------------####################################
        self.Frame_top.pack(side = TOP)
        self.Frame_left.pack(side = LEFT)
        self.Frame1.pack(side = TOP)
        self.Frame2.pack(side = BOTTOM)
        self.Frame_right.pack(side = RIGHT)


        ######-----------Elements du jeu-----------------##########################################
        self.sentence = Label(self.Frame2, text = "Attrape Moi \n Si Tu Peux !!!",font = ("Berlin Sans FB", 15), bg = 'white')
        self.sentence.place(x = 45, y = 60)

        self.canvas_show_time = Canvas(self.Frame1, bg = 'black',highlightthickness=0)
        self.canvas_show_time.place(x = 10, y = 30)

        self.show_time = Label(self.canvas_show_time, text = "Temps: %s" %str(0), foreground = 'blue2', bg = 'black',font = ("Berlin Sans FB", 24))
        self.show_time.pack(padx= 3, pady = 3)

        bestplayer = get_game_score_list("Flappy")[0]
        self.best_label = Label(self.Frame_top, text = "Meilleur joueur:\n{} avec {} points".format(bestplayer[0], int(bestplayer[1])), bg = "black", fg = "#00cc00") #je te laisse la mise en forme
        self.best_label.place(x = 30, y = 15)


        #######---------------Variables du jeu-------------###########################
        self.x = 0                      #Déplacement du bird en x
        self.y = -2.9                   #Déplacement en vitesse du bird en y (en montée)
        self.vitesse = 0                #Déplacement en vitesse du bird en y (en descente, ensuite augmentée)
        self.vitesse_wait = 0           #Déplacement en vitesse du bird en y lorsqu'il attend le début de la partie

        self.compte = 0                 #Score du joueur
        self.count_image = 8            #Départ du jeu à l'image 8
        self.Best_Score = 0             #Init du meilleur score à retenir

        self.play = False               #Variable servant à declencher le début de la partie
        self.wait = True                #Variable servant à savoir quand descendre ou monter (bird en attente)
        self.press = False              #Variable servant à savoir si le joueur a appuyé pour sauter
        self.verite = True              #Variable servant à savoir si la fonction update fonctionne ou non

        self.u = 0                      #Unité pour l'affichage du score
        self.d = 0                      #Dizaine pour l'affichage du score
        self.c = 0                      #Centaine pour l'affichage du score
        ###############################################################################

        ############--------------Labels/Canvas et autres-----------------###################
        self.Canvas_world = Canvas(self.Frame_right, width = 1700, height = 500, highlightthickness=0)
        self.Canvas_world.place(x = 0, y = 0)

        self.Canvas_ground = Canvas(self.Frame_right, width = 900, height = 70, highlightthickness=0)
        self.Canvas_ground.place(x = 0, y = 500)

        self.Canvas_world.create_image(350,250,  image = self.background[randint(0,5)])
        self.ground = self.Canvas_ground.create_image(450,35,  image = self.ground_image)

        ##########----------Création des images servant à l'attente du clic-----------------###############
        self.tap1 = self.Canvas_world.create_image(285,250,  image = self.tap[1])
        self.tap2 = self.Canvas_world.create_image(415,250,  image = self.tap[0])
        self.hand = self.Canvas_world.create_image(350,300,  image = self.hand_image)

        self.image_Bird = self.Canvas_world.create_image(350,220,  image = self.liste_image[int(self.count_image)]) #Image de l'oiseau dans l'attente
        self.image_unite = self.Canvas_world.create_image(350,30,  image = self.liste_nombres[self.u]) #Image du score(unité)
        self.wait_game()

    def wait_game(self,event = None):       #Fonction servant à bouger l'oiseau de haut en bas dans l'attente
        if self.play == False:              #Si le joueur n'as toujours pas appuyé, la fonction s'éxécute en boucle
            if self.wait == True:           #Si self.wait == True, alors l'oiseau monte
                self.vitesse_wait += 0.9
                self.Canvas_world.move(self.image_Bird, 0 ,self.vitesse_wait)
                if  self.vitesse_wait > 7:  #Si il atteind la limite, self.wait = False et l'oiseau descend
                    self.wait = False
                    self.vitesse_wait = 0   #On réinitialise la variable à 0 pour la descente
            elif self.wait == False:                                            ###########################
                self.vitesse_wait -= 0.9                                        #
                self.Canvas_world.move(self.image_Bird, 0 ,self.vitesse_wait)   #    Même résonnement
                if  self.vitesse_wait < -7:                                     #
                    self.wait = True                                            #
                    self.vitesse_wait = 0                                       ###########################
            self.root.after(75,self.wait_game)

        elif self.play == True:             #Le joueur a appuyé sur la touche, la fonction s'arrête et passe à la suivante
            self.move_bird_begin()

    def move_bird_begin(self):              #Fonction servant à déplacer l'oiseau jusqu'à la zone où il pourra sauter
        self.Canvas_world.delete(self.tap1) #~~~~~~~~~~~~~~~~~~~~~~~~
        self.Canvas_world.delete(self.tap2) #On supprime~alors les anciens éléments servant à l'attente
        self.Canvas_world.delete(self.hand) #~~~~~~~~~~~~~~~~~~~~~~
        vitesse = -12                       #Vitesse de déplacement du sol et de l'oiseau
        x, y =  self.Canvas_ground.coords(self.ground) #Coordonées du sol
        x1, y1 =  self.Canvas_world.coords(self.image_Bird) #Coordonées de l'oiseau
        self.Canvas_ground.move(self.ground, vitesse,0)
        if x < 260:                                         #Si le centre du sol dépasse 260, il repart du début
            self.Canvas_ground.coords(self.ground, 450,35)

        if x1 + vitesse > 100:                      #Tant que l'abscisse de l'oiseau est supérieur à 100, la fonction tourne en boucle
            if self.wait == True:                                                   ####################################
                self.vitesse_wait += 0.9                                            #
                self.Canvas_world.move(self.image_Bird, vitesse ,self.vitesse_wait) #
                if  self.vitesse_wait > 7:                                          #
                    self.wait = False                                               #
                    self.vitesse_wait = 0                                           #   Même résonnement qu'à la fonction
            elif self.wait == False:                                                #   précédente pour le déplacement vertical,
                self.vitesse_wait -= 0.9                                            #   on rajoute seulement le déplacement horizontal ici
                self.Canvas_world.move(self.image_Bird, vitesse ,self.vitesse_wait) #
                if  self.vitesse_wait < -7:                                         #
                    self.wait = True                                                #
                    self.vitesse_wait = 0                                           #
            self.root.after(50,self.move_bird_begin)                                ####################################
        else:
            self.Canvas_world.coords(self.image_Bird, 125, 220) #On réinitialise les coordonnées de l'oiseau
            self.press = False  #On réinitialise self.press = False pour que l'oiseau descende au début de partie
            self.start()

    def start(self):    #Fonction servant à créer le nouvel oiseau qui pourra voler et les 4 tuyaux
        self.Canvas_world.delete(self.image_Bird)   #Suppression de l'ancien oiseau
        self.root.focus_force()
        self.tuyau0 = Pipe(self)                    ####################
        self.tuyau1 = Pipe(self)                    # création des 4 objets tuyau à l'aide de la classe Pipe
        self.tuyau2 = Pipe(self)                    #
        self.tuyau3 = Pipe(self)                    ##################

        self.tuyau0.create_pipe(1100,350)                   ################################
        self.tuyau1.create_pipe(1500, randint(200,400))     # création des 4 tuyaux à l'aide de la fonction create_pipe
        self.tuyau2.create_pipe(1900, randint(100,300))     # appartenant à la classe Pipe
        self.tuyau3.create_pipe(2300, randint(100,400))     ################################

        self.image_Bird_true = self.Canvas_world.create_image(125,220,  image = self.liste_image[int(self.count_image)])    #Création du nouvel oiseau
        self.Canvas_world.tag_raise(self.image_unite)   #Mise en avant du score (unité)
        self.update()

    def update(self):  #Fonction servant à relancer différentes fonctions toutes le 50 ms
        if self.verite == True:         #La fonction s'éffectue si self.verite == True
            self.bird_move()            #Déplacement de l'oiseau
            self.tuyau0.move_pipe()     #######################
            self.tuyau1.move_pipe()     #Déplacement des tuyaux
            self.tuyau2.move_pipe()     #
            self.tuyau3.move_pipe()     #######################
            self.root.after(50,self.update)

    """
    La fonction Bird_move sert à déplacer l'oiseau de bas en haut ou de haut en bas. Elle sert aussi à changer l'inclinaison
    de la tête de l'oiseau en fonction de la vitesse de descente. Tout d'abord, on place toute la fonction dans une boucle qui
    se répète 6 fois afin de faire plus de calculs et d'être plus précis.
    L'oiseau va donc commencer à descendre puisque la dernière valeur de self.press = False.

    Pour la montée, self.press = True grâce au click du joueur, l'oiseau va donc monter de 2.9 pixels multiplié par 6 toutes
    les 50 ms. Pour éviter que l'oiseau ne s'envole vers l'infini, on pose i = 0 et à chaque tour on l'incrémente de 1, ainsi au
    bout de 30 calculs la fonction s'arrete et l'oiseau aura monté de 87 pixels en 250 ms. En ce qui concerne l'inclinaison de
    l'oiseau, on connait la derniere valeur de l'image de la descente avec self.count_image, on va lui soustraire à chaque boucle
    -1,2. La liste_image contient 30 images de l'oiseau ce qui permet d'avoir une bonne précision sur l'inclinaison de l'oiseau.
    A la fin, quand i == 30, self.press = False et l'oiseau va alors descendre.

    Pour la descente, self.press = False, on fait toujours tourner l'algorithme dans la boucle for pour la même raison.
    On sépare tout d'abord l'algo en 2 partie, la 1ère où self.count_image < 27 et l'autre où self.count_image > 29. On sépare de
    cette manière afin de ne pas augmenter self.count_image lorsqu'on est à la dernière image pour éviter d'avoir l'erreur
    (IndexError: list index out of range) car self.count_image augmente à chaque boucle. Pour simuler une chute de l'oiseau,
    on multiplie self.count_image par 1.04 et par 1.1 si  self.count_image > 5. Après avoir fait ceci, on passe au déplacement de l'oiseau, on commence
    alors par incrémenter la vitesse de +0.055 à chaque boucle. En même temps que de déplacer l'oiseau, on vérifie aussi si
    l'oiseau ne touche pas le sol avec if (self.y_center_bird +self.vitesse + 25) > 500, ainsi si cette condition est vérifiée,
    on place l'oiseau à y = 475 afin d'être sûr qu'il touche bien sans dépasser le sol, on appelle la fonction vérif qui nous
    sert à afficher le Game Over et self.verite = False afin d'arrêter la boucle de la fonction update.
    """
    def bird_move(self): #Fonction servant à déplacer le sol et l'oiseau pendant le jeu
        x, y =  self.Canvas_ground.coords(self.ground)      ############################
        self.Canvas_ground.move(self.ground, -12,0)         #   Déplacement du sol
        if x < 260:                                         #
            self.Canvas_ground.coords(self.ground, 450,35)  ############################
        for _ in range(6): #Début de la boucle pour plus de calculs et de précision
            if self.press == True:  #La montée de l'oiseau
                self.i +=1          #On incrémente i de 1
                self.vitesse = 0    #On réinitialise la vitesse pour la déscente
                self.x_center_bird, self.y_center_bird=  self.Canvas_world.coords(self.image_Bird_true) #Coordonées de l'oiseau qui servent ensuite à la fonction verif_bird
                self.Canvas_world.move(self.image_Bird_true, self.x,self.y) #Déplacement de l'oiseau
                self.Canvas_world.itemconfigure(self.image_Bird_true, image = self.liste_image[int(self.count_image)])  #Changement de l'inclinaison de l'oiseau
                if self.i >= 30:    #Grace à ctte condition, on effectue 30 calculs et on recommence la descente avec self.press = False
                    self.press = False
                    self.count_image = 0.5 #On réinitialise self.count_image = 0.5 pour la descente
                else:                           ################################
                    if self.count_image > 0:    # Sinon:
                        self.count_image -= 1.2 # On baisse self.count_image à chaque boucle
                    else:                       # jusqu'à ce self.count_image = 0
                        self.count_image = 0    ################################

            elif self.press == False:           #La descente de l'oiseau
                if self.count_image < 25:       #Si self.count_image < 27, pour éviter index out of range
                    if self.count_image > 5:    #Si self.count_image > 5:
                        self.count_image *=1.1  #On multiplie self.count_image par 1.1
                    else:                       #Sinon
                        self.count_image *=1.04 #On multiplie self.count_image par 1.4 pour faire accéler l'inclinaison
                    self.vitesse +=0.055        #La vitesse est toujours augmentée
                    self.x_center_bird, self.y_center_bird =  self.Canvas_world.coords(self.image_Bird_true)#On récupérer les coordonnées de l'oiseau
                                                                                                #########################################
                    if (self.y_center_bird +self.vitesse + 25) > 500:                           #Grace aux coordonées, on vérifie si l'oiseau ne touche pas le sol
                        self.Canvas_world.coords(self.image_Bird_true, self.x_center_bird, 475) #Si oui: on le positione à y = 475 et on
                        self.verif_bird(0,0,b = True)                                           #appelle la fonction verif_bird avec b = True (IMPORTANT), cela sert à
                                                                                                #ne pas lancer la fonction wait_dead ensuite ainsi que l'arret de la fonction update
                    else:                                                                       #Sinon:
                        self.Canvas_world.move(self.image_Bird_true, self.x,self.vitesse)       #On déplace l'oiseau et on change son inclinaison avec itemconfigure
                        self.Canvas_world.itemconfigure(self.image_Bird_true, image = self.liste_image[int(self.count_image)])

                                                ############################################################################
                else:                           #Si self.count_image > 27
                    self.vitesse +=0.055        #On effectue la même chose qu'au dessus sans changer l'inclinaison
                    self.x_center_bird, self.y_center_bird =  self.Canvas_world.coords(self.image_Bird_true)############################
                    if (self.y_center_bird +self.vitesse + 25) > 500:                                       #
                        self.Canvas_world.coords(self.image_Bird_true, self.x_center_bird, 475)             #
                        self.verif_bird(0,0,b = True)                                                       # Même résonnement
                    else:                                                                                   #
                        self.Canvas_world.move(self.image_Bird_true, self.x,self.vitesse)                   ############################


    def verif_bird(self, y_pipe_center_top , y_pipe_center_down ,b = False): #Fonction serant à vérifier si l'oiseau rentre en contact avec le tuyau ou non
        if self.verite == True: #Cette condition sert à n'executer qu'une fois cette fonction car après l'appel de celle-ci, self.verite = False
            self.y_pipe_down = y_pipe_center_down - 250 #Valeur du haut du tuyau bas
            self.y_pipe_top = y_pipe_center_top + 250   #Valeur du bas du tuyau haut
            if self.y_pipe_down<self.y_center_bird + 24 or self.y_center_bird - 24< self.y_pipe_top or b == True: #Si il y a touche du sol ou du tuyau
                self.root.unbind("<Button-1>")          #On évite que le joueur click ce qui peut faire bugger le programme
                self.root.unbind("<space>")
                self.verite = False                     #On réinitialise self.verite = False pour éviter de refaire la fonction
                self.tempo_image = self.image.subsample(4) #image de game over réduite de 400%
                self.image_game_over = self.Canvas_world.create_image(350,250,  image = self.tempo_image) #création de l'image de game over
                self.Canvas_world.after(500, self.ending)
                self.Canvas_world.after(1000, lambda: self.ending(True))
                if b == True:                           #Cette condition sert à différencier
                    self.root.after(2000, self.dead)    #si la mort vient du sol ou du tuyau
                else:                                   #ainsi si b == True, on n'appelle pas wait_dead puique l'oiseau est déjà au sol
                    self.wait_dead()                    #sinon, on appelle wait_dead qui sert à faire descendre l'oiseau quand il est mort
                    self.root.after(2000, self.dead)    #on appelle dead dans les 2 cas avec un temps de latence afin de voir le Game Over

    def ending(self, a = False) :#fonction pour afficher l'annimation de l'apparition du game over
        if a == False:
            self.image = self.image.subsample(2) #la première fois que la fonction est appelée, on affiche l'image réduite à 200%
        else:
            self.image = self.image.zoom(2) #affichage de l'image zoomée de 200% à la 2nd exécution de la fonction
        self.Canvas_world.itemconfig(self.image_game_over, image = self.image)

    def wait_dead(self): #Fonction servant à faire descendre l'oiseau lorsque ce dernier a touché un tuyau
        x, y =  self.Canvas_world.coords(self.image_Bird_true) #On récupère les coordonnées de l'oiseau au moment de sa mort
        self.Canvas_world.tag_raise(self.image_game_over)      #On le place au premier plan devant les tuyaux
        if y + self.vitesse +25< 500: #Condition pour savoir si il a atteint le sol ou non
            self.count_image *=1.5    #On augmente count_image pour augmenter l'inclinaison
            if self.count_image < 250:#Si self.count_image < 250, on continue à itemconfigure avec image = self.liste_image[int(abs(self.count_image)/10)]
                self.Canvas_world.itemconfigure(self.image_Bird_true, image = self.liste_image[int(abs(self.count_image)/10)])
                self.vitesse +=0.5 #On augmente la vitesse de descente
                self.Canvas_world.move(self.image_Bird_true, self.x,self.vitesse)#On déplace l'oiseau
            else:                     #Si self.count_image > 250, on fait les mêmes déplacements en mettant l'inclinaison à image = self.liste_image[28]
                self.Canvas_world.itemconfigure(self.image_Bird_true, image = self.liste_image[28])
                self.vitesse +=0.5 #On augmente la vitesse de descente
                self.Canvas_world.move(self.image_Bird_true, self.x,self.vitesse)#On déplace l'oiseau
            self.root.after(25,self.wait_dead)#On éxécute la fonction tant que l'oiseau n'a pas touché le sol
        else:   #Si il touche le sol, la boucle s'arrête et on place l'oiseau à y = 475 pour être sur qu'il ne dépasse pas le sol
            self.Canvas_world.coords(self.image_Bird_true, x, 475)#On replace l'oiseau



    def dead(self):
        if (self.compte)*40 > self.Best_Score: # si on a fait un meilleur score que l'ancien on l'enregistre
            self.Best_Score = (self.compte)*100

        question = askquestion("RESTART", "Perdu!\nVeux-tu recommencer")
        if question == "yes":                        # si l'utilisateur veut recommencer, on regenère l'affichage
            self.Frame_right.destroy()               # destruction des frames
            self.Frame_left.destroy()                #
            self.Frame_top.destroy()                 #
            self.build_game()                        # reconstruction de la fenètre
        else:
            self.exit()                              #sinon, on quitte l'application

    def count_score(self):#Fonction servant à afficher le socre au milieu en haut de la partie en cours
        if self.compte == 10:   #Si le compte = 10, on crée l'image du chiffre des dizaines
            self.image_dizaine = self.Canvas_world.create_image(322,30,  image = self.liste_nombres[self.d])
        elif self.compte == 100:#Si le compte = 100, on crée l'image du chiffre des centaines
            self.image_centaine = self.Canvas_world.create_image(304,30,  image = self.liste_nombres[self.c])
        self.u+=1               #On incrémente le chiffre des unités à chaque tuyau
        if self.u >9:           #Si le chiffre des unités dépasse 9
            self.u =0           #On le réinitialise à 0
            self.d+=1           #Et on incrémente le chiffre des dizaines tous les 10 tuyaux
            if self.d >9:       #Si le chiffre des dizaines dépasse 9
                self.d = 0      #On le réinitialise à 0
                self.c+=1       #Et on incrémente le chiffre des centaines tous les 100 tuyaux
                self.Canvas_world.itemconfigure(self.image_centaine, image = self.liste_nombres[self.c])#On itemconfigure le chiffre des centaines si il le faut
            self.Canvas_world.itemconfigure(self.image_dizaine, image = self.liste_nombres[self.d])#On itemconfigure le chiffre des dizaines si il le faut
        self.Canvas_world.itemconfigure(self.image_unite, image = self.liste_nombres[self.u])#On itemconfigure le chiffre des unités à chaque fois
        self.Canvas_world.tag_raise(self.image_unite)#On met en avant devant les tuyaux à chaque fois
        if self.compte >=10:
            self.Canvas_world.tag_raise(self.image_dizaine)#On met en avant le chiffre des centaines devant les tuyaux si il le faut
        if self.compte >=100:
            self.Canvas_world.tag_raise(self.image_centaine)#On met en avant le chiffre des centaines devant les tuyaux si il le faut
        self.Canvas_world.tag_raise(self.image_Bird_true)#On met en avant l'oiseau à chaque fois

class Pipe:                     #Creéation de la classe Pipe
    def __init__(self, parent): #Argument qui sert à récupérer les variables de la classe Flappy
        self.parent = parent    #
        self.move_x = -12       #Vitesse de déplacement des tuyaux
        self.test = PhotoImage(file = 'Flappy_Bird/Ressources/test.png')    #Tuyau du bas
        self.test3 = PhotoImage(file = 'Flappy_Bird/Ressources/test3.png')  #Tuyau du haut
        self.length_pipe = 500  #Taille de l'image des tuyaux, utile pour les calculs de placement du tuyau

    def create_pipe(self, x_pipe, y_pipe):  #Fonction servant à créer l'image du tuyau, appellée à chaque fois qu'un tuyau quitte l'écran
        self.y_pipe_top = y_pipe - 75       #Permet de créer l'espace entre les 2 tuyaux
        self.y_pipe_down = y_pipe + 75      #ce qui fait un écart de 150 pixels
        self.top_pipe =  self.parent.Canvas_world.create_image(x_pipe + 75, self.y_pipe_top - self.length_pipe/2,  image = self.test3) #Création du tuyau haut
        self.down_pipe =  self.parent.Canvas_world.create_image(x_pipe + 75,self.y_pipe_down + self.length_pipe/2 ,  image = self.test)#Création du tuyau bas
    def move_pipe(self):  #Fonction servant à déplacer le tuyau à l'horizontal, la fonction tourne toutes les 50ms, grace à update
        self.parent.Canvas_world.move(self.top_pipe, self.move_x,0) #Déplacement des 2 tuyaux
        self.parent.Canvas_world.move(self.down_pipe, self.move_x,0)#
        self.x_center_top_pipe, self.y_center_top_pipe =  self.parent.Canvas_world.coords(self.top_pipe)    #On récupère les coordonées des 2
        self.x_center_down_pipe, self.y_center_down_pipe =  self.parent.Canvas_world.coords(self.down_pipe) #tuyaux qui serviront à verif_pipe
        self.verif_pipe()   #On appelle verif_pipe à chaque déplacement du tuyau

    def verif_pipe(self):   #Fonction servant à vérifier si le tuyau dans des intervalles donnés
        if self.x_center_top_pipe + 65 < 0:#Si le tuyau a quitté l'écran, on le supprime et on le recréer directement caché à droite
            self.parent.Canvas_world.delete(self.top_pipe)  #Supression du haut
            self.parent.Canvas_world.delete(self.down_pipe) #Suppresion du bas
                                                            #Au lieu de le supprimer et de le recréer on aurait pu le changer de place,
                                                            #Le problème aurait été que l'ecart entre les 2 tuyaux serait trouvé toujours au même endroit du tuyau concerné
            self.create_pipe(randint(1400, 1500), randint(100,400))#Création du nouveau tuyau, les randint servent à donner plus de fun et de difficultés au jeu

        if 100<self.x_center_top_pipe + 60 <150 or 100<self.x_center_top_pipe - 60 <150:#Si le tuyau se trouve entre 100 et 150 pixels (c'est à dire au niveau de l'oiseau)
            self.parent.verif_bird(self.y_center_top_pipe,self.y_center_down_pipe)#On appelle la fonction verif_bird permettant de voir si il y contact ou non

        if 100>=self.x_center_top_pipe + 60 >88:#Si le tuyau dépassé l'oiseau, l'interval est de 12 pixels car le tuyau se déplaces de 12 lui aussi toules 50ms
            self.parent.compte+=1       #Le score augmente de 1
            self.parent.count_score()   #On appelle count_score pour l'affichage du score

def Flappy_Bird(User):    # fonction pour commencer le jeu
  jeux = bird(User)       # création de l'instance
  return jeux.Best_Score  #renvois du meilleur score
