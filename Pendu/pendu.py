from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from random import choice
from tkinter.font import Font
#difficulté: nombre de lettres différentes par mot: facile: <= 4, moyen: 4 < x < 8, difficile: >= 8
find = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]

accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']

class pendu:
    def __init__(self, user):
        self.user = user
        self.score = 0
        with open("Pendu/ressources/liste_francais.txt") as f:
            self.data = f.read().lower().split("\n")
        #elements du pendu
        self.elements = [lambda: self.canvas.create_rectangle(50,350,150,370, fill = "sienna4"),\
                        lambda: self.canvas.create_rectangle(90, 350, 110, 50, fill = "sienna4"),\
                        lambda: self.canvas.create_rectangle(110, 50, 350, 70, fill = "sienna4"),\
                        lambda: self.canvas.create_polygon([(110, 120), (110, 150), (170, 70), (145, 70)], fill = "sienna4"),\
                        lambda: self.canvas.create_rectangle(300, 71, 310, 110, fill = "burlywood3", width = 0),\
                        lambda: self.canvas.create_oval(290, 110, 320, 140, width = 5, outline = "tan1"),\
                        lambda: self.canvas.create_rectangle(302, 140, 307, 200, fill = "tan1", outline = "tan1"),\
                        lambda: self.canvas.create_polygon([(302, 160), (302, 165), (270, 135), (270, 130)], fill = "tan1", outline = "tan1"),\
                        lambda: self.canvas.create_polygon([(307, 160), (307, 166), (335, 136), (335, 130)], fill = "tan1", outline = "tan1"),\
                        lambda: self.canvas.create_polygon([(302, 192), (302, 200), (270, 237), (270, 230)], fill = "tan1", outline = "tan1"),\
                        lambda: self.canvas.create_polygon([(307, 192), (307, 200), (335, 237), (335, 230)], fill = "tan1", outline = "tan1")]

        for i in range(len(self.data)):
            self.data[i] = [self.data[i], letter_count(remove_accent(self.data[i]))]

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


        self.explanation = Label(self.Frame_main2_wind2, text = "Le but du jeu est de découvrir quel est  le mot mystère\n\
        fleime d'écrire la suite")
        self.explanation.place(x = 20, y = 100)
        self.Button_Skip = Button(self.Frame_main2_wind2, text = "-Skip-", command = self.quit_rules)
        self.Button_Skip.place(x = 50, y = 350)
        self.show_rules.mainloop()

        self.root = Toplevel() #fenetre principale
        self.root.title("Pendu")
        self.root.geometry("600x500")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.withdraw() #on masque la fenetre principale le temps de la sélection de la difficulté

        self.difficulty() #on charge la difficulté
        self.root.mainloop()

    def exit(self): #fonction appelée pour quiter l'application
        self.root.destroy()
        self.root.quit()

    def quit_ranking(self): #fonction utilisée pour quitter l'interface des classements
        self.show_rules.destroy()
        self.show_rules.quit()

    def quit_rules(self): #fonction pour passer des regles au classement
        self.Frame_main2_wind2.destroy()
        Scoreboard(self.Frame_main1_wind2, self.show_rules, "Pendu", self.user)

    def difficulty(self): #fonction de sélection de la difficulté
        self.root_difficulty = Toplevel()
        self.root_difficulty.title("Selectionne une difficulté")
        self.root_difficulty.geometry("300x125")
        #boutons avec les différentes difficultés
        Button(self.root_difficulty, text = "Facile", command = lambda : self.start(0)).place(x = 15, y = 70)
        Button(self.root_difficulty, text = "Moyen", command = lambda : self.start(1)).place(x = 115, y = 70)
        Button(self.root_difficulty, text = "Difficile", command = lambda : self.start(2)).place(x = 215, y = 70)
        self.root_difficulty.mainloop()

    def start(self, level): #fontion appelée après la sélection de la difficulté avec level en paramètre
        self.entred = []
        self.root_difficulty.destroy() #destruction de la fenetre de la difficulté
        self.root_difficulty.quit()
        self.level = level
        if level == 0:
            self.selection = [list[0] for list in self.data if 4 > list[1] and len(list[0]) > 3]
        elif level == 1:
            self.selection = [list[0] for list in self.data if 5 >= list[1] >= 4 and len(list[0]) > 3]
        elif level == 2:
            self.selection = [list[0] for list in self.data if list[1] > 5 and len(list[0]) > 3]
        self.word = choice(self.selection)
        self.word_accentless = remove_accent(self.word)
        print(self.word)

        self.root.deiconify()
        self.root.focus_force()

        self.error_Count = 0
        self.canvas = Canvas(self.root, width = 400, height = 400)
        self.canvas.place(x = 200, y = 100)
        start = ""
        for char in self.word:
            if char != " ":
                start += "_ "
            else:
                start += "  "
        self.result = Label(self.root, text = "{}".format(start), font = Font(size = 30))
        self.result.place(x = 30, y = 20)

        self.entry = Entry(self.root)
        self.entry.place(x = 30, y = 200)
        self.entry.bind("<Return>", self.check)
        self.entry.focus()
        self.message = Label(self.root, text = "entrée déjà saisie ou trop longue", fg = "red")
        Button(self.root, text = "Valider", command = self.check).place(x = 160, y = 195)

    def check(self, event = None):
        lettre = self.entry.get().lower()
        self.entry.delete(0, len(lettre))
        if lettre in self.entred or len(lettre) > 1:
            self.message.place(x = 30, y = 230)
        else:
            self.message.place_forget()
            self.entred.append(lettre)
            if lettre in self.word_accentless:
                old = self.result["text"]
                index = find(self.word_accentless, lettre)
                for i in range(len(index)):
                    self.result["text"] = old[:index[i]*2] + self.word[index[i]] + old[index[i]*2+1:]
                    old = self.result["text"]
                if old.replace(" ","") == self.word:
                    self.end(True)
            else:
                self.elements[self.error_Count]()
                self.error_Count += 1
                if self.error_Count == 11:
                    self.end(False)

    def end(self, win):
        scored = (self.level+1)*50*win*2*(len(self.entred)-self.error_Count)/(1+self.error_Count)
        if scored > self.score:
            print(scored)
            self.score = scored
        self.entry.unbind("<Return>")

        mess = "\nVeux-tu recommencer ?"
        if win == False:
            mess = "Perdus !, le mot était {}".format(self.word) + mess
        else:
            mess = "Gagné" + mess
        question = askquestion("Restart", mess)
        if question == "yes": #si oui, on cache la fenete et on redemande la difficulté
            self.restart()
        else:
            self.exit() #sinon on quite le jeu

    def restart(self):
        self.root.withdraw()
        for wg in self.root.winfo_children():
            wg.destroy()
        self.difficulty()

def remove_accent(word):
    for i in range(len(accent)):
        word = word.replace(accent[i], sans_accent[i])
    return word

def letter_count(word):
    lettre = []
    for letter in word:
        if letter not in lettre:
            lettre.append(letter)
    return len(lettre)

def Pendu(user):
    partie = pendu(user)
    return partie.score
