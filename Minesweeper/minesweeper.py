from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import choice
#difficultés: 9x9: 10, 16x16: 40, 16x30: 99

around = lambda x, y: [(x-1, y-1), (x-1, y), (x-1, y+1), (x,y+1), (x,y-1), (x+1, y-1), (x+1, y), (x+1, y+1)]

class demineur:
    def __init__(self, user):
        self.score = 0
        self.User = user
        self.level = 0
        self.border = 25 #taille d'une cellule

        self.Number_Image = [PhotoImage(file = "Minesweeper/Images/0.png").subsample(8), PhotoImage(file = "Minesweeper/Images/1.png").subsample(8), PhotoImage(file = "Minesweeper/Images/2.png").subsample(8),\
            PhotoImage(file = "Minesweeper/Images/3.png").subsample(8), PhotoImage(file = "Minesweeper/Images/4.png").subsample(8), PhotoImage(file = "Minesweeper/Images/5.png").subsample(8),\
            PhotoImage(file = "Minesweeper/Images/6.png").subsample(8), PhotoImage(file = "Minesweeper/Images/7.png").subsample(8), PhotoImage(file = "Minesweeper/Images/8.png").subsample(8)]
        self.bomb_Image = PhotoImage(file = "Minesweeper/Images/bomb.png").subsample(8)
        self.Normal_Image = PhotoImage(file = "Minesweeper/Images/facingDown.png").subsample(8)
        self.Flag_Image = PhotoImage(file = "Minesweeper/Images/flagged.png").subsample(8)

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
        self.explanation.place(x = 20, y = 100)
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", command = self.quit_rules)
        self.Button_Skip.place(x = 50, y = 350)
        self.show_rules.mainloop()

        self.root = Toplevel()
        self.root.title("Minesweeper")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.withdraw()

        self.difficulty()
        self.root.mainloop()
        
    def quit_ranking(self):
        self.show_rules.destroy()
        self.show_rules.quit()

    def quit_rules(self):
        self.Frame_main2_wind2.destroy()
        Scoreboard(Frame_main1_wind2, self.show_rules, "Minesweeper", self.User)
    
    def difficulty(self):
        self.root_difficulty = Toplevel()
        self.root_difficulty.title("Selectionne une difficulté")
        self.root_difficulty.geometry("300x125")
        Button(self.root_difficulty, text = "Facile", command = lambda : self.start(0)).place(x = 15, y = 70)
        Button(self.root_difficulty, text = "Moyen", command = lambda : self.start(1)).place(x = 115, y = 70)
        Button(self.root_difficulty, text = "Difficile", command = lambda : self.start(2)).place(x = 215, y = 70)
        self.root_difficulty.mainloop()
    
    def start(self, level):
        self.root_difficulty.destroy()
        self.root_difficulty.quit()
        self.level = level
        if level == 0:
            self.dims = (9,9)
            self.mine_Count = 10
        elif level == 1:
            self.dims = (16,16)
            self.mine_Count = 40
        else:
            self.dims = (30, 16)
            self.mine_Count = 99
        self.root.deiconify()
        self.root.focus_force()
        self.root.geometry("%sx%s" % (200 + self.dims[0]*self.border, self.dims[1]*self.border))
        self.grid = [[0 for i in range(self.dims[1])] for j in range(self.dims[0])]

        index = [i for i in range(self.dims[0]*self.dims[1])]
        for _ in range(self.mine_Count):
            temp = choice(index)
            index.remove(temp)
            self.grid[temp//self.dims[0]][temp%self.dims[0]] = -1
        
        for x in range(self.dims[0]):
            for y in range(self.dims[1]):
                if self.grid[x][y] == -1:
                    for xp, yp in around(x, y):
                        if self.dims[0] > xp >-1 and self.dims[1] > yp >= 0 and self.grid[xp][yp]!=-1:
                            self.grid[xp][yp] += 1

        self.canvas = Canvas(self.root, width = self.dims[0]*self.border, height = self.dims[1]*self.border, bg = "red")
        self.canvas.bind("<Button>", self.click)
        self.canvas.place(x = 200, y = 0)

        self.list_images = [[0 for i in range(self.dims[1])] for j in range(self.dims[0])]
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                self.list_images[i][j] = self.canvas.create_image(i*self.border + self.border/2, j*self.border + self.border/2, image = self.Normal_Image)

    def exit(self):
        self.root.destroy()
        self.root.quit()

    def click(self, event):
        x = event.x//self.border
        y = event.y//self.border
        if event.num == 1: #clique gauche
            value = self.grid[x][y]
            if self.list_images[x][y] == self.Flag_Image:
                self.canvas.itemconfigure(self.list_images[x][y], image = self.Normal_Image)
                self.click(event)
            elif value == -1:
                count = 0
                for i in range(self.dims[0]):
                    for j in range(self.dims[1]):
                        if self.list_images[i][j] == self.Flag_Image and self.grid[i][j] == -1:
                            count += 1
                self.end(False, count)
            elif value > 0:
                self.canvas.itemconfigure(self.list_images[x][y], image = self.Number_Image[value])
            elif value == 0:
                self.canvas.itemconfigure(self.list_images[x][y], image = self.Number_Image[value])
                process = around(x, y)
                done = process.copy()
                while len(process) != 0:
                    next_process = []
                    for x,y in process:
                        if self.dims[0] > x >-1 and self.dims[1] > y >= 0:
                            value = self.grid[x][y]
                            self.canvas.itemconfigure(self.list_images[x][y], image = self.Number_Image[value])
                            if value == 0:
                                for xb,yb in around(x, y):
                                    if (xb, yb) not in done:
                                        done.append((xb,yb))
                                        next_process.append((xb, yb))
                    process = next_process
            
        elif event.num == 3: #clique droit
            self.canvas.itemconfigure(self.list_images[x][y], image = self.Flag_Image)
        count = 0
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                try:
                    if self.list_images[i][j] == self.Flag_Image and self.grid[i][j] == -1:
                        print("buh")
                        count += 1
                except: pass
        print(count, self.mine_Count)
        if count == self.mine_Count:
            self.end(True, count)
        self.canvas.update()

    def end(self, win, count = 0):
        if win == False:
            for x in range(self.dims[0]):
                for y in range(self.dims[1]):
                    if self.grid[x][y] == -1:
                        self.canvas.itemconfigure(self.list_images[x][y], image = self.bomb_Image)
        self.score = count* 50 #ajouter le temps
        question = askquestion("Restart", "Partie finie.\nVeux-tu recommencer?")
        if question == "yes":
            self.root.withdraw()
            self.difficulty()
        else:
            self.exit()
        

def Minesweeper(user):
    jeux = demineur(user)
    return jeux.score
