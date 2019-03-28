from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from Tete_chercheuse.data import *
from time import sleep

##################----------Variables------------######################################
#'0' correpond à une case vide
#'X' correspond à une case pleine (mur)
#'R' correpond à la case associée au robot
#'P' correpond à la case associée à l'arrivée (drapeau)
#'C' correpond aux palettes, où l'on ajoute un obstacle
#'S' correspond à une (petite) pièce/récompense
#'B' correspond à une (grosse) pièce/récompense
#'E' correspond au robot arrivé
#
########################################################################################

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

def update():
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

                #Table.create_rectangle((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = "lightgrey")
                #Table.create_line((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = 'red')
                #Table.create_line((cell_width)*i,(cell_height)*j,(cell_width)*(i+1),(cell_height)*(j+1), fill = 'red')

            elif (table[i][j])=='R':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = robot[index_robot])

            elif (table[i][j])=='P':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Flag)

            elif (table[i][j])=='S':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Yellow_Coin)
                #Table.create_line((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = 'yellow')

            elif (table[i][j])=='B':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Red_Coin)
                #Table.create_line((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = 'red')
            elif table[i][j] == "E":
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = End)
    root_tete.update()


def end_game():
    global question, box_placed, score
    update()

    score.append((10000/(box_placed*10 + time_game*0.2) + score_star) * level)

    question = Toplevel()
    question.geometry("300x125")
    Button(question, text = "Restart", command = restart_menu).place()
    Button(question, text = "Main Menu", command = exit).pack()
    Button(question, text = "Next Level", command = next).pack()

def restart_menu():
    global score
    score[-1] = 0
    question.destroy()
    restart()

box_placed = 0
time_game = 0

def time_num():
    global time_game
    time_game+=1
    show_time['text'] = "Time: %s" %str(time_game)
    root_tete.after(1000,time_num)

def next():
    global level
    question.destroy()
    level += 1
    Title_level["text"] = f"Level {level}"
    restart()

def start():
    global table, index_robot, Start_game, score_star
    Table.unbind("<Button-1>")
    dir = [1, 0] #matrice de mouvement
    for i in range(nbcases_width):
        for j in range(nbcases_height):
            if table[i][j] == "R":
                pos = [i, j]
                break
    reminder = {} #pour vérifier le nombre de fois qu'on est passé a un meme endroit
    run = True
    while run == True:
        sleep(0.5)
        table[pos[0]][pos[1]] = "0"
        x = pos[0] + dir[0]
        y = pos[1] - dir[1]
        if nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "0":
            pos = [x, y]
            try:
                reminder[(pos[0], pos[1])] += 1
                if reminder[(pos[0], pos[1])] > 4: #si on est passé plus de 4 fois au meme endroit, on restart
                    run = False
                    Start_game = False
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
            Start_game = False
            return
        else:
            dir = [dir[1], -dir[0]]
            index_robot = (index_robot + 1)%4
        table[pos[0]][pos[1]] = "R"
        update()

def restart():
    global table, timer_start, time_game, Start_game, box_placed, index_robot, score_star
    Start_game = True
    index_robot = 0
    time_game = box_placed = score_star = 0
    Table.bind("<Button-1>", click)
    show_time['text'] = "Time: %s" %str(time_game)
    show_count['text'] = "Nombre de palettes: %s" %str(box_placed)

    for i in range(nbcases_width):
        for j in range(nbcases_height):
            table[i][j] = Levels[level-1][(j*nbcases_width)+i]

    update()

def exit():
    try:
        question.destroy()
    except: pass
    root_tete.quit()
    root_tete.destroy()

def Tete():
    global root_tete, robot, index_robot, Flag, End, Frame_top, Frame_right, Frame_left, Frame_down, Table, Frame1, Caisse, Wall, Red_Coin, Yellow_Coin
    global Frame2, Title_level, show_time, show_count, nbcases_width, nbcases_height, rayon, cell_width, cell_height, table, level, score, score_star
    #preparation du jeu

    score = [0]
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

    Button_start = Button(Frame1, text = "START" ,relief = GROOVE, font = 40,pady = 10, padx = 10,command = start)
    Button_start.place(x = 57, y = 50)
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
    """
    enlever des points quand on perd la partie
    si l'on veut restart, on prévient qu on va lui enlever des points et remettre son score de la partie en cours à 0
    petite piece = 5
    grosse piece = 10

    """

    return sum(score)
