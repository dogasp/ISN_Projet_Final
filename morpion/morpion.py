from tkinter import* #@unusedWildImport
from tkinter.messagebox import *
"""Il serait meilleur dans notre cas d'utiliser une classe afin d'eviter les definitions globales, economiser de la RAM / du CPU et simplifier le code"""

def placer(event = None): #fonction executee quand il y a un clic sur le cnavas
    global cases
    X = (event.x - event.x%tailleCase) + tailleCase/2 #on recupère les coordonees de la cellule cliquee
    Y = (event.y - event.y%tailleCase) + tailleCase/2

    if cases[X,Y] == "":
        cases[X,Y] = joueur[1] #si la calse etait vide, on la remplis
        verifier()

def jouer(event = None): #fonction principale
    global Main
    global tour
    global joueur

    if tour%2 == 0: #tour pair = joueur 1
        joueur = ("Joueur 1", "X")
    else:
        joueur = ("Joueur 2", "O")

    tour +=1
    Main["text"]= joueur[0]
    fenetre.unbind("<Return>") #on enlève le bind de la touche entree à la fenetre

def verifier(): #fonction de verification si quelqu'un a aligne trois cases
    global Main
    global score
    win = None #variable pour verifier si quelqu'un a gagne
    #lignes et colones
    
    for x in range(int(tailleCase/2), int(3*tailleCase + tailleCase/2), tailleCase): # range(50,350,100) x prends les valeurs 50,150,250
        if cases[x, tailleCase/2] == cases[x, tailleCase + tailleCase/2] == cases[x, 2*tailleCase + tailleCase/2] == "O":
            Main["text"]= "Joueur 2 a gagne"
            win = 1
        elif cases[x, tailleCase/2] == cases[x, tailleCase + tailleCase/2] == cases[x, 2*tailleCase + tailleCase/2] == "X":
            Main["text"]= "Joueur 1 a gagne"
            win = 0

    for y in range(int(tailleCase/2), int(3*tailleCase + tailleCase/2), tailleCase):# range(50,350,100) y prends les valeurs 50,150,250
        if cases[tailleCase/2, y] == cases[tailleCase + tailleCase/2, y] == cases[2*tailleCase + tailleCase/2, y] == "O":
            Main["text"]= "Joueur 2 a gagne"
            win = 1
        elif cases[tailleCase/2, y] == cases[tailleCase + tailleCase/2, y] == cases[2*tailleCase + tailleCase/2, y] == "X":
            Main["text"] = "Joueur 1 a gagne"
            win = 0
    #diagonales
    if cases[tailleCase/2, tailleCase/2] == cases[tailleCase + tailleCase/2, tailleCase + tailleCase/2] == cases[2*tailleCase + tailleCase/2, 2*tailleCase + tailleCase/2] == "O":
        Main["text"] = "Joueur 2 a gagne"
        win = 1
    elif cases[tailleCase/2, tailleCase/2] == cases[tailleCase + tailleCase/2, tailleCase + tailleCase/2] == cases[2*tailleCase + tailleCase/2, 2*tailleCase + tailleCase/2] == "X":
        Main["text"] = "Joueur 1 a gagne"
        win = 0

    elif cases[tailleCase/2, 2*tailleCase + tailleCase/2] == cases[tailleCase + tailleCase/2, tailleCase + tailleCase/2] == cases[2*tailleCase + tailleCase/2, tailleCase/2] == "O":
        Main["text"] = "Joueur 2 a gagne"
        win = 1
    elif cases[tailleCase/2, 2*tailleCase + tailleCase/2] == cases[tailleCase + tailleCase/2, tailleCase + tailleCase/2] == cases[2*tailleCase + tailleCase/2, tailleCase/2] == "X":
        Main["text"] = "Joueur 1 a gagne"
        win = 0

    for (x,y),symbole in cases.items(): #affichage des cases cliquees
        if symbole == "O":
            dessine.create_oval(x - (tailleCase/2) + 10, (y - tailleCase/2) + 10,\
            x + (tailleCase/2) - 10, y + (tailleCase/2) - 10, width = 4, outline = "red")

        elif symbole == "X":
            dessine.create_line(x - (tailleCase/2) + 10, (y - tailleCase/2) + 10,\
            x + (tailleCase/2) - 10, y + (tailleCase/2) - 10, width = 4, fill = "blue" )

            dessine.create_line(x - (tailleCase/2) + 10, (y + tailleCase/2) - 10,\
            x + (tailleCase/2) - 10, y - (tailleCase/2) + 10, width = 4, fill = "blue" )
        fenetre.update()

    if win != None or tour == 9: #si qqn a gagne ou si toutes les cases sont remplies, on arrete la partie
        if win != None: #si il y a quelqu'un qui a gagne
            partie[win] += 1 #on augmente le nombre de parties gagnees du joueur vainqueur
            score["text"] = "Joueur 1 : " + str(partie[0]) + " | " + "Joueur 2:" + str(partie[1]) #actualisation du scoreboard

        answer = askquestion("recommencer", 'Voulez-vous recommencer?\n Joueur1 : %d | Joueur2 : %d' % (partie[0], partie[1])) #on demandes à l'utilisateur si il veut recommencer
        if answer == "yes": #si l'utilisateur veut recommencer, on regenère l'affichage
            init(True)
        else:
            fenetre.quit() #sinon on quitte
    jouer()

