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

def rules_game(): #fonction pour afficher les regles du jeu
    global show_rules, Frame_main2_wind2, Frame_main1_wind2
    show_rules = Toplevel()

    show_rules.title('Règles')
    show_rules.geometry('670x530')
    show_rules.protocol("WM_DELETE_WINDOW", quit_ranking)

################-----------Création des Frames de la fenetre secondaire----------##############
    Frame_main1_wind2 = Canvas(show_rules, relief = GROOVE)
    Frame_main1_wind2.pack(ipadx = 670, ipady = 530)

    Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
    Frame_main1_wind2.create_image(335,265,image =Fond_Frame_main1_wind2)

    Frame_main2_wind2 = Frame(Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
    Frame_main2_wind2.place(x = 60, y = 45)
###############---------Création des regles avec animations--------------####################

    Rules = Label(Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
    Rules.place(x = 200, y =5)

#------------------1----------------------------------------------------------------
    #détail d'une rêgle
    Rules2 = Label(Frame_main2_wind2, text = "Le but est que le robot arrive au drapeau.\n\
     ", font = ("Berlin Sans FB", 12))
    Frame_main2_wind2.after(500, lambda: Rules2.place(x = 45, y = 70)) #affichage après un délais

    CANVAS1 = Canvas(Frame_main2_wind2, width = 150, height = 60) #canvas pour afficher l'image
    Frame_main2_wind2.after(1000, lambda: CANVAS1.place(x = 380, y = 60 )) #placement du canvas
    first_photo1 = PhotoImage(file = "Rules_tete_photo/first_photo.png") #import de l'image
    CANVAS1.create_image(75, 30,image = first_photo1) #création de l'image

#------------------2-----------------------------------------------------------------
    Rules3 = Label(Frame_main2_wind2, text = 'Pour cela, tu as à disposition des caisses \n\
    qui te permettront de dévier le robot.',font = ("Berlin Sans FB", 12))
    Frame_main2_wind2.after(2000, lambda: Rules3.place(x = 40, y = 150))

    CANVAS2 = Canvas(Frame_main2_wind2,  width = 130, height = 72)
    Frame_main2_wind2.after(2500, lambda: CANVAS2.place(x = 390, y = 140 ))
    first_photo2 = PhotoImage(file = "Rules_tete_photo/second_photo.png")
    CANVAS2.create_image(65, 36,image = first_photo2)

#------------------3------------------------------------------------------------------
    Rules4 = Label(Frame_main2_wind2, text = "A chaque fois que le robot rencontre un obstacle, \n\
    il tourne à droite sinon il va toujours tout droit.",font = ("Berlin Sans FB", 12))
    Frame_main2_wind2.after(3500, lambda: Rules4.place(x = 20, y = 240))

    CANVAS3 = Canvas(Frame_main2_wind2, width = 190, height = 72)
    Frame_main2_wind2.after(4000, lambda: CANVAS3.place(x = 350, y = 230 ))
    first_photo3 = PhotoImage(file = "Rules_tete_photo/third_photo.png")
    CANVAS3.create_image(95, 36,image = first_photo3)

#------------------4-------------------------------------------------------------------
    Rules5 = Label(Frame_main2_wind2, text = "Enfin tu peux rencontrer des pièces rouges et \n\
    jaunes, en passant dessus tu gagneras des points. \n\
    Les rouges rapportent plus de points que les jaunes.",font = ("Berlin Sans FB", 12))
    Frame_main2_wind2.after(5000, lambda: Rules5.place(x = 17, y = 320))

    CANVAS4 = Canvas(Frame_main2_wind2, width = 150, height = 86)
    Frame_main2_wind2.after(5500, lambda: CANVAS4.place(x = 380, y = 320 ))
    first_photo4 = PhotoImage(file = "Rules_tete_photo/four_photo.png")
    CANVAS4.create_image(75, 43,image = first_photo4)

#--------------5------------------------------------
    Bouton_skip = Button(Frame_main2_wind2, text = '-Skip-',font = ("Helvetica", 10),cursor ='hand2', relief = GROOVE,command = warning)
    Bouton_skip.place(x = 200, y = 390)

    show_rules.mainloop()

def quit_ranking(): #fonction pour quitter la fenetre des rêgles et du classement
    show_rules.destroy()
    show_rules.quit()

def quit_rules(): #fonction pour quiter les rêgles et aller sur les classements
    Frame_main2_wind2.destroy()
    Scoreboard(Frame_main1_wind2, show_rules, "Tete", User_name) #appel de la classe du scoreboard

def warning(): #warning appelé au moment du clique sur le bouton skip au niveau des rêgles
    showwarning("Attention", "Attention !! La partie commencera quand tu \n appuyeras sur le bouton 'Continuer' \n et le temps est compté donc prépare-toi.")
    quit_rules()

"""######################------------------Début du Jeu---------------------------########################################"""

def click(event): #fonction appelée lors du clique de la souris sur le canvas
    global box_placed
    x = event.x #on récupère la position de la souris sur l'écran
    y = event.y

    i = int(x//cell_width) #on convertit la position de la souris en indice pour le tableau
    j = int(y//cell_height)

    if table[i][j] == "0":   # si on se trouve sur une case vide
        table[i][j] = "C"    # on ajoute une caisse
        box_placed+=1        # et on incrémente le nombre de caisses en actualisant l'affichage
        show_count['text'] = "Nombre de palettes: %s" %str(box_placed)
    elif table[i][j] == "C": # si on clique sur une caisse
        table[i][j] = "0"    # on l'enlève
        box_placed-=1        # on décrémente le compteur en actualisant l'affichage
        show_count['text'] = "Nombre de palettes: %s" %str(box_placed)
    update()

def update(Print_Score = True): #fonction pour regénérer l'affichage
    Table.delete("all") #on supprime tout ce qu'il y a sur le canvas

    for i in range(nbcases_width): #recréation des lignes
        Table.create_line((cell_width)*i,0,(cell_width)*i,500)
    for j in range(nbcases_height):
        Table.create_line(0,(cell_width)*j,500,(cell_width)*j)

    Table.create_rectangle(2,2,500,500) #contours
    for i in range(10): #pour chaques cases, on regarde ce qu'il y a dans le tableau et on crée l'affichage correspondant
        for j in range(10):
            if (table[i][j])=='X':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Wall)
            elif table[i][j] == "C":
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Caisse)
            elif (table[i][j])=='R':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = robot[index_robot])
            elif (table[i][j])=='P':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Flag)
            elif (table[i][j])=='S':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Yellow_Coin)
            elif (table[i][j])=='B':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Red_Coin)
            elif table[i][j] == "E":
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = End)
    root_tete.update()

    if Print_Score == True: #on peut appeler la fonction update sans actualiser le score
        show_score["text"] = "Score: %s" %str(int(sum(score))) #actualisation du score

