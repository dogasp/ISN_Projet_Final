from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import randint
from Fantome.Ressources.data.map_ghost import*


class ghost:
    def __init__(self, user):
        self.User_name = user
        self.show_rules = Toplevel()
        self.show_rules.title('Règles')
        self.show_rules.geometry('700x500')
        """self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking)

        self.Frame_main1_wind2 = Canvas(self.show_rules, bg = 'red', relief = GROOVE)
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 530)
        #self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
        #self.Frame_main1_wind2.create_image(335,265,image =Fond_Frame_main1_wind2)
        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
        self.Frame_main2_wind2.place(x = 60, y = 45)
        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)

        #Labels à mettre pour les règles

        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", command = self.quit_rules)
        self.Button_Skip.place(x = 50, y = 300)"""
        self.start()
        self.show_rules.mainloop()



    def start(self):
        self.level = 1
        self.nbcases = (8, 6, 10)
        self.length = 500/self.nbcases[self.level - 1]
        self.grid = [[(0) for i in range(self.nbcases[self.level - 1])] for j in range((self.nbcases[self.level - 1]))]
        print(self.grid)
        self.root = Tk()
        self.root.geometry("702x552")
        #self.root.bind("<Key>", self.rotate)
        #self.root.protocol("WM_DELETE_WINDOW", self.exit)

        ########------------Frames Pricipaux-------------########################################
        self.Frame_top = Frame(self.root, width = 700, height = 50, bg = 'lightgrey')
        self.Frame_right = Frame(self.root, width = 500, height = 500)
        self.Frame_left = Frame(self.root, width = 200, height = 500, bg = 'red')


        #######-----------Package des Frames-------------####################################
        self.Frame_top.pack(side = TOP)
        self.Frame_right.pack(side = RIGHT)
        self.Frame_left.pack(side = LEFT)

        ######-----------Elements du jeu-----------------##########################################

        self.grille = Canvas(self.Frame_right, width = 500, height = 500, bg = "#1a1a1a")
        self.grille.pack(fill = BOTH)

        for i in range(self.nbcases[self.level - 1]):
            self.grille.create_line((self.length)*i,0,(self.length)*i,500)
        for j in range(self.nbcases[self.level - 1]):
            self.grille.create_line(0,(self.length)*j,500,(self.length)*j)

        for i in range(self.nbcases[self.level - 1]):
            for j in range(self.nbcases[self.level - 1]):
                #self.grid[i][j] = level_map[self.level - 1][(j*self.nbcases[self.level - 1])+i]
                print(level_map[self.level - 1][(j*self.nbcases[self.level - 1])+i])
                if self.grid[i][j] == 'X':
                    self.grille.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'red')
                elif self.grid[i][j] == 'R':
                    self.grille.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'yellow')
                elif self.grid[i][j] == 'F':
                    self.grille.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'green')
                elif self.grid[i][j] == 'D':
                    self.grille.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'brown')


    def update(self):
        pass


def Ghost(User):
  jeux = ghost(User)
  return jeux.Best_Score
