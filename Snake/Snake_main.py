from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import randint

class snake:
    def __init__(self, user):
        self.User_name = user
        #rules

        #Scoreboard(Frame, root, "Snake", user)

        self.start()
        return self.score

    def start(self):
        self.grid = [[0 for i in range(20)] for j in range(20)]
        self.length_max = 2
        self.grid[9][10] = 1
        self.grid[10][10] = 2

        self.root = Toplevel()
        self.root.geometry("702x552")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.grille = Canvas(self.root, width = 500, height = 500, bg = "white")
        self.grille.place(x = 200, y = 50)

        self.sweet()
        self.update()
        self.root.mainloop()

    def update(self):
        self.Fruit_Image = PhotoImage(file = "Snake/images/Fruit.png")
        self.grille.delete("all")

        for i in range(0, 500, 25):
            self.grille.create_line(i, 0, i, 500)
        for i in range(0, 500, 25):
            self.grille.create_line(0, i, 500, i)


        for i in range(20):
            for j in range(20):
                if self.grid[i][j] == 0:
                    self.grille.create_rectangle(i*25, j*25, (i+1)*25, (j+1)*25, fill = 'lightgrey' )

                elif self.grid[i][j] == 1:
                    self.grille.create_oval(i*25, j*25, (i+1)*25, (j+1)*25, fill = 'red')

                elif self.grid[i][j] == self.length_max:
                    self.grille.create_oval(i*25, j*25, (i+1)*25, (j+1)*25, fill = 'yellow')


        self.grille.create_rectangle(2,2,500,500)

        self.grille.create_image(self.fruit[0]*25 + 13, self.fruit[1]*25 + 13, image = self.Fruit_Image)

    def sweet(self):
        verite = True
        while verite:
            x = randint(0, 20)
            y = randint(0, 20)

            if self.grid[x][y] == 0:
                verite = False
                self.fruit = (x, y)
            #pick a random cords
            #while cords isn't a snake part

    def verif(self, x, y):
        score = 0
        if self.grid[x][y] != 0:
            #self.dead()
            pass
        elif x == self.fruit[0] and y == self.fruit[1]:
            score += 1
            self.sweet()
            pass



    def exit(self):
        self.root.destroy()
        self.root.quit()

def Snake(User):
    global jeux
    jeux = snake(User)

if __name__ == "__main__":
    Snake("Test_Purpose")