def end_game(): #fonction appelée quand la partie se termine
    global question, box_placed, score_temp
    score_temp = (10000/(box_placed*10 + time_game*0.2) + score_star) * level #calcul du score
    show_score["text"] = "Score: %s"%str(int(sum(score + [score_temp]))) #on actualise l'affichage
    Button_restart["state"] = "disabled" #désactivation du bouton restart
    update(False)

    question = Toplevel()
    question.geometry("300x125")
    question.protocol("WM_DELETE_WINDOW", exit_menu) #on demande les actions a faire
    Button(question, text = "Restart", command = restart_question,cursor ='hand2', font = ("Helvetica", 10)).place(x = 30, y = 45)
    Button(question, text = "Main Menu", command = exit_menu,cursor ='hand2', font = ("Helvetica", 10)).place(x = 210, y = 45)
    Button(question, text = "Next Level", command = next,cursor ='hand2', font = ("Helvetica", 10)).place(x = 110, y = 45)

def restart_question(): # fonction executée si le joueur veut recommencer le niveau
    global question2, question
    question.destroy()
    question2 = askquestion("RESTART", "Est-tu-sur de recommencer ? Tu perdras à chaque fois 50 points multiplié par le niveau où tu es")
    if question2 == "yes": #si l'utilisateur veut recommencer, on regenère l'affichage
        restart()
    else: #sinon on redemande l'action a executer
        end_game()

box_placed = 0 #nombre de box que l'utilisateur a posé sur la map
time_game = 0 #temps pris par le joueur pour résoudre l'agnime

def time_num(): #fonciton pour incrémenter le temps
    global time_game
    time_game+=1 # incrémentation de la variable
    show_time['text'] = "Temps: %s" %str(time_game) #actualisation de l'affichage
    root_tete.after(1000,time_num) #rappel de la fonction après 1 seconde (1000 ms)

def next(): #fonction pour passer au niveau suivant
    global level, score
    score[-1] += score_temp     # on atribue au dernier niveau joué le score gardé en mémoire
    score.append(50*(level+1))  # création d'un nouveau slot dans la liste des scores pour le nouveau niveau initié avec une valeur car il y a un malus appliqué dans la foction restart
    question.destroy()
    level += 1                  # incrémentation du niveau
    if level == len(Levels)+1:  # si le joueur a atteint la fin de la liste des niveaux
        score[-1] = 0           # le dernier score ne doit pas avoir d'offset
        exit()                  # on quitte le jeu en arretant la fonction
        return
    Title_level["text"] = "Level {}".format(level) #actualisation de l'affichage
    restart()                   # régénération de l'affichage

