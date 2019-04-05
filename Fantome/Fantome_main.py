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
        self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking)
        self.level = 1
        self.score = 0


        self.Jerry_1 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_1.png")
        self.keyboard_fantome = PhotoImage(file = "Fantome/Ressources/Images/keyboard_fantome.png")
        self.Jerry_3 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_3.png")
        self.Jerry_2 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_2.png")




        self.Frame_main1_wind2 = Canvas(self.show_rules, bg = 'red', relief = GROOVE)
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 530)
        #self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
        #self.Frame_main1_wind2.create_image(335,265,image =Fond_Frame_main1_wind2)
        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
        self.Frame_main2_wind2.place(x = 60, y = 45)
        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)

        #détail des rêgles

        self.Rules2 = Label(self.Frame_main2_wind2, text = "Le but est que Jerry puisse arriver \n\
        au fromage sans que Tom l'attrape. \n Pour cela tu pourras utiliser les flèches \n du keyboard afin de déplacer Jerry", font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(500, lambda: self.Rules2.place(x = 40, y = 70))

        self.CANVAS1 = Canvas(self.Frame_main2_wind2, width = 120, height = 70)
        self.CANVAS2 = Canvas(self.Frame_main2_wind2, width = 100, height = 70)
        self.Frame_main2_wind2.after(1000, lambda: self.CANVAS1.place(x = 388, y = 35))
        self.Frame_main2_wind2.after(1000, lambda: self.CANVAS2.place(x = 400, y = 106))
        self.CANVAS1.create_image(60, 35,image = self.Jerry_1)
        self.CANVAS2.create_image(50, 35,image = self.keyboard_fantome)
        self.CANVAS2.create_rectangle(2,2,98,68, outline='black')

    #------------------2-----------------------------------------------------------------
        self.Rules3 = Label(self.Frame_main2_wind2, text = "Mais Attention !! Tom va plus vite que toi car il peut \n\
        se déplacer en diagonale. Tom se déplace par \n rapport à Jerry et fait tout pour se rapprocher." ,font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(2000, lambda: self.Rules3.place(x = 30, y = 202))

        self.CANVAS3 = Canvas(self.Frame_main2_wind2,  width = 100, height = 100)
        self.Frame_main2_wind2.after(2500, lambda: self.CANVAS3.place(x = 400, y = 183 ))
        self.CANVAS3.create_image(50,50, image = self.Jerry_3)

    #------------------3------------------------------------------------------------------
        self.Rules4 = Label(self.Frame_main2_wind2, text = "L'astuce est alors de bloquer le robot grâce\n\
        aux bloques disposés sur la carte",font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(3500, lambda: self.Rules4.place(x = 40, y = 315))
#
        self.CANVAS4 = Canvas(self.Frame_main2_wind2, width = 130, height = 95)
        self.Frame_main2_wind2.after(4000, lambda: self.CANVAS4.place(x = 388, y = 293 ))
        self.CANVAS4.create_image(65, 47,image = self.Jerry_2)

    #------------------Skip------------------------------------------------------------------
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", command = self.quit_rules)
        self.Button_Skip.place(x = 200, y = 390)
        self.show_rules.mainloop()

        self.root = Toplevel()
        self.root.geometry("702x552")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()


        self.start()
        self.time_num()

        self.root.mainloop()




    def quit_rules(self):
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Ghost", self.User_name)

    def quit_ranking(self):
        self.show_rules.destroy()
        self.show_rules.quit()

    def exit(self):
        self.root.destroy()
        self.root.quit()


    def start(self):
        self.root.focus_force()
        self.root.bind("<Key>", self.move_Jerry)

        self.nbcases = (7, 8, 10)
        self.length = 500/self.nbcases[self.level - 1]
        self.fantome = []
        self.Best_Score = 0
        self.time_game = 0
        self.move = 0


        self.grid = [[(0) for i in range(self.nbcases[self.level - 1])] for j in range((self.nbcases[self.level - 1]))]

        #########-----------Import des photos-------------#################################
        self.Jerry_image = PhotoImage(file = "Fantome/Ressources/Images/Jerry.png")
        self.Tom_image_left = PhotoImage(file = "Fantome/Ressources/Images/Tom_left.png")
        self.Tom_image_right = PhotoImage(file = "Fantome/Ressources/Images/Tom_right.png")
        self.Fromage_image = PhotoImage(file = "Fantome/Ressources/Images/fromage.png")
        self.Fromage_Jerry_image = PhotoImage(file = "Fantome/Ressources/Images/Fromage_Jerry.png")
        self.Tom_right_image = PhotoImage(file = "Fantome/Ressources/Images/Tom_Jerry.png")
        ########------------Frames Pricipaux-------------########################################
        self.Frame_top = Frame(self.root, width = 700, height = 50, bg = 'lightgrey')
        self.Frame_right = Frame(self.root, width = 500, height = 500)
        self.Frame_left = Frame(self.root, width = 200, height = 500, bg = 'red')

        #######-----------Package des Frames-------------####################################
        self.Frame_top.pack(side = TOP)
        self.Frame_right.pack(side = RIGHT)
        self.Frame_left.pack(side = LEFT)

        ######-----------Elements du jeu-----------------##########################################
        self.show_time = Label(self.Frame_left, text = "Temps: %s" %str(0),font = ("Berlin Sans FB", 12))
        self.show_time.place(x = 45, y = 70)

        self.show_score = Label(self.Frame_left, text = "Score: %s" %str(int(self.score)), font = ("Helvetica", 10), relief = GROOVE)
        self.show_score.place(x = 25, y = 170)

        self.table = Canvas(self.Frame_right, width = 500, height = 500, bg = "#1a1a1a")
        self.table.pack(fill = BOTH)

        for i in range(self.nbcases[self.level - 1]):
            self.table.create_line((self.length)*i,0,(self.length)*i,500,fill = 'blue')
        for j in range(self.nbcases[self.level - 1]):
            self.table.create_line(0,(self.length)*j,500,(self.length)*j, fill = 'blue')

        for j in range(self.nbcases[self.level - 1]):
            for i in range(self.nbcases[self.level - 1]):
                self.grid[i][j] = level_map[self.level - 1][(j*self.nbcases[self.level - 1])+i]

                if self.grid[i][j] == 'X':
                    self.table.create_rectangle(self.length* i, self.length* j,self.length* (i+1), self.length*(j+1), fill = 'red')
                elif self.grid[i][j] == 'R':
                    self.robot = self.table.create_image(self.length* i +self.length/2, self.length* j +self.length/2, image = self.Jerry_image)
                elif self.grid[i][j] == 'F':
                    self.Tom = self.table.create_image(self.length* i +self.length/2, self.length* j +self.length/2, image = self.Tom_image_left)
                    self.fantome.append(self.Tom)
                elif self.grid[i][j] == 'D':
                    self.Drapeau = self.table.create_image(self.length* i +self.length/2, self.length* j +self.length/2, image = self.Fromage_image)

    def move_Jerry(self, event = None):
        self.move += 1
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
            list_dir = [[0, -1],[-1, -1],[-1, 0],[-1, 1],[0, 1],[1, 1],[1, 0],[1, -1], [0,0]]
            distance =[]
            list =[]

            self.pos_x_tom, self.pos_y_tom = self.table.coords(self.fantome[elt])
            for i in list_dir:
                if 0 <= self.pos_x_tom + i[0]*self.length < 500 and 0 <= self.pos_y_tom+i[1]*self.length <= 500:
                    if self.grid[int(self.pos_x_tom//self.length + i[0])][int(self.pos_y_tom//self.length + i[1])] == "0" or self.grid[int(self.pos_x_tom//self.length + i[0])][int(self.pos_y_tom//self.length + i[1])] == "F":
                        distance.append((sqrt (((self.pos_x_tom + i[0]*self.length-self.newpos_x)**2)+ ((self.pos_y_tom+i[1]*self.length- self.newpos_y)**2)) , i))

            distance.sort(key = lambda list: list[0])
            list = [j[1] for j in distance]

            self.newpos_x_Tom = self.pos_x_tom +list[0][0]*self.length
            self.newpos_y_Tom = self.pos_y_tom + list[0][1]*self.length
            self.new_grid_x_Tom = int(self.newpos_x_Tom//self.length)
            self.new_grid_y_Tom = int(self.newpos_y_Tom//self.length)
            if list[0][0] == 1:
                self.table.itemconfigure(self.Tom, image = self.Tom_image_right)
            else:
                self.table.itemconfigure(self.Tom, image = self.Tom_image_left)


            self.table.move(self.fantome[elt], list[0][0]*self.length, list[0][1]*self.length)
            self.verif(self.new_grid_x_Jerry,self.new_grid_y_Jerry,self.new_grid_x_Tom,self.new_grid_y_Tom)
            self.table.update()


    def verif(self,next_jerry_x, next_jerry_y,next_tom_x, next_tom_y):
        if self.grid[next_jerry_x][next_jerry_y] == "D":
            self.table.itemconfigure(self.Drapeau, image = self.Fromage_Jerry_image)
            self.table.itemconfigure(self.robot,  image = self.Fromage_Jerry_image)
            self.root.unbind("<Key>")
            self.win()

        elif next_jerry_x == next_tom_x and next_jerry_y == next_tom_y:
            self.table.itemconfigure(self.Tom, image = self.Tom_right_image)
            self.table.itemconfigure(self.robot,  image = self.Tom_right_image)
            self.root.unbind("<Key>")
            #self.dead()

    def time_num(self):
        self.time_game+=1
        self.root.after(1000,self.time_num)
        self.show_time['text'] = "Temps: %s" %str(self.time_game)

    def win(self):
        self.score_temp = (10000/(self.move*0.8 + self.time_game*0.2)) * self.level
        self.score += self.score_temp
        self.show_score["text"] = "Score: %s"%str(int(self.score))
        self.question = Toplevel()
        self.question.geometry("300x125")
        Button(self.question, text = "Restart", command = self.restart_question,cursor ='hand2', font = ("Helvetica", 10)).place(x = 30, y = 45)
        Button(self.question, text = "Main Menu", command = self.exit_menu,cursor ='hand2', font = ("Helvetica", 10)).place(x = 210, y = 45)
        Button(self.question, text = "Next Level", command = self.next,cursor ='hand2', font = ("Helvetica", 10)).place(x = 110, y = 45)

    def dead(self):
        self.score -= 50*(self.level)
        self.Frame_right.destroy()               # destruction des frames
        self.Frame_left.destroy()
        self.Frame_top.destroy()
        self.start()

    def restart_question(self):
        self.question.destroy()
        self.question2 = askquestion("RESTART", "Est-tu-sur de recommencer ? Tu perdras à chaque fois 50 points multiplié par le niveau où tu es")
        if self.question2 == "yes": #si l'utilisateur veut recommencer, on regenère l'affichage
            self.score -= 50*(self.level)
            self.update()
        else:
            self.win()

    def exit_menu(self):
        self.exit()

    def next(self):
        self.question.destroy()
        self.level += 1
        self.Frame_right.destroy()               # destruction des frames
        self.Frame_left.destroy()
        self.Frame_top.destroy()
        self.start()

    def update(self):
        self.Frame_right.destroy()               # destruction des frames
        self.Frame_left.destroy()
        self.Frame_top.destroy()
        self.start()

def Ghost(User):
  jeux = ghost(User)
  return jeux.score
