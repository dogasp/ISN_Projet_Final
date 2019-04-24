from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import randint
from math import*

class bird:
    def __init__(self,user):
        self.User_name = user
        self.Best_Score = 0
        self.show_rules = Toplevel()
        self.show_rules.title('Règles')
        self.show_rules.geometry('670x530')
        self.show_rules.resizable(False,False)
        self.show_rules.focus_force()
        self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking)

        self.Frame_main1_wind2 = Canvas(self.show_rules, bg = 'red', relief = GROOVE)
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 526)
        #self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Ghost2.png")
        #self.Frame_main1_wind2.create_image(335,263,image =self.Fond_Frame_main1_wind2)
        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE)
        self.Frame_main2_wind2.place(x = 60, y = 45)
        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)

        self.Jerry_1 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_1.png")
        self.keyboard_fantome = PhotoImage(file = "Fantome/Ressources/Images/keyboard_fantome.png")
        self.Jerry_3 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_3.png")
        self.Jerry_2 = PhotoImage(file = "Fantome/Ressources/Images/Jerry_2.png")

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

        self.CANVAS4 = Canvas(self.Frame_main2_wind2, width = 130, height = 95)
        self.Frame_main2_wind2.after(4000, lambda: self.CANVAS4.place(x = 388, y = 293 ))
        self.CANVAS4.create_image(65, 47,image = self.Jerry_2)

    #------------------Skip------------------------------------------------------------------
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", cursor ='hand2', command = self.quit_rules)
        self.Button_Skip.place(x = 200, y = 390)
        self.show_rules.mainloop()

        """#################----------------- début du jeu ----------------#################### """
        self.root = Toplevel()
        self.root.geometry("900x550")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.resizable(False,False)
        self.root.title('Flappy Bird')
        self.root.focus_force()

        ########-----------Frames Principaux------------#######################################
        self.Frame_left = Frame(self.root, width = 200, height = 500, bg = 'white')
        self.Frame_top = Frame(self.root, width = 900, height = 50, bg = 'grey')

        ########-----------Frames Secondaires------------#######################################
        self.Frame1 = Frame(self.Frame_left, width = 200, height = 200, bg = 'yellow')
        self.Frame2 = Frame(self.Frame_left, width = 200, height = 300, bg = 'red')

        #######-----------Package des Frames-------------####################################
        self.Frame_top.pack(side = TOP)
        self.Frame_left.pack(side = LEFT)
        self.Frame1.pack(side = TOP)
        self.Frame2.pack(side = BOTTOM)

        ######-----------Elements du jeu-----------------##########################################
        self.sentence = Label(self.Frame2, text = "Attrape Moi \n Si Tu Peux !!!",font = ("Berlin Sans FB", 15), bg = 'white')
        self.sentence.place(x = 45, y = 60)

        self.canvas_show_time = Canvas(self.Frame1, bg = 'black',highlightthickness=0)
        self.canvas_show_time.place(x = 10, y = 30)
        self.show_time = Label(self.canvas_show_time, text = "Temps: %s" %str(0), foreground = 'blue2', bg = 'black',font = ("Berlin Sans FB", 24))
        self.show_time.pack(padx= 3, pady = 3)

        self.root.bind("<space>", self.bird_up)
        self.x = 0
        self.y = -80
        self.dx = -0.2
        self.dy = 0.2
        self.vitesse = 0
        self.compte = 0
        self.test2 = PhotoImage(file = 'Flappy_Bird/Ressources/test2.png')

        self.start()
        self.root.mainloop()

    def quit_rules(self):
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Flappy", self.User_name)
        self.show_rules.destroy()
        self.show_rules.quit()


    def quit_ranking(self):
        self.show_rules.destroy()
        self.show_rules.quit()

    def exit(self):
        self.root.destroy()
        self.root.quit()

    def start(self):
        self.root.focus_force()


        self.tuyau0 = Pipe(self, 500,350)
        self.tuyau1 = Pipe(self, 900, randint(150,550))
        self.tuyau2 = Pipe(self, 1300, randint(150,550))
        self.tuyau3 = Pipe(self, 1700, randint(150,550))
        self.tuyau = [self.tuyau0,self.tuyau1,self.tuyau2,self.tuyau3]


        self.Frame_right = Frame(self.root, width = 700, height = 500, bg = 'black')
        self.Frame_right.pack(side = RIGHT)

        self.Canvas_world = Canvas(self.Frame_right, width = 1700, height = 500, highlightthickness=0)
        self.Canvas_world.place(x = 0, y = 0)

        self.trait = self.Canvas_world.create_line(250,0,250,500)
        self.image_Bird = self.Canvas_world.create_image(100,100,  image = self.test2)

        self.tuyau0.create_pipe()
        self.tuyau0.move_pipe()
        self.tuyau1.create_pipe()
        self.tuyau1.move_pipe()
        self.tuyau2.create_pipe()
        self.tuyau2.move_pipe()
        self.tuyau3.create_pipe()
        self.tuyau3.move_pipe()
        self.bird_down()

    def bird_up(self, event = None):
        self.vitesse = 0
        self.x_center_bird, self.y_center_bird=  self.Canvas_world.coords(self.image_Bird)
        self.Canvas_world.move(self.image_Bird, self.x,self.y)


    def bird_down(self):
        self.vitesse +=1
        self.x_center_bird, self.y_center_bird =  self.Canvas_world.coords(self.image_Bird)
        self.Canvas_world.move(self.image_Bird, self.x,self.vitesse)
        self.root.after(50,self.bird_down)
        if self.y_center_bird +self.vitesse + 10 > 500:
            self.dead()



