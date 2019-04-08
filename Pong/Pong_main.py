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


class pong:
    def __init__(self, user):
        self.User_name = user
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
        self.root.geometry("702x552")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()

        ########-----------Frames Principaux------------#######################################
        self.Frame_left = Frame(self.root, width = 200, height = 500, bg = 'white')
        self.Frame_top = Frame(self.root, width = 700, height = 50, bg = 'lightgrey')

        ########-----------Frames Secondaires------------#######################################
        self.Frame1 = Frame(self.Frame_left, width = 200, height = 200)
        self.Frame2 = Frame(self.Frame_left, width = 200, height = 300, bg = 'black')

        #######-----------Package des Frames-------------####################################
        self.Frame_top.pack(side = TOP)
        self.Frame_left.pack(side = LEFT)
        self.Frame1.pack(side = TOP)
        self.Frame2.pack(side = BOTTOM)

        self.root.mainloop()