def start(): #fonction pour faire bouger le robot
    global table, index_robot, score_star, run
    Table.unbind("<Button-1>")          # on désactive le clique et le bouton start
    Button_start["state"] = "disabled"
    dir = [1, 0]                        # matrice de mouvement, par défaut, on va a droite
    for i in range(nbcases_width):
        for j in range(nbcases_height): # on récupère la position du robot en parcourant la liste
            if table[i][j] == "R":
                pos = [i, j]
                break
    reminder = {} # pour vérifier le nombre de fois qu'on est passé a un meme endroit
    run = True    # variable vraie tant qu'on execute la boucle
    while run == True:
        sleep(0.5) #on fait avancer le robot toutes les 0.5 secondes
        table[pos[0]][pos[1]] = "0" # on remplace la case où il était par une case vide
        x = pos[0] + dir[0] #calcul de la prochaine position
        y = pos[1] - dir[1]
        if nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "0": #si la prochaine position est dans le tableau et que la prochaine case est libre
            pos = [x, y] #on lui assigne la nouvelle position
            try:
                reminder[(pos[0], pos[1])] += 1     # on essaye d'ajouter 1 à la position actuelle
                if reminder[(pos[0], pos[1])] > 4:  # si on est passé plus de 4 fois au meme endroit, on restart
                    run = False
                    restart()
                    return
            except:
                reminder[(pos[0], pos[1])] = 1 #si impossible de ajouter 1 c'est que la clef n'est pas crée, on l'initialise a 1

        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "S": #si la prochaine case est une petite pièce
            pos = [x, y]        # on lui atribue la nouvelle position
            score_star += 50    # ajout du bonnus
            table[x][y] = "0"   # et on vide la case

        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "B": #même chose si la prochaine case est une grosse pièce
            pos = [x, y]
            score_star += 150
            table[x][y] = "0"


        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "P": #si la prochaine case est le drapeau
            table[x][y] = "E" #on change la case actuelle à réussi pour afficher avec le drapeau
            run = False #on arrete la boucle
            end_game()  #fin du jeu
            return      # fin de la fonction

        else:                                   # sinon, on a un obstacle devant le robot
            dir = [dir[1], -dir[0]]             # rotation d'une matrice [a, b] par -PI/2 en faisant [b, -a]
            index_robot = (index_robot + 1)%4   # affichage de la rotation
        table[pos[0]][pos[1]] = "R"             # on place la robot dans la grille à sa position actuelle
        update()

def restart_button(): #si on clique sur le bouton pour restart
    global run, score_star
    run = False #on arrete la boucle
    restart()   #restart de l'application

def restart(): #fonction appelée pour redémarer la partie
    global table, timer_start, time_game, box_placed, index_robot, score_star, score
    Button_restart["state"] = "normal" #on réactive le bouton restart
    index_robot = 0 #on repositionne le robot à droite
    score[-1] -= 50*level #pénalité
    Button_start["state"] = "normal" #réactivation du bouton start
    time_game = box_placed = score_star = 0 #on réinitaialise des variables de jeu
    Table.bind("<Button-1>", click) #rebind du clique droit
    show_time['text'] = "Temps: %s" %str(time_game) #actualisation des affichages
    show_count['text'] = "Nombre de palettes: %s" %str(box_placed)

    for i in range(nbcases_width):
        for j in range(nbcases_height):
            table[i][j] = Levels[level-1][(j*nbcases_width)+i] #réinitialisation de la table
    update()

def exit_menu(): #fonction pour quiter le jeu à partir des questions
    global  score
    score[-1] += score_temp # on lui attribue le score gardé en mémoire
    exit()                  # et on quitte l'application

def exit(): #fonction pour quitter, elle se charge de détruire les fenètres lancées
    try:
        question.destroy()
    except: pass
    root_tete.quit()
    root_tete.destroy()

