from tkinter import * #@UnusedWildImport
from data import *
from time import sleep

def click(event):
    x = event.x
    y = event.y

    i = int(x//cell_width)
    j = int(y//cell_height)

    if table[i][j] == "0":
        table[i][j] = "C" 
    elif table[i][j] == "C":
        table[i][j] = "0"
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
    root.update()

def start():
    global table, index_robot
    Table.unbind("<Button-1>")
    dir = [1, 0] #matrice de mouvement
    for i in range(nbcases_width):
        for j in range(nbcases_height):
            if table[i][j] == "R":
                pos = [i, j]
                break
    run = True
    while run == True:
        sleep(0.5)
        table[pos[0]][pos[1]] = "0"
        x = pos[0] + dir[0]
        y = pos[1] - dir[1]
        if nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "0":
            pos = [x, y]
        elif nbcases_width > x >= 0 and nbcases_height > y >= 0 and table[x][y] == "P":
            print("gagne")
        else:
            dir = [dir[1], -dir[0]]
            index_robot = (index_robot + 1)%4
        table[pos[0]][pos[1]] = "R"
        update()


#preparation du jeu
root = Tk()

root.geometry('700x550')

#######################################################
robot = [PhotoImage(file = "Tete chercheuse/robot_right.png"), PhotoImage(file = "Tete chercheuse/robot_front.png"), PhotoImage(file = "Tete chercheuse/robot_left.png"), PhotoImage(file = "Tete chercheuse/robot_back.png")]
index_robot = 0
Flag = PhotoImage(file = "Tete chercheuse/flag.png")

########------------Frames Pricipaux-------------########################################
Frame_top = Frame(root, width = 700, height = 50, bg = 'pink')
Frame_right = Frame(root, width = 500, height = 500)
Frame_left = Frame(root, width = 200, height = 500, bg = 'red')
Table = Canvas(Frame_right, width = 500, height = 500)

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


Table.bind("<Button-1>", click)

nbcases_width = nbcases_height = 10
rayon = 7

cell_width = 500/nbcases_width
cell_height = 500/nbcases_height



#################################################################################
#generation du terrain

table = [[0 for i in range(nbcases_width)] for j in range(nbcases_height)]

for i in range(nbcases_width):
    for j in range(nbcases_height):
        table[i][j] = niveau3[(j*nbcases_width)+i]

update()
print(table)



################################################################################

root.mainloop()
