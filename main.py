from tkinter import *

class BoutonS:
    def __init__(self, x, y, jeux):


    def command(self):
        pass

root = Tk()
root.geometry('1000x600')


Frame_top = Frame(root, bg ='pink')
Frame_top.pack(ipadx = 1000, ipady =50, side = TOP)

Frame_left = Frame(root, bg ='yellow')
Frame_left.pack(ipadx = 50, ipady =500,side = LEFT)

Frame_right = Frame(root, bg ='green')
Frame_right.pack(ipadx = 50, ipady =500,side = RIGHT)

Frame_down = Frame(root, bg ='black')
Frame_down.pack(ipadx = 900, ipady = 20,side = BOTTOM)

Frame_main = Frame(root,bg = 'red',borderwidth=2, relief=GROOVE)
Frame_main.pack(ipadx = 900, ipady =530,side = BOTTOM)

nom_de_jeux = ["Tête Cherseuse", "Pong", "space Invaders", "Snake", "Tetris", "Jeu 6", "Jeu 7", "Jeu 8",]

for i in range(10):
    Frame_main.rowconfigure(i)
    Frame_main.columnconfigure(i)

BoutonS(1, 1, "bite")
"""
for i in range(4):
    for j in range(2):
        Label[i] = Label()
j*nbcases_width)+i
"""






root.mainloop()
