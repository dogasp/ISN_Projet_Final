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
        self.Best_Score = 0
        self.show_rules = Toplevel()
        self.show_rules.title('Règles')
        self.show_rules.geometry('700x500')
        self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking)

        self.Frame_main1_wind2 = Canvas(self.show_rules, bg = 'red', relief = GROOVE)
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 530)
        #self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
        #self.Frame_main1_wind2.create_image(335,265,image =Fond_Frame_main1_wind2)
        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
        self.Frame_main2_wind2.place(x = 60, y = 45)
        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)


        """self.explanation = Label(self.Frame_main2_wind2, text = "Le serpent va en ligne droite, on peut le dévier en utilisant\n\
            les flèches sur le clavier.\n\n\
            Si le sepent mange un fruit, il grandit et cela rapporte des points\n\n\
            Si le serpent touche un bord ou qu'il se mange lui-même, il meurt.")
        self.explanation.place(x = 50, y = 40)"""

        self.Rules2 = Label(self.Frame_main2_wind2, text = "Le but est que le serpent mange des pommes \n pour qu'il puisse grandir et gagner la partie ", font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(500, lambda: self.Rules2.place(x = 45, y = 70))

        self.CANVAS1 = Canvas(self.Frame_main2_wind2, width = 150, height = 60)
        self.Frame_main2_wind2.after(1000, lambda: self.CANVAS1.place(x = 375, y = 60 ))
        self.snake_ex_image = PhotoImage(file = "Snake/images/snake_ex_image.png")
        self.CANVAS1.create_image(75, 30,image = self.snake_ex_image)

    #------------------2-----------------------------------------------------------------
        self.Rules3 = Label(self.Frame_main2_wind2, text = 'Pour cela, tu as à disposition les flèches \n du clavier qui te permettront de déplacer.',font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(2000, lambda: self.Rules3.place(x = 35, y = 170))

        self.CANVAS2 = Canvas(self.Frame_main2_wind2,  width = 150, height = 104)
        self.Frame_main2_wind2.after(2500, lambda: self.CANVAS2.place(x = 375, y = 150 ))
        self.keyboard_snake = PhotoImage(file = "Snake/images/keyboard_snake.png")
        self.CANVAS2.create_image(73, 51,image = self.keyboard_snake)
        self.CANVAS2.create_rectangle(2,2,148,102, outline='black')

    #------------------3------------------------------------------------------------------
        self.Rules4 = Label(self.Frame_main2_wind2, text = "Cependant attention tu peux mourir en rencontrant \n\
        en mourir, ou en te retournant sur toi même.",font = ("Berlin Sans FB", 12))
        self.Frame_main2_wind2.after(3500, lambda: self.Rules4.place(x = 20, y = 300))

        self.CANVAS3 = Canvas(self.Frame_main2_wind2, width = 90, height = 62)
        self.CANVAS4 = Canvas(self.Frame_main2_wind2, width = 90, height = 62)
        self.Frame_main2_wind2.after(4000, lambda: self.CANVAS3.place(x = 402, y = 267 ))
        self.Frame_main2_wind2.after(4000, lambda: self.CANVAS4.place(x = 402, y = 332 ))
        self.mur_snake = PhotoImage(file = "Snake/images/mur_snake.png")
        self.mort_snake = PhotoImage(file = "Snake/images/mort_snake.png")
        self.CANVAS3.create_image(45, 31,image = self.mur_snake)
        self.CANVAS4.create_image(45,31, image = self.mort_snake)
    #------------------Skip------------------------------------------------------------------
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", command = self.quit_rules)
        self.Button_Skip.place(x = 200, y = 390)
        self.show_rules.mainloop()

        self.root = Toplevel()
        self.root.geometry("702x552")
        self.root.bind("<Key>", self.rotate)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()


        self.Start_image = PhotoImage(file = "Snake/images/play.png")
        self.Fruit_Image = PhotoImage(file = "Snake/images/Fruit.png")
        self.Head_Image = [PhotoImage(file = "Snake/images/Head_Right.png"),PhotoImage(file = "Snake/images/Head_Down.png"), PhotoImage(file = "Snake/images/Head_Left.png"), PhotoImage(file = "Snake/images/Head_Up.png")]
        self.Body_Image = [PhotoImage(file = "Snake/images/Horizontal.png"), PhotoImage(file = "Snake/images/Vertical.png"), PhotoImage(file = "Snake/images/Horizontal.png"), PhotoImage(file = "Snake/images/Vertical.png"),\
        PhotoImage(file = "Snake/images/Angle_Right_Top.png"),PhotoImage(file = "Snake/images/Angle_Right_Down.png"),PhotoImage(file = "Snake/images/Angle_Left_Down.png"),PhotoImage(file = "Snake/images/Angle_Left_Top.png")]
        self.Queue_Image = [PhotoImage(file = "Snake/images/Queue_Right.png"), PhotoImage(file = "Snake/images/Queue_Down.png"), PhotoImage(file = "Snake/images/Queue_Left.png"), PhotoImage(file = "Snake/images/Queue_Up.png")]


        self.start()
        self.root.mainloop()


    def quit_rules(self):
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Snake", self.User_name)

    def quit_ranking(self):
        self.show_rules.destroy()
        self.show_rules.quit()

    def start(self):
        self.grid = [[(0, 0, 0) for i in range(20)] for j in range(20)] #pour chaque élément de la grille, on a le temps de vie et la direction de la partie du serpent
        self.length_max = 2
        self.fruit = [-1, -1]
        self.dir = [1, 0]
        self.next_Rotation = 0
        self.pos = [0, 10]
        self.grid[0][10] = [2, 0, 0]
        self.pause = True


        ########------------Frames Pricipaux-------------########################################
        self.Frame_top = Frame(self.root, width = 702, height = 50, bg = 'lightgrey')
        self.Frame_right = Frame(self.root, width = 502, height = 502)
        self.Frame_left = Frame(self.root, width = 200, height = 502, bg = 'red')

        ########-----------Frames Secondaires-----------######################################
        self.Frame1 = Frame(self.Frame_left, width = 200, height =200, bg = 'gold')
        self.Frame2 = Frame(self.Frame_left, width = 200, height =300, bg = 'black')

        #######-----------Package des Frames-------------##################################

        self.Frame_top.pack(side = TOP)
        self.Frame_right.pack(side = RIGHT)
        self.Frame_left.pack(side = LEFT)
        self.Frame1.pack(side = TOP)
        self.Frame2.pack(side = BOTTOM)

        #########------------Labels et autres-----------##################################

        self.grille = Canvas(self.Frame_right, width = 501, height = 501, bg = "#1a1a1a")
        self.grille.place(x = 1, y = 1)

        self.Pause_Button = Button(self.Frame2, text = "Pause", command = self.pause_command)
        self.Pause_Button.place(x = 50, y = 100)

        self.start_button = Button(self.Frame2, image = self.Start_image,  command = self.start_game)
        self.start_button["bg"] = "white"
        self.start_button["border"] = "0"
        self.start_button.place(x = 50, y = 150)

        self.Score = Label(self.Frame1, text = "Score : 0")
        self.Score.place(x = 50, y = 150)

        self.sweet()
    
    def start_game(self):
        self.pause = False
        self.update()


    def pause_command(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False
            self.update()

    def update(self):
          if self.pause == False:
              newX = self.pos[0] + self.dir[0]
              newY = self.pos[1] + self.dir[1]
              self.grid[self.pos[0]][self.pos[1]] = [self.length_max, convert_dir(self.dir, True), self.next_Rotation]

              if self.verif(newX, newY) == True:
                  self.pos = [newX, newY]
                  for i in range(20):
                      for j in range(20):
                          if self.grid[i][j][0] != 0:
                              self.grid[i][j][0] -= 1

                  if self.next_Rotation != convert_dir(self.dir, True):
                      self.next_Rotation = convert_dir(self.dir, True)
                  self.grid[newX][newY] = [self.length_max, convert_dir(self.dir, True), convert_dir(self.dir, True)]
              else:
                  self.dead()
          if self.pause == False:
              self.grille.delete("all")

              for i in range(20):
                  for j in range(20):
                      if self.grid[i][j][0] == 0:
                          self.grille.create_rectangle(i*25, j*25, (i+1)*25, (j+1)*25, outline ='#1a1a1a',fill = '#1a1a1a' )

                      elif self.grid[i][j][0] == 1:
                          self.grille.create_image(i*25+13, j*25+13, image = self.Queue_Image[self.grid[i][j][1]])

                      elif self.grid[i][j][0] == self.length_max:
                          self.grille.create_image(i*25+13, j*25+13, image = self.Head_Image[self.grid[i][j][1]])

                      else:
                          self.grille.create_image(i*25+13, j*25+13, image = self.Body_Image[self.grid[i][j][2]])


              self.grille.create_rectangle(0,0,500,500)

              self.grille.create_image(self.fruit[0]*25 + 13, self.fruit[1]*25 + 13, image = self.Fruit_Image)

              self.root.after(150, self.update)

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
            return False
        elif x == self.fruit[0] and y == self.fruit[1]:
            for i in range(20):
                for j in range(20):
                    if self.grid[i][j][0] != 0:
                        self.grid[i][j][0] += 1
            self.length_max += 1
            self.Score["text"] = "Score : {}".format((self.length_max-2)*40)
            self.sweet()
        return True

    def exit(self):
        self.pause = True
        self.root.destroy()
        self.root.quit()

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
            old = convert_dir(self.dir, True)
            if dir == old or dir == (old+2)%4:
                return False
            else:
                if (dir == 0 and old == 1) or (dir == 3 and old == 2):
                    self.next_Rotation = 4
                elif (dir == 0 and old == 3) or (dir == 1 and old == 2):
                    self.next_Rotation = 5
                elif (dir == 1 and old == 0) or (dir == 2 and old == 3):
                    self.next_Rotation = 6
                elif (dir == 2 and old == 1) or (dir == 3 and old == 0):
                    self.next_Rotation = 7
                self.dir = convert_dir(dir)

    def dead(self):
        self.Pause_Button["state"] = "disabled"
        self.pause = True
        if (self.length_max-2)*40 > self.Best_Score:
            self.Best_Score = (self.length_max-2)*40
        question = askquestion("RESTART", "Perdu!\nVeux-tu recommencer")
        if question == "yes": #si l'utilisateur veut recommencer, on regenère l'affichage
            self.Frame_right.destroy()
            self.Frame_left.destroy()
            self.Frame_top.destroy()
            self.start()
        else:
            self.exit()


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
  return jeux.Best_Score
