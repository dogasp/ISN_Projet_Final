from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from Tete_chercheuse.data import *
from time import sleep, time

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
                Table.create_rectangle((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = "black")

            elif table[i][j] == "C":
                Table.create_rectangle((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = "lightgrey")
                Table.create_line((cell_width)*(i+1),(cell_height)*j,(cell_width)*i,(cell_height)*(j+1), fill = 'red')
                Table.create_line((cell_width)*i,(cell_height)*j,(cell_width)*(i+1),(cell_height)*(j+1), fill = 'red')

            elif (table[i][j])=='R':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = robot[index_robot])

            elif (table[i][j])=='P':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Flag)

            elif table[i][j] == "E":
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = End)
    root_tete.update()


def end_game():
    global question, box_placed, score
    update()
    timer = time() - timer_start


    for i in range(nbcases_width):
        for j in range(nbcases_height):
            if table[i][j] == "C":
                box_placed += 1
    score = 1000/(box_placed*10 + timer*0.5) * level
    print(score)

    question = Toplevel()
    Button(question, text = "Restart", command = restart_menu).pack()
    Button(question, text = "Main Menu", command = lambda: print("WIP")).pack()
    Button(question, text = "Next Level", command = next).pack()

def restart_menu():
    question.destroy()
    restart()

box_placed = 0
Start_game = True
time_game = 0

def time_num():
    if Start_game == True:
        global time_game
        if time_game != 1000:
            time_game+=1
            show_time['text'] = "Time: %s" %str(time_game)
            root_tete.after(1000,time_num)
        else: pass

def next():
    global level
    question.destroy()
    level += 1
    Title_level["text"] = f"Level {level}"
    restart()

def start():
    global table, index_robot, Start_game
    Table.unbind("<Button-1>")
    dir = [1, 0] #matrice de mouvement
    for i in range(nbcases_width):
        for j in range(nbcases_height):
            if table[i][j] == "R":
                pos = [i, j]
                break
    reminder = {}
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
                if reminder[(pos[0], pos[1])] > 4:
                    restart()
                    return
            except:
                reminder[(pos[0], pos[1])] = 1
        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "P":
            table[x][y] = "E"
            end_game()
            Start_game = False
            return
        else:
            dir = [dir[1], -dir[0]]
            index_robot = (index_robot + 1)%4
        table[pos[0]][pos[1]] = "R"
        update()

def restart():
    global table, timer_start, time_game, Start_game, box_placed, index_robot
    Start_game = True
    index_robot = 0
    time_game = box_placed = 0
    Table.bind("<Button-1>", click)
    show_time['text'] = "Time: %s" %str(time_game)
    show_count['text'] = "Nombre de palettes: %s" %str(box_placed)

    for i in range(nbcases_width):
        for j in range(nbcases_height):
            table[i][j] = Levels[level-1][(j*nbcases_width)+i]

    time_num()
    update()
    timer_start = time()

def exit():
    root_tete.quit()
    root_tete.destroy()

def tete_start():
    global root_tete, robot, index_robot, Flag, End, Frame_top, Frame_right, Frame_left, Frame_down, Table, Frame1, Frame2, Title_level, show_time, show_count, nbcases_width, nbcases_height, rayon, cell_width, cell_height, table, level
    #preparation du jeu
    root_tete = Toplevel()

    root_tete.geometry('700x550')
    root_tete.overrideredirect(1)

    ########---------Import Photos------------------###############################################
    robot = [PhotoImage(file = "Tete_chercheuse/robot_right.png"), PhotoImage(file = "Tete_chercheuse/robot_front.png"), PhotoImage(file = "Tete_chercheuse/robot_left.png"), PhotoImage(file = "Tete_chercheuse/robot_back.png")]
    index_robot = 0
    Flag = PhotoImage(file = "Tete_chercheuse/flag.png")
    End = PhotoImage(file = "Tete_chercheuse/robot_flag.png")

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

    Button_quit = Button(Frame_top, text = "quit", command = exit)
    Button_quit.place(x = 650, y = 10)

    nbcases_width = nbcases_height = 10
    rayon = 7

    cell_width = 500/nbcases_width
    cell_height = 500/nbcases_height



    #################################################################################
    #generation du terrain

    table = [[0 for i in range(nbcases_width)] for j in range(nbcases_height)]
    level = 1

    restart()
    update()

    ################################################################################

    root_tete.mainloop()

    try:
        return score
    except:
        return -1
