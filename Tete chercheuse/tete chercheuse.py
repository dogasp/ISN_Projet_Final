from tkinter import *
from data import *

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
                Table.create_rectangle((cell_width)*(i+1),(cell_height)*(j),(cell_width)*i,(cell_height)*(j+1), fill = "black")
            elif table[i][j] == "C":
                Table.create_rectangle((cell_width)*(i+1),(cell_height)*(j),(cell_width)*i,(cell_height)*(j+1), fill = "lightgrey")
                Table.create_line((cell_width)*(i+1),(cell_height)*(j),(cell_width)*i,(cell_height)*(j+1), fill = 'red')
                Table.create_line((cell_width)*i,(cell_height)*(j),(cell_width)*(i+1),(cell_height)*(j+1), fill = 'red')
            elif (table[i][j])=='R':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = robot_right)
            elif (table[i][j])=='P':
                Table.create_image(cell_width* i + cell_width/2, cell_height* j + cell_height/2, image = Flag)

def start():
    Table.unbind("<Button 1>")


#préparation du jeu
root = Tk()

root.geometry('700x550')

#######################################################
robot_right = PhotoImage(file = "Tete chercheuse/robot_right.png")
Flag = PhotoImage(file = "Tete chercheuse/flag.png")

########------------Frames Pricipaux-------------########################################
Frame_top = Frame(root, width = 700, height = 50, bg = 'pink')
Frame_right = Frame(root, width = 500, height = 500)
Frame_left = Frame(root, width = 200, height = 500, bg = 'red')
Table = Canvas(Frame_right, width = 500, height = 500)

########-----------Frames Secondaires-----------######################################
Frame1 = Frame(Frame_left)
Frame2 = Frame(Frame_left)

Title_level = Label(Frame_top, text = "Level 1", font=("Helvetica", 20), relief = GROOVE)
Table = Canvas(Frame_right,width = 500, height = 500, bg ='white')

#######-----------Package des Frames-------------##################################
Frame_top.pack(side = TOP)
Frame_right.pack(side = RIGHT)
Frame_left.pack(side = LEFT)

Frame1.pack(side = TOP)
Frame2.pack(side = BOTTOM)

Table.pack(fill = BOTH)
#Title_level.place(x = 315, y = 10)






Table.bind("<Button-1>", click)

nbcases_width = 10
nbcases_height = 10
rayon = 7

cell_width = 500/nbcases_width
cell_height = 500/nbcases_height



#################################################################################
#génération du terrain

table = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        table[i][j] = niveau3[(j*10)+i]

update()
print(table)



################################################################################

root.mainloop()
