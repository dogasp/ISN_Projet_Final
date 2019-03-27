from tkinter import *
from Tete_chercheuse.tete_chercheuse import *
#import Tete_chercheuse.tete_chercheuse
class BoutonS:
    def __init__(self, x, y, jeux):
        self.x = x
        self.y = y
        self.jeux = jeux

    def command(self):
        root_main.withdraw()
        result = self.jeux()
        print(result)
        root_main.deiconify()

root_main = Tk()
root_main.geometry('1000x600')

Frame_top = Frame(root_main, bg ='pink')
Frame_top.pack(ipadx = 1000, ipady =50, side = TOP)

Frame_left = Frame(root_main, bg ='yellow')
Frame_left.pack(ipadx = 50, ipady =500,side = LEFT)

Frame_right = Frame(root_main, bg ='green')
Frame_right.pack(ipadx = 50, ipady =500,side = RIGHT)

Frame_down = Frame(root_main, bg ='black')
Frame_down.pack(ipadx = 900, ipady = 20,side = BOTTOM)

Frame_main = Frame(root_main,bg = 'red',borderwidth=2, relief=GROOVE)
Frame_main.pack(ipadx = 900, ipady =530,side = BOTTOM)

BoutonS(0,1, tete_start).command()
root_main.mainloop()


# [['x', 0, 'x', 0, 'x', 0, 'x', 0], ['x', 0, 'x', 0, 'x', 0, 'x', 0]]