def init(bis = False): #fonction pour initialiser
    global tour
    global joueur
    global dessine
    global cases
    global Main

    if bis == True: #si la partie a ete construite en recommencant, on reinitialise les affichages et on detruit le cnvas
        Main["text"] = ""
        dessine.destroy()

    tour = 0
    dessine = Canvas(fenetre, height = 3*tailleCase, width = 3*tailleCase, background = "lightgrey") #creation du canvas

    dessine.create_line(tailleCase, 0, tailleCase, tailleCase*3)        #grille de jeu
    dessine.create_line(2*tailleCase, 0, 2*tailleCase, 3*tailleCase)
    dessine.create_line(0, tailleCase, 3*tailleCase, tailleCase)
    dessine.create_line(0, 2*tailleCase, 3*tailleCase, 2*tailleCase)

    dessine.pack(side = LEFT)
    dessine.bind("<Button-1>", placer) #on associe la fonction placer à un clique gauche sur le canvas
#dictionnaire avec les coordonnees et les etats
    cases = {(tailleCase/2, tailleCase/2):"",(tailleCase/2, tailleCase + tailleCase/2):"",(tailleCase/2, 2*tailleCase + tailleCase/2):"",\
    (tailleCase + tailleCase/2, tailleCase/2):"",(tailleCase + tailleCase/2, tailleCase + tailleCase/2):"",(tailleCase + tailleCase/2, 2*tailleCase + tailleCase/2):"",\
    (2*tailleCase + tailleCase/2, tailleCase/2):"",(2*tailleCase + tailleCase/2, tailleCase + tailleCase/2):"",(2*tailleCase + tailleCase/2, 2*tailleCase + tailleCase/2):""} #(x,y):value

    fenetre.bind("<Return>", jouer) #on bind la touche entree pour commencer la partie
    fenetre.update()

fenetre = Tk() #fenetre
tailleCase = 100 #taille de la case, elle definit toutes les dimensions
fenetre.geometry(str(tailleCase*4+50) + "x" + str(tailleCase*3)) #recadrage de la fenetre principale,
partie = [0,0]

init() #on initialise l'interface

score = Label(fenetre, text = "") #label affichant le scoreboard
score.place(x = 3*tailleCase + 0.2*tailleCase, y = 0.3*tailleCase)

Main = Label(fenetre, text = "Appuyez sur Entree\n pour commencer") #label affichant des information et à quel joueur est-ce le tour
Main.place(x = 3*tailleCase + 0.2*tailleCase, y = tailleCase + 0.7*tailleCase)

fenetre.mainloop() #boucle principale
