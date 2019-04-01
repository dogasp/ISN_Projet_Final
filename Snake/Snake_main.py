from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *

class snake:
    def __init__(self, user):
        self.User_name = user
        #rules

        #Scoreboard(Frame, root, "Snake", user)

        self.start()
        return self.score

    def start(self):
        self.grid = [[0 for i in range(20)] for j in range(20)]
        self.grid[10][10] = 2

        self.root = Tk()
        self.root.geometry("700x550")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.Plateforme = Canvas(self.root, width = 500, height = 500, bg = "white")
        self.Plateforme.place(x = 200, y = 50)
        self.update()
        self.root.mainloop()

    def update(self):
        self.Plateforme.delete("all")
        self.Plateforme.create_line(2, 0, 2, 500)
        self.Plateforme.create_line(0, 2, 500, 2)

        for i in range(0, 500, 25):
            self.Plateforme.create_line(i, 0, i, 500)
        for i in range(0, 500, 25):
            self.Plateforme.create_line(0, i, 500, i)

        for i in range(20):
            for j in range(20):
                

    def exit(self):
        self.root.destroy()
        self.root.quit()

def Snake(User):
    jeux = snake(User)

if __name__ == "__main__":
    Snake("Test_Purpose")