def dead(self):
    self.root.destroy()
    self.root.quit()

class Pipe:
    def __init__(self, parent, x_pipe = 0, y_pipe = randint(150,550)):
        self.x_pipe = x_pipe
        self.y_pipe = y_pipe
        self.y_pipe_top = y_pipe - 75
        self.y_pipe_down = y_pipe + 75
        self.parent = parent
        self.move_x = -8
        self.compte = 0




        self.test = PhotoImage(file = 'Flappy_Bird/Ressources/test.png')

    def create_pipe(self):
        self.top_pipe =  self.parent.Canvas_world.create_image(self.x_pipe + 75, self.y_pipe_top/2,  image = self.test)
        self.down_pipe =  self.parent.Canvas_world.create_image(self.x_pipe + 75, (self.y_pipe_top+700)/2,  image = self.test)

    def move_pipe(self):
        self.parent.Canvas_world.move(self.top_pipe, self.move_x,0)
        self.parent.Canvas_world.move(self.down_pipe, self.move_x,0)
        self.x_center_top_pipe, self.y_center_top_pipe =  self.parent.Canvas_world.coords(self.top_pipe)
        self.x_center_down_pipe, self.y_center_down_pipe =  self.parent.Canvas_world.coords(self.down_pipe)
        self.verif_pipe(self.x_center_top_pipe, self.y_center_top_pipe, self.x_center_down_pipe, self.y_center_down_pipe)

    def verif_pipe(self, x_center_top_pipe, y_center_top_pipe, x_center_down_pipe, y_center_down_pipe):

        if x_center_top_pipe + 75 < 0:
            print(self.parent.compte)
            self.parent.Canvas_world.delete(self.top_pipe)
            self.parent.Canvas_world.delete(self.down_pipe)

            self.parent.tuyau[self.compte].create_pipe()
            self.parent.tuyau[self.compte].move_pipe()
            self.parent.compte+=1
            if self.parent.compte == 4:
                self.parent.compte = 0
        else:
            self.parent.root.after(50,self.move_pipe)














def Flappy_Bird(User):           # fonction pour commencer le jeu
  jeux = bird(User)       # création de l'instance
  return jeux.Best_Score   #renvois du meilleur score
