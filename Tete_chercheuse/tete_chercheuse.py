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
########################################################################################

def rules_game():
    global show_rules, Frame_main2_wind2, Frame_main1_wind2
    show_rules = Toplevel()

    show_rules.title('Règles')
    show_rules.geometry('670x530')
    show_rules.protocol("WM_DELETE_WINDOW", quit_ranking)

################-----------Création des Frames de la fenetre secondaire----------##############
    Frame_main1_wind2 = Canvas(show_rules, bg = 'red', relief = GROOVE)
    Frame_main1_wind2.pack(ipadx = 670, ipady = 530)

    Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
    Frame_main1_wind2.create_image(335,265,image =Fond_Frame_main1_wind2)

    Frame_main2_wind2 = Frame(Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
    Frame_main2_wind2.place(x = 60, y = 45)
###############---------Création des regles avec animations--------------####################

    Rules = Label(Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
    Rules.place(x = 200, y =5)

#------------------1----------------------------------------------------------------
    Rules2 = Label(Frame_main2_wind2, text = "Le but est que le robot arrive au drapeau.\n\
     ", font = ("Berlin Sans FB", 12))
    Frame_main2_wind2.after(500, lambda: Rules2.place(x = 45, y = 70))

    CANVAS1 = Canvas(Frame_main2_wind2, width = 150, height = 60)
    Frame_main2_wind2.after(1000, lambda: CANVAS1.place(x = 380, y = 60 ))
    first_photo1 = PhotoImage(file = "Rules_tete_photo/first_photo.png")
    CANVAS1.create_image(75, 30,image = first_photo1)

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
    Bouton_skip = Button(Frame_main2_wind2, text = '-Skip-',font = ("Helvetica", 10), relief = GROOVE,command = quit_rules)
    Bouton_skip.place(x = 200, y = 390)

    show_rules.mainloop()

def quit_ranking():
    show_rules.destroy()
    show_rules.quit()

def quit_rules():
    Frame_main2_wind2.destroy()
    score = Scoreboard(Frame_main1_wind2, show_rules, "Tete", User_name)


"""######################------------------Début du Jeu---------------------------########################################"""

def click(event):
    global box_placed
    x = event.x
    y = event.y

    i = int(x//cell_width)
    j = int(y//cell_height)

    if table[i][j] == "0":
        table[i][j] = "C"
        box_placed+=1
        show_count['text'] = "Nombre de palettes: %s" %str(box_placed)
    elif table[i][j] == "C":
        table[i][j] = "0"
        box_placed-=1
        show_count['text'] = "Nombre de palettes: %s" %str(box_placed)
    update()

def update(Print_Score = True):
    Table.delete("all")
    for i in range(nbcases_width):
        Table.create_line((cell_width)*i,0,(cell_width)*i,500)

    for j in range(nbcases_height):
        Table.create_line(0,(cell_width)*j,500,(cell_width)*j)

    Table.create_rectangle(2,2,500,500)
    for i in range(10):
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

    if Print_Score == True:
        show_score["text"] = "Score: %s" %str(int(sum(score)))

def end_game():
    global question, box_placed
    show_score["text"] = "Score: %s"%str(int(sum(score + [(10000/(box_placed*10 + time_game*0.2) + score_star) * level])))
    update(False)

    question = Toplevel()
    question.geometry("300x125")
    Button(question, text = "Restart", command = restart_question, font = ("Helvetica", 10)).place(x = 30, y = 45)
    Button(question, text = "Main Menu", command = exit_menu, font = ("Helvetica", 10)).place(x = 210, y = 45)
    Button(question, text = "Next Level", command = next, font = ("Helvetica", 10)).place(x = 110, y = 45)

def restart_question():
    global question2, question
    question.destroy()
    question2 = askquestion("RESTART", "Est-tu-sur de recommencer ? Tu perdras 50 points à chaque fois")
    if question2 == "yes": #si l'utilisateur veut recommencer, on regenère l'affichage
        restart()
    else:
        end_game()

box_placed = 0
time_game = 0

def time_num():
    global time_game
    time_game+=1
    show_time['text'] = "Temps: %s" %str(time_game)
    root_tete.after(1000,time_num)

def next():
    global level, score
    score[-1] += ((10000/(box_placed*10 + time_game*0.2) + score_star) * level)
    score.append(50*(level+1))
    question.destroy()
    level += 1
    if level == len(Levels)+1:
        exit()
        return
    Title_level["text"] = f"Level {level}"
    restart()

def start():
    global table, index_robot, score_star, run
    Table.unbind("<Button-1>")
    Button_start["state"] = "disabled"
    dir = [1, 0] #matrice de mouvement
    for i in range(nbcases_width):
        for j in range(nbcases_height):
            if table[i][j] == "R":
                pos = [i, j]
                break
    reminder = {} #pour vérifier le nombre de fois qu'on est passé a un meme endroit
    run = True
    while run == True:
        sleep(0.1)
        table[pos[0]][pos[1]] = "0"
        x = pos[0] + dir[0]
        y = pos[1] - dir[1]
        if nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "0":
            pos = [x, y]
            try:
                reminder[(pos[0], pos[1])] += 1
                if reminder[(pos[0], pos[1])] > 4: #si on est passé plus de 4 fois au meme endroit, on restart
                    run = False
                    restart()
                    return
            except:
                reminder[(pos[0], pos[1])] = 1 #si impossible de ajouter 1 c'est que la clef n'est pas crée, on l'initialise a 1

        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "S":
            pos = [x, y]
            score_star += 50
            table[x][y] = "0"

        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "B":
            pos = [x, y]
            score_star += 150
            table[x][y] = "0"


        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "P":
            table[x][y] = "E"
            run = False
            end_game()
            return
        else:
            dir = [dir[1], -dir[0]] #rotation d'une matrice [a, b] par -PI/2 en faisant [b, -a]
            index_robot = (index_robot + 1)%4
        table[pos[0]][pos[1]] = "R"
        update()

def restart_button():
    global run, score_star
    run = False
    restart()

def restart():
    global table, timer_start, time_game, box_placed, index_robot, score_star, score
    index_robot = 0
    score[-1] -= 50*level
    Button_start["state"] = "normal"
    time_game = box_placed = score_star = 0
    Table.bind("<Button-1>", click)
    show_time['text'] = "Temps: %s" %str(time_game)
    show_count['text'] = "Nombre de palettes: %s" %str(box_placed)

    for i in range(nbcases_width):
        for j in range(nbcases_height):
            table[i][j] = Levels[level-1][(j*nbcases_width)+i]
    update()

def exit_menu():
    global  score
    score[-1] += ((10000/(box_placed*10 + time_game*0.2) + score_star) * level)
    exit()

def exit():
    try:
        question.destroy()
    except: pass
    root_tete.quit()
    root_tete.destroy()

def Tete(user):
    global root_tete, robot, index_robot, Flag, End, Frame_top, Frame_right, Frame_left, Frame_down, Table, Frame1, Caisse, Wall, Red_Coin, Yellow_Coin, show_score
    global Frame2, Title_level, show_time, show_count, nbcases_width, nbcases_height, rayon, cell_width, cell_height, table, level, score, score_star, Button_start
    global User_name
    #preparation du jeu
    User_name = user
    rules_game()

    score = [50]
    root_tete = Toplevel()

    root_tete.geometry('700x550')
    root_tete.protocol("WM_DELETE_WINDOW", exit)

    ########---------Import Photos------------------###############################################
    robot = [PhotoImage(file = "Tete_chercheuse/robot_right.png"), PhotoImage(file = "Tete_chercheuse/robot_front.png"), PhotoImage(file = "Tete_chercheuse/robot_left.png"), PhotoImage(file = "Tete_chercheuse/robot_back.png")]
    index_robot = 0
    Flag = PhotoImage(file = "Tete_chercheuse/flag.png")
    End = PhotoImage(file = "Tete_chercheuse/robot_flag.png")
    Caisse = PhotoImage(file = "Tete_chercheuse/caisse.png")
    Wall = PhotoImage(file = "Tete_chercheuse/mur.ppm")
    Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")

    Yellow_Coin = PhotoImage(file = "Tete_chercheuse/yellow_coin.ppm")
    Red_Coin = PhotoImage(file = "Tete_chercheuse/red_coin.ppm")

    ########------------Frames Pricipaux-------------########################################
    Frame_top = Frame(root_tete, width = 700, height = 50, bg = 'pink')
    Frame_right = Frame(root_tete, width = 500, height = 500)
    Frame_left = Frame(root_tete, width = 200, height = 500, bg = 'red')

    ########-----------Frames Secondaires-----------######################################
    Frame1 = Frame(Frame_left, width = 200, height =250, bg = 'green')
    Frame2 = Frame(Frame_left, width = 200, height =250, bg = 'yellow')

    Title_level = Label(Frame_top, text = "Level 1", font=("Helvetica", 20), relief = GROOVE)
    Table = Canvas(Frame_right,width = 500, height = 500, bg ='white')

    #######-----------Package des Frames-------------##################################
    Frame_top.pack(side = TOP)
    Frame_right.pack(side = RIGHT)
    Frame_left.pack(side = LEFT)

    Frame1.pack(side = TOP)
    Frame2.pack(side = BOTTOM)

    Table.pack(fill = BOTH)
    Title_level.place(x = 315, y = 10)

    #########------------Labels et autres-----------##################################

    Button_start = Button(Frame1, text = "START" ,relief = GROOVE, activeforeground = 'red',font = ("Helvetica", 20),pady = 10, padx = 10,command = start)
    Button_start.place(x = 35, y = 50)

    Button_restart = Button(Frame_top, text = "RESTART", relief = GROOVE, font = ("Helvetica", 10),command = restart_button)
    Button_restart.place(x = 600, y = 19)

    show_time = Label(Frame1, text = "Time: %s" %str(0), relief =GROOVE)
    show_time.place(x = 65, y = 180)

    show_count = Label(Frame1, text = "Nombre de palettes: %s" %str(0), relief = GROOVE)
    show_count.place(x = 65, y = 220)

    show_score = Label(Frame2, text = "Score: %s" %str(sum(score)), relief = GROOVE)
    show_score.place(x = 65, y = 100)

    nbcases_width = nbcases_height = 10
    rayon = 7

    cell_width = 500/nbcases_width
    cell_height = 500/nbcases_height

    score_star = 0

    #################################################################################
    #generation du terrain
    table = [[0 for i in range(nbcases_width)] for j in range(nbcases_height)]
    level = 1

    time_num()
    restart()
    update()

    ################################################################################

    root_tete.mainloop()

    """#si l'on veut restart, on prévient qu on va lui enlever des points"""

    return sum(score)