def Tete(user): #fonction principale
    global root_tete, robot, index_robot, Flag, End, Frame_top, Frame_right, Frame_left, Frame_down, Table, Frame1, Caisse, Wall, Red_Coin, Yellow_Coin, show_score
    global Frame2, Title_level, show_time, show_count, nbcases_width, nbcases_height, cell_width, cell_height, table, level, score, score_star, Button_start
    global User_name, Button_restart
    #preparation du jeu
    User_name = user #nom d'utilisateur
    rules_game() #on execute les rêgles du jeu et le scoreboard


    root_tete = Toplevel() #fenetre principale
    root_tete.geometry('700x550')
    root_tete.protocol("WM_DELETE_WINDOW",exit)
    #############------------variables----------########################
    score = [50] #initialisation de la liste des scores
    index_robot = 0 #la ou le robot regarde
    nbcases_width = nbcases_height = 10 #dimensions
    cell_width = 500/nbcases_width #dimensions des cellules
    cell_height = 500/nbcases_height
    score_star = 0                  #bonnus des pièces

    table = [[0 for i in range(nbcases_width)] for j in range(nbcases_height)]#tableau
    level = 1 #niveau

    ########---------Import Photos------------------###############################################
    robot = [PhotoImage(file = "Tete_chercheuse/image/robot_right.png"), PhotoImage(file = "Tete_chercheuse/image/robot_front.png"), PhotoImage(file = "Tete_chercheuse/image/robot_left.png"), PhotoImage(file = "Tete_chercheuse/image/robot_back.png")]
    restart_button_image = PhotoImage(file = "Tete_chercheuse/image/start.png")
    Flag = PhotoImage(file = "Tete_chercheuse/image/flag.png")
    End = PhotoImage(file = "Tete_chercheuse/image/robot_flag.png")
    Caisse = PhotoImage(file = "Tete_chercheuse/image/caisse.png")
    Wall = PhotoImage(file = "Tete_chercheuse/image/mur.ppm")
    Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
    Yellow_Coin = PhotoImage(file = "Tete_chercheuse/image/yellow_coin.ppm")
    Red_Coin = PhotoImage(file = "Tete_chercheuse/image/red_coin.ppm")
    Guide_tete = PhotoImage(file = "Tete_chercheuse/image/brain.png")
    Bulle_image = PhotoImage(file = "Tete_chercheuse/image/bulle.png")


    ########------------Frames Pricipaux-------------########################################
    Frame_top = Frame(root_tete, width = 700, height = 50, bg = 'lightgrey')
    Frame_right = Frame(root_tete, width = 500, height = 500)
    Frame_left = Frame(root_tete, width = 200, height = 500, bg = 'red')

    ########-----------Frames Secondaires-----------######################################
    Frame1 = Frame(Frame_left, width = 200, height =200, bg = 'gold')
    Frame2 = Frame(Frame_left, width = 200, height =300, bg = 'black')

    Title_level = Label(Frame_top, text = "Level 1", font=("Helvetica", 20), relief = GROOVE)
    Table = Canvas(Frame_right,width = 500, height = 500, bg ='white')

    Canvas_dessine = Canvas(Frame2, bg = 'white',width = 186, height =290)

    #######-----------Package des Frames-------------##################################
    Frame_top.pack(side = TOP)
    Frame_right.pack(side = RIGHT)
    Frame_left.pack(side = LEFT)

    Frame1.pack(side = TOP)
    Frame2.pack(side = BOTTOM)
    Canvas_dessine.place(x = 3, y =4)

    Table.pack(fill = BOTH)
    Title_level.place(x = 315, y = 5)

    #########------------Labels et autres-----------##################################

    Button_start = Button(Frame1,relief = GROOVE,activebackground = 'black' ,bg = 'black', cursor ='hand2', image = restart_button_image,command = start)
    Button_start.place(x = 20, y = 27)

    Button_quit = Button(Frame_top, text = 'Quit' ,relief = GROOVE , cursor ='hand2',command = exit_menu)
    Button_quit.place(x = 570, y = 19)

    Button_restart = Button(Frame_top, text = "RESTART", relief = GROOVE,cursor ='hand2', font = ("Helvetica", 10),command = restart_button)
    Button_restart.place(x = 600, y = 19)

    show_time = Label(Frame1, text = "Time: %s" %str(0), font = ("Helvetica", 10), relief =GROOVE)
    show_time.place(x = 110, y = 170)

    show_score = Label(Frame1, text = "Score: %s" %str(sum(score)), font = ("Helvetica", 10), relief = GROOVE)
    show_score.place(x = 25, y = 170)

    show_count = Label(Frame1, text = "Nombre de palettes: %s" %str(0), font = ("Helvetica", 10), relief = GROOVE)
    show_count.place(x = 31, y = 130)

    Canvas_dessine.create_image(86,215 ,image = Guide_tete)
    Canvas_dessine.create_image(100,68, image= Bulle_image)

    show_conseils = Label(Canvas_dessine, text = "Conseil: Je te propose \n d'être sûr de ton trajet \n avant de commencer",bg = 'white', font = ("Helvetica", 9))
    show_conseils.place(x = 32, y =38 )

    ###############-----------Lancement des fonctions-------------######################
    time_num()
    restart()
    update()

    ################################################################################

    root_tete.mainloop()

    return sum(score) #retour du score total du joueur sur tout les niveaux joués
