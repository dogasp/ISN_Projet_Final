from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from tkinter.font import Font
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from Tetris.tiles import *
from random import choice, randint

class Tile:
    def __init__(self, pattern):
        self.pos = [3, 0]
        self.pattern = pattern[0]
        self.letter = pattern[1]
        self.index = 0

    def update(self, state, parent):
        for i in range(4):
            for j in range(4):
                if self.pattern[self.index][i][j] != "_":
                    if state == 0:
                        parent.canvas.create_image((i+self.pos[0])*(parent.width/10) + parent.width/20, (j+self.pos[1])*(parent.height/22) + parent.height/44, image = parent.image_tiles[self.letter])
                        if self.verify(i, j, parent) == True:
                            return 0
                    elif state == 2:
                        parent.canvas.create_image((i+self.pos[0])*(parent.width/10) + parent.width/20, (j+self.pos[1])*(parent.height/22) + parent.height/44, image = parent.image_tiles[self.letter])
                    else:
                        parent.next_Canvas.create_image(i*parent.width/10 + parent.width/20, j*parent.height/22 + parent.height/44, image = parent.image_tiles[self.letter])
        if state == 0:
            self.pos[1] += 1

    def verify(self, x, y, parent):
        testX = x + int(self.pos[0])
        testY = y + int(self.pos[1]) + 1
        if  testX == 10 or testY == 22 or parent.grid[testX][testY] != "":
            for i in range(4):
                for j in range(4):
                    if self.pattern[self.index][i][j] != "_":
                        parent.grid[int(i+self.pos[0])][int(self.pos[1]+j)] = self.pattern[self.index][i][j]
            rowCount = 0
            j = 0
            while j < 22:
                row = True
                for i in range(10):
                    if parent.grid[i][j] != "#":
                        row = False
                if row == True:
                    rowCount +=1
                    for k in range(10):
                        parent.grid[k][j] = ""
                    for k in range(j, 0, -1):
                        for i in range(10):
                            parent.grid[i][k] = grid[i][k-1]
                    j -= 1
                j += 1
            if rowCount == 1:
                parent.score += 40*(parent.speed//2 + 1)
            elif rowCount == 2:
                parent.score += 100*(parent.speed//2 + 1)
            elif rowCount == 3:
                score += 300*(parent.speed//2 + 1)
            elif rowCount == 4:
                score += 1200*(parent.speed//2 + 1)
            if parent.score > parent.Best_score:
                parent.Best_score = parent.score
            parent.Total_Row += rowCount
            if rowCount != 0 and parent.Total_Row%10 == 0:
                parent.speed += 2
            parent.current = parent.next
            parent.next = Tile(choice([(L, "L"), (J, "J"), (I, "I"), (O, "O"), (Z, "Z"), (S, "S"), (T, "T")]))
            parent.next_Canvas.delete("all")
            return True
        return False

    def border(self, coeff, parent):
        for i in range(4):
            for j in range(4):
                if self.pattern[self.index][i][j] != "_":
                    if i + self.pos[0] + coeff == 10 or j + self.pos[1] == 22 or i + self.pos[0] + coeff == -1 or parent.grid[int(self.pos[0]) + i + coeff][int(self.pos[1]) + j] != "":
                        return False
        return True

    def check(self):
        toTry = (self.index + 1)%len(self.pattern)
        for i in range(4):
            for j in range(4):
                if self.pattern[toTry][i][j] != "_" and (self.pos[0] + i == 10 or self.pos[0] == -1):
                    return False
        return True

class tetris:
    def __init__(self, user):
        self.user = user
        self.Best_score = 0
        self.height = 420
        self.width = 220
        self.paused = False

        self.show_rules = Toplevel()
        self.show_rules.title('Règles')
        self.show_rules.geometry('700x500')
        self.show_rules.protocol("WM_DELETE_WINDOW", self.quit_ranking) #protocole pour controler la fermeture d ela fenetre

        self.Frame_main1_wind2 = Canvas(self.show_rules, bg = 'red', relief = GROOVE) #premier frame, celui en dessous
        self.Frame_main1_wind2.pack(ipadx = 670, ipady = 530)
        #self.Fond_Frame_main1_wind2 = PhotoImage(file = "thumbnail/Tete2.png")
        #self.Frame_main1_wind2.create_image(335,265,image =Fond_Frame_main1_wind2)
        self.Frame_main2_wind2 = Frame(self.Frame_main1_wind2,width = 550, height = 425, relief = GROOVE) #second frame, au dessus
        self.Frame_main2_wind2.place(x = 60, y = 45)
        self.Rules = Label(self.Frame_main2_wind2, text = 'Les règles:', font = ("Berlin Sans FB", 23), relief = GROOVE)
        self.Rules.place(x = 200, y =5)


        self.explanation = Label(self.Frame_main2_wind2, text = "Le but du jeu est de compléter des lignes\n\
        fleime d'écrire la suite")
        self.explanation.place(x = 20, y = 100)
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", cursor ='hand2', command = self.quit_rules)
        self.Button_Skip.place(x = 50, y = 350)
        self.show_rules.mainloop()

        self.root = Toplevel()
        self.root.geometry("420x420")
        self.image_tiles = {"I": PhotoImage(file = "Tetris/Images/I.png"), "L": PhotoImage(file = "Tetris/Images/L.png"), "O": PhotoImage(file = "Tetris/Images/O.png"),\
            "J": PhotoImage(file = "Tetris/Images/J.png"), "Z": PhotoImage(file = "Tetris/Images/Z.png"), "S": PhotoImage(file = "Tetris/Images/S.png"), "T": PhotoImage(file = "Tetris/Images/T.png")}

        Label(self.root, text = "Tetris", font = Font(size = 35)).place(x = 260, y = 30)
        Label(self.root, text = "Next:", font = Font(size = 25)).place(x = 272, y = 180)
        self.aff_score = Label(self.root, text = "Score = 0", font =Font(size = 20))
        self.aff_score.place(x = 245, y = 130)
        self.aff_level = Label(self.root, text = "Level = 1", font =Font(size = 20))
        self.aff_level.place(x = 245, y = 90)

        self.start()

        self.root.mainloop()

    def exit(self): #fonction appelée pour quiter l'application
        self.run = False
        self.root.destroy()
        self.root.quit()

    def quit_ranking(self): #fonction utilisée pour quitter l'interface des classements
        self.show_rules.destroy()
        self.show_rules.quit()

    def quit_rules(self): #fonction pour passer des regles au classement
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Tetris", self.user)

    def start(self):
        self.root.bind("<Key>", self.KeyPressed)
        self.canvas = Canvas(self.root, width = 220, height = 420, bg = "grey")
        self.next_Canvas = Canvas(self.root, width = 4*self.width/10, height = 4*self.height/22, bg = "lightgrey")
        self.next_Canvas.place(x = 270, y = 230)
        self.canvas.place(x=0, y=0)
        self.grid = [["" for i in range(22)] for j in range(10)]
        self.current = Tile(choice([(L, "L"), (J, "J"), (I, "I"), (O, "O"), (Z, "Z"), (S, "S"), (T, "T")]))
        self.next = Tile(choice([(L, "L"), (J, "J"), (I, "I"), (O, "O"), (Z, "Z"), (S, "S"), (T, "T")]))
        self.run = True
        self.speed = 0
        self.score = 0
        self.Total_Row = 0
        self.frame_count = 0
        self.update()

    def update(self):
        self.frame_count += 1
        if self.frame_count % (35-self.speed) == 0:
            self.current.update(0, self)
        self.canvas.delete("all")
        if self.run == True:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] != "":
                        self.canvas.create_image(i*(self.width/10) + self.width/20, j*(self.height/22) + self.height/44, image = self.image_tiles[self.grid[i][j]])
            self.current.update(2, self)
            self.next.update(1, self)
            self.root.after(20, self.update)

    def KeyPressed(self, event):
        if event.keycode == 80:
            if self.run == True:
                self.run = False
            else:
                self.run = True
                self.update()
        keyCode = event.keysym
        if self.run == True:
            if keyCode == "Down":
                self.current.update(0, self)

            elif keyCode == "Right":
                if self.current.border(1, self) == True:
                    self.current.pos[0] += 1

            elif keyCode == "Left":
                if self.current.border(-1, self) == True:
                    self.current.pos[0] -= 1

            elif keyCode == "Up":
                if self.current.check() == True:
                    self.current.index = (self.current.index +1)%len(self.current.pattern)

def Tetris(user):
    jeux = tetris(user)
    return jeux.Best_score
