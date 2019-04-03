from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
#difficultés: 9x9: 10, 16x16: 40, 16x30: 99

class demineur:
    def __init__(self), user:
        self.User = user
        self.level = 0

        self.Number_Image = []

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


        self.explanation = Label(self.Frame_main2_wind2, text = "Le but du jeu est de découvrir toutes les mines\n\
            sans se faire exploser. Il faut donc cliquer (gauche) sur les cases avec afin de révéler des numéros\n\
            ils indiquerons le nombre de bombes voisines. Si une cellule est succeptible d'être une bombe,\n\
            un clique droit marquera la case avec un drapeau.\n\n\
            Il y a trois difficultés, la taille de la grille ainsi que le nombre de mines change entre les niveaux.")
        self.explanation.place(x = 50, y = 100)
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", command = self.quit_rules)
        self.Button_Skip.place(x = 50, y = 400)
        self.show_rules.mainloop()

        self.root = Toplevel()
        self.root.bind("<Button>", self.click)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()

        self.difficulty()
        self.root.mainloop()

    def quit_rules():
        self.Frame_main2_wind2.destroy()
        Scoreboard(Frame_main1_wind2, self.show_rules, "Minesweeper", self.User)
    
    def difficulty(self):
        root_difficulty = Toplevel()
        root_difficulty.title("Selectionne une difficulté")
        root_difficulty.geometry("300x125")
        Button(root_difficulty, text = "Facile", command = lambda : self.start(0)).place(x = 50, y = 70)
        Button(root_difficulty, text = "Moyen", command = lambda : self.start(1)).place(x = 150, y = 70)
        Button(root_difficulty, text = "Difficile", command = lambda : self.start(2)).place(x = 250, y = 70)
    
    def start(self, level):
        self.level = level
        if level == 0:
            self.dims = (9,9)
            self.mine_Count = 10
        elif level == 1:
            self.dims = (16,16)
            self.mine_Count = 40
        else:
            self.dims = (16, 30)
            self.mine_Count = 99
        self.root.geometry("%sx%s" % (self.dims[0]*))
        

    def exit(self):
        self.root.destroy()
        self.root.quit()

    def click(self, event):
        if event.num == 1: #clique gauche

        elif event.num == 3: #clique droit

def Minesweeper(user):
    jeux = demineur(user)
    return jeux.score
