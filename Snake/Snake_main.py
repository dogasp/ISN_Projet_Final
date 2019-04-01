from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import randint

"""--------------------------------Directions-------------------------"""
#0 = droite
#1 = bas
#2 = gauche
#3 = haut

class snake:
    def __init__(self, user):
        self.User_name = user
        #rules
        #Scoreboard(Frame, root, "Snake", user)

        self.start()
        return self.length_max * 40

    def start(self):
        global test
        self.grid = [[(0, 0) for i in range(20)] for j in range(20)] #pour chaque élément de la grille, on a le temps de vie et la direction de la partie du serpent
        self.length_max = 2
        self.fruit = [-1, -1]
        self.dir = [1, 0]
        self.pos = [10, 10]
        self.grid[10][10] = [2, 0]

        self.root = Toplevel()
        self.root.geometry("702x552")
        self.root.bind("<Key>", self.rotate)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()

        test = PhotoImage(file = "Snake/images/Head_Right.png")

        self.Fruit_Image = PhotoImage(file = "Snake/images/Fruit.png")
        self.Head_Image = [PhotoImage(file = "Snake/images/Head_Right.png"),PhotoImage(file = "Snake/images/Head_Down.png"), PhotoImage(file = "Snake/images/Head_Left.png"), PhotoImage(file = "Snake/images/Head_Up.png")]
        self.Body_Image = [PhotoImage(file = "Snake/images/Horizontal.png"), PhotoImage(file = "Snake/images/Vertical.png"), PhotoImage(file = "Snake/images/Horizontal.png"), PhotoImage(file = "Snake/images/Vertical.png")]
        self.Queue_Image = [PhotoImage(file = "Snake/images/Queue_Right.png"), PhotoImage(file = "Snake/images/Queue_Down.png"), PhotoImage(file = "Snake/images/Queue_Left.png"), PhotoImage(file = "Snake/images/Queue_Up.png")]

        self.grille = Canvas(self.root, width = 500, height = 500, bg = "#1a1a1a")
        self.grille.place(x = 200, y = 50)

        self.sweet()
        self.update()
        self.root.mainloop()

    def update(self):
        newX = self.pos[0] + self.dir[0]
        newY = self.pos[1] + self.dir[1]

        if self.verif(newX, newY) == True:
            self.pos = [newX, newY]
            for i in range(20):
                for j in range(20):
                    if self.grid[i][j][0] != 0:
                        self.grid[i][j][0] -= 1

            self.grid[newX][newY] = [self.length_max, convert_dir(self.dir, True)]

        self.grille.delete("all")

        for i in range(20):
            for j in range(20):
                if self.grid[i][j][0] == 0:
                    self.grille.create_rectangle(i*25, j*25, (i+1)*25, (j+1)*25, outline ='#1a1a1a',fill = '#1a1a1a' )

                elif self.grid[i][j][0] == 1:
                    #self.grille.create_image(i*25, j*25, (i+1)*25, (j+1)*25, image = self.Queue_Image[self.grid[i][j][1]])
                    self.grille.create_oval(i*25, j*25, (i+1)*25, (j+1)*25, fill = "yellow")

                elif self.grid[i][j][0] == self.length_max:
                    self.grille.create_image(i*25, j*25, (i+1)*25, (j+1)*25, image = test) #self.Head_Image[self.grid[i][j][1]]) unknown option 300 or unknown option 275
                    self.grille.create_oval(i*25, j*25, (i+1)*25, (j+1)*25, fill = "green")
                else:
                    self.grille.create_oval(i*25, j*25, (i+1)*25, (j+1)*25, fill = "blue")


        self.grille.create_rectangle(2,2,500,500)

        self.grille.create_image(self.fruit[0]*25 + 13, self.fruit[1]*25 + 13, image = self.Fruit_Image)

        self.root.after(300, self.update)

    def rotate(self, event = None):
        symb = event.keysym
        dir = -1
        if symb == "Right":
            dir = 0
        elif symb == "Down":
            dir = 1
        elif symb == "Left":
            dir = 2
        elif symb == "Up":
            dir = 3
        if dir != -1:
            self.dir = convert_dir(dir)

    def sweet(self):
        verite = True
        while verite:
            x = randint(0, 19)
            y = randint(0, 19)
            if self.grid[x][y][0] == 0 and x != self.fruit[0] and y != self.fruit[1]:
                verite = False
                self.fruit = (x, y)
            #pick a random cords
            #while cords isn't a snake part

    def verif(self, x, y):
        if x < 0 or x > 19 or y < 0 or y > 19 or self.grid[x][y][0] != 0:
            #self.dead()
            return False
        elif x == self.fruit[0] and y == self.fruit[1]:
            for i in range(20):
                for j in range(20):
                    if self.grid[i][j][0] != 0:
                        self.grid[i][j][0] += 1
            self.length_max += 1
            self.sweet()
        return True

    def exit(self):
        self.root.destroy()
        self.root.quit()

def convert_dir(dir, mat = False): #dir correspond à l'entrée et mat, si c'est une matrice qui est entrée
    if mat == True:
        if dir == [1, 0]:
            return 0
        elif dir == [0, 1]:
            return 1
        elif dir == [-1, 0]:
            return 2
        elif dir == [0, -1]:
            return 3
    else:
        if dir == 0:
            return [1, 0]
        elif dir == 1:
            return [0, 1]
        elif dir == 2:
            return [-1, 0]
        elif dir == 3:
            return [0, -1]

def Snake(User):
    jeux = snake(User)

if __name__ == "__main__":
    Snake("Test_Purpose")
