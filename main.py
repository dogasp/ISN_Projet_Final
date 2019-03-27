from tkinter import *
from Tete_chercheuse.tete_chercheuse import *
from Reseau.client import *

class BoutonS: #classe pour gérer les boutons interactifs
    def __init__(self, x, y, jeux, run): # a besoin de cligne, colone, ne nom du jeux et la commande our executer le jeu
        self.image = PhotoImage(file = "thumbnail/" + jeux + ".png") #on charge l'immage correspondante au jeu
        self.button = Button(Frame_main, image = self.image, command = self.command) #création du boutton
        self.button.grid(row = x, column = y)
        self.jeux = jeux
        self.run = run

    def command(self): #fonction executée lors du clique sur le boutton
        root_main.withdraw() #on masque l'interface principale
        result = self.run() #on execute le jeu
        push_score("random", self.jeux, result) #on envois au serveur le score de la partie
        root_main.deiconify() #on fait réapparaite la fenetre principale

root_main = Tk()
root_main.geometry('1000x600')

Frame_top = Frame(root_main, bg ='pink') #création des pannels
Frame_top.pack(ipadx = 1000, ipady =50, side = TOP)

Frame_left = Frame(root_main, bg ='yellow')
Frame_left.pack(ipadx = 50, ipady =500,side = LEFT)

Frame_right = Frame(root_main, bg ='green')
Frame_right.pack(ipadx = 50, ipady =500,side = RIGHT)

Frame_down = Frame(root_main, bg ='black')
Frame_down.pack(ipadx = 900, ipady = 20,side = BOTTOM)

Frame_main = Frame(root_main,bg = 'red',borderwidth=2, relief=GROOVE)
Frame_main.pack(ipadx = 900, ipady =530,side = BOTTOM)

score = get_score_list() #récupération du scoreboard
print(score)


nom_de_jeux = ["Tête Cherseuse", "Pong", "space Invaders", "Snake", "Tetris", "Jeu 6", "Jeu 7", "Jeu 8",]

for i in range(9):
    Frame_main.rowconfigure(i, weight = 1)
    Frame_main.columnconfigure(i ,weight =1)

Label_list0= Label(Frame_main, text = nom_de_jeux[0]) #labels
Label_list1= Label(Frame_main, text = nom_de_jeux[1])
Label_list2= Label(Frame_main, text = nom_de_jeux[2])
Label_list3= Label(Frame_main, text = nom_de_jeux[3])
Label_list4= Label(Frame_main, text = nom_de_jeux[4])
Label_list5= Label(Frame_main, text = nom_de_jeux[5])
Label_list6= Label(Frame_main, text = nom_de_jeux[6])
Label_list7= Label(Frame_main, text = nom_de_jeux[7])

Label_list0.grid(row = 2, column = 1)
Label_list1.grid(row = 2, column = 3)
Label_list2.grid(row = 2, column = 5)
Label_list3.grid(row = 2, column = 7)
Label_list4.grid(row = 4, column = 1)
Label_list5.grid(row = 4, column = 3)
Label_list6.grid(row = 4, column = 5)
Label_list7.grid(row = 4, column = 7)

bouton_0 = BoutonS(3, 1, "Tete", Tete)

root_main.mainloop()
