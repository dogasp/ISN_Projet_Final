from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import randint
from Fantome.Ressources.data.map_ghost import*
from math import*


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


        self.fantome = []


        self.grid = [[(0) for i in range(self.nbcases[self.level - 1])] for j in range((self.nbcases[self.level - 1]))]
        self.root = Toplevel()
        self.root.geometry("702x552")
        self.root.bind("<Key>", self.move_Jerry)
        #self.root.protocol("WM_DELETE_WINDOW", self.exit)

        #########-----------Import des photos-------------#################################
        self.Jerry_image = PhotoImage(file = "Fantome/Ressources/Images/Jerry.png")
        self.Tom_image_left = PhotoImage(file = "Fantome/Ressources/Images/Tom_left.png")
        self.Tom_image_right = PhotoImage(file = "Fantome/Ressources/Images/Tom_right.png")
        ########------------Frames Pricipaux-------------########################################
        self.Frame_top = Frame(self.root, width = 700, height = 50, bg = 'lightgrey')
        self.Frame_right = Frame(self.root, width = 500, height = 500)
        self.Frame_left = Frame(self.root, width = 200, height = 500, bg = 'red')


        #######-----------Package des Frames-------------####################################
        self.Frame_top.pack(side = TOP)
        self.Frame_right.pack(side = RIGHT)
        self.Frame_left.pack(side = LEFT)

        ######-----------Elements du jeu-----------------##########################################

        self.table = Canvas(self.Frame_right, width = 500, height = 500, bg = "#1a1a1a")
        self.table.pack(fill = BOTH)

        for i in range(self.nbcases[self.level - 1]):
            self.table.create_line((self.length)*i,0,(self.length)*i,500)
        for j in range(self.nbcases[self.level - 1]):
            self.table.create_line(0,(self.length)*j,500,(self.length)*j)

        for j in range(self.nbcases[self.level - 1]):
            for i in range(self.nbcases[self.level - 1]):
                self.grid[i][j] = level_map[self.level - 1][(j*self.nbcases[self.level - 1])+i]

                if self.grid[i][j] == 'X':
                    self.table.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'red')
                elif self.grid[i][j] == 'R':
                    self.robot = self.table.create_image(self.length* i +self.length/2, self.length* j +self.length/2, image = self.Jerry_image)
                elif self.grid[i][j] == 'F':
                    Tom = self.table.create_image(self.length* i +self.length/2, self.length* j +self.length/2, image = self.Tom_image_left)
                    self.fantome.append(Tom)
                elif self.grid[i][j] == 'D':
                    self.table.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'brown')

        print(self.table.coords(self.robot))



    def move_Jerry(self, event = None):
        pos_x, pos_y = self.table.coords(self.robot)
        symb = event.keysym
        self.dir_Jerry = [0,0]
        if symb == "Right": #[1,0]
            self.dir_Jerry = [1,0]
        elif symb == "Down": #[0, 1]
            self.dir_Jerry = [0,1]
        elif symb == "Left": #[-1,0]
            self.dir_Jerry = [-1,0]
        elif symb == "Up":#[0, -1]
            self.dir_Jerry = [0, -1]

        self.newpos_x_Jerry = pos_x + self.dir_Jerry[0]*self.length
        self.newpos_y_Jerry = pos_y + self.dir_Jerry[1]*self.length
        self.new_grid_x_Jerry = int(self.newpos_x_Jerry//self.length)
        self.new_grid_y_Jerry = int(self.newpos_y_Jerry//self.length)
        if 0 <= self.newpos_x_Jerry <= 500 and 0 <= self.newpos_y_Jerry <= 500:
            if self.grid[self.new_grid_x_Jerry][self.new_grid_y_Jerry] != 'X':
                self.table.move(self.robot, self.dir_Jerry[0]*self.length, self.dir_Jerry[1]*self.length)
                self.move_Tom(pos_x + self.dir_Jerry[0]*self.length, pos_y + self.dir_Jerry[1]*self.length)
        self.table.update()

    def move_Tom(self, last_x, last_y):
        for elt in range(len(self.fantome)):
            self.newpos_x = last_x
            self.newpos_y = last_y
            self.dir_Tom = [0,0]
            list_dir = [[0, -1],[-1, -1],[-1, 0],[-1, 1],[0, 1],[1, 1],[1, 0],[1, -1]]
            distance =[]
            list =[]

            self.pos_x_tom, self.pos_y_tom = self.table.coords(self.fantome[elt])
            print(self.pos_x_tom,self.pos_y_tom)
            for i in range(len(list_dir)):
                distance.append((sqrt (((self.pos_x_tom + list_dir[i][0]*self.length-self.newpos_x)**2)+ ((self.pos_y_tom+list_dir[i][1]*self.length- self.newpos_y)**2)) , i))

            distance.sort(key = lambda list: list[0])
            print(distance)

            for i in range(8):
                list.append(distance[i][1])

            print(list)

            for i in range(8):
                self.newpos_x_Tom = self.pos_x_tom +list_dir[list[i]][0]*self.length
                self.newpos_y_Tom = self.pos_y_tom + list_dir[list[i]][1]*self.length
                self.new_grid_x_Tom = int(self.newpos_x_Tom//self.length)
                self.new_grid_y_Tom = int(self.newpos_y_Tom//self.length)
                print(self.newpos_x_Tom, self.newpos_y_Tom)


                if 0 <= self.newpos_x_Tom <= 500 and 0 <= self.newpos_y_Tom <= 500:
                    if self.grid[self.new_grid_x_Tom][self.new_grid_y_Tom] != 'X' and self.grid[self.new_grid_x_Tom][self.new_grid_y_Tom] != 'D':
                        if sqrt (((self.pos_x_tom + list_dir[i][0]*self.length-self.newpos_x)**2)+ ((self.pos_y_tom+list_dir[i][1]*self.length- self.newpos_y)**2)) - sqrt(((self.newpos_x_Tom +list_dir[i][0]*self.length - self.newpos_x)**2)+ ((self.newpos_y_Tom+list_dir[i][1]*self.length- self.newpos_x_Tom)**2)) >= 0:
                            self.table.move(self.fantome[elt], list_dir[i][0]*self.length, list_dir[i][1]*self.length)
                            break










            self.table.update()
            #self.table.itemconfigure(Tom, image = PhotoImage(file= "Fantome/Ressources/Images/Tom_left.png"))







def Ghost(User):
  jeux = ghost(User)
  return jeux.Best_Score
