from tkinter import *
from Reseau.client import *
from tkinter import font
sys.path.append('../')
from Reseau.client import *
from Tete_chercheuse.tete_chercheuse import *
from Snake.Snake_main import *
from Fantome.Fantome_main import *
from Minesweeper.minesweeper import *
from Pendu.pendu import *
from Tetris.tetris import *
from Pong.Pong_main import*

class BoutonS: #classe pour gérer les boutons interactifs
    def __init__(self, x, y, jeux, run): # a besoin de ligne, colone, ne nom du jeux et la commande our executer le jeu
        self.image = PhotoImage(file = "thumbnail/" + jeux + ".png") #on charge l'immage correspondante au jeu
        self.button = Button(Frame_main, image = self.image, cursor ='hand2',  command = self.command) #création du boutton
        self.button.grid(row = x, column = y)
        self.jeux = jeux
        self.run = run

    def command(self): #fonction executée lors du clique sur le boutton
        global label_pseudo, label_score, score
        root_main.withdraw() #on masque l'interface principale
        result = self.run(User_name) #on execute le jeu
        push_score(User_name, self.jeux, result) #on envois au serveur le score de la partie
        root_main.deiconify() #on fait réapparaite la fenetre principale

        for label in label_score:
            label.destroy()
        for label in label_pseudo:
            label.destroy()

        score = get_score_list()

        label_pseudo = []
        label_score = []
        for i in range(len(score)): #pour chaque éléments de la liste recue, on affiche le pseudo et le score
            label_pseudo.append(Label(Frame_ranking,text = "#{} :       {}".format(i+1, score[i][0]),font = ("Helvetica", 8)))
            label_pseudo[-1].place(x = 4, y = 75 +i*20)
            label_score.append(Label(Frame_ranking, text = "{}".format(str(int(score[i][1]))),font = ("Helvetica", 8)))
            label_score[-1].place(x = 160, y = 75 +i*20)

        for i in range(10-len(score)): #si jamais la liste est plus petite que 10, on affiche des emplacements vides
            label_pseudo.append(Label(Frame_ranking,text = "#{} :".format(i+1+len(score)),font = ("Helvetica", 8)))
            label_pseudo[-1].place(x = 4, y = 75 + 20*len(score) +i*20)

User_name = "Unknown"

with open('Data/mots.txt', 'r') as file:
    mots = file.read()
    mots_interdits = mots.split("\n")

def valider(event = None):
    global User_name
    temp = entry.get().replace(" ", "_")
    if temp == "" or len(temp) > 20:
        alert.place(x = 50, y = 100)
        return
    for elt in mots_interdits[:-1]:
        if elt in temp.lower():
            alert.place(x = 50, y = 100)
            return
    User_name = temp
    root_user.destroy()
    root_user.quit()

root_user = Tk()
root_user.geometry("300x120")
root_user.bind("<Return>", valider)
root_user.focus_force()

Label(root_user, text = "Entre un pseudo pour jouer").place(x = 100, y = 30)

entry = Entry(root_user)
entry.place(x = 25, y = 80)
entry.focus()

alert = Label(root_user, text = "Nom invalide", fg = "red")

confirm = Button(root_user, text = "valider",cursor ='hand2', command = valider)
confirm.place(x = 225, y = 80)

root_user.mainloop()

root_main = Tk()
root_main.geometry('1000x600')
root_main.title("Menu")
root_main.focus_force()
#########################-----Création de la forme de la page----------------------#######################################
Frame_top = Frame(root_main, bg ='pink') #création des pannels
Frame_top.pack(ipadx = 1000, ipady =50, side = TOP)

Frame_left = Frame(root_main, bg ='yellow')
Frame_left.pack(ipadx = 100, ipady =500,side = LEFT)

Frame_down = Frame(root_main, bg ='black')
Frame_down.pack(ipadx = 900, ipady = 20,side = BOTTOM)

image_de_fond = PhotoImage(file = "thumbnail/image_de_fond.png")

Frame_main = Canvas(root_main,borderwidth=2, relief=GROOVE)
Frame_main.pack(ipadx = 900, ipady =530,side = BOTTOM)
Frame_main.create_image(450,265, image = image_de_fond)


Frame_ranking = Frame(Frame_left, width = 196 , height =280 , relief = GROOVE)
Frame_ranking.place(x = 2, y = 70)


score = get_score_list() #récupération du scoreboard

#############---------Création des labels et autres au contour du Frame_main-------#########################

Title_main = Label(Frame_top, text = 'La Caverne Aux Jeux',font = ("Berlin Sans FB", 45), relief = GROOVE)
Title_main.place(x = 250, y = 10)

Title_ranking = Label(Frame_ranking, text = 'Classements',font = ("Berlin Sans FB", 20), relief = GROOVE)
Title_ranking.place(x = 27, y = 5)

################---------Création du Classement-----------------------------################################
Label(Frame_ranking, text = "Rang" + " "*8 + "Nom" + " "*24 + "Score  " ,font = ("Helvetica",9), relief = GROOVE).place(x = 2, y = 50) #légende
label_pseudo = []
label_score = []
for i in range(len(score)): #pour chaque éléments de la liste recue, on affiche le pseudo et le score
    label_pseudo.append(Label(Frame_ranking,text = "#{} :       {}".format(i+1, score[i][0]),font = ("Helvetica", 8)))
    label_pseudo[-1].place(x = 4, y = 75 +i*20)
    label_score.append(Label(Frame_ranking, text = "{}".format(str(int(score[i][1]))),font = ("Helvetica", 8)))
    label_score[-1].place(x = 160, y = 75 +i*20)

for i in range(10-len(score)): #si jamais la liste est plus petite que 10, on affiche des emplacements vides
    label_pseudo.append(Label(Frame_ranking,text = "#{} :".format(i+1+len(score)),font = ("Helvetica", 8)))
    label_pseudo[-1].place(x = 4, y = 75 + 20*len(score) +i*20)


#############----------Création du tableau et des Labels du Frame_main--------------#################################

nom_de_jeux = ["Tête Chercheuse", "Snake", "Pong", "Space Invaders", "Tetris", "Tom & Jerry", "Demineur", "Pendu"]

for i in range(9):
    Frame_main.rowconfigure(i, weight = 1)
    Frame_main.columnconfigure(i ,weight =1)

Label_list0= Label(Frame_main, text = nom_de_jeux[0],font = ("Berlin Sans FB", 14), relief = GROOVE) #labels
Label_list1= Label(Frame_main, text = nom_de_jeux[1],font = ("Berlin Sans FB", 14), relief = GROOVE)
Label_list2= Label(Frame_main, text = nom_de_jeux[2],font = ("Berlin Sans FB", 14), relief = GROOVE)
Label_list3= Label(Frame_main, text = nom_de_jeux[3],font = ("Berlin Sans FB", 14), relief = GROOVE)
Label_list4= Label(Frame_main, text = nom_de_jeux[4],font = ("Berlin Sans FB", 14), relief = GROOVE)
Label_list5= Label(Frame_main, text = nom_de_jeux[5],font = ("Berlin Sans FB", 14), relief = GROOVE)
Label_list6= Label(Frame_main, text = nom_de_jeux[6],font = ("Berlin Sans FB", 14), relief = GROOVE)
Label_list7= Label(Frame_main, text = nom_de_jeux[7],font = ("Berlin Sans FB", 14), relief = GROOVE)

Label_list0.grid(row = 1, column = 1)
Label_list1.grid(row = 1, column = 3)
Label_list2.grid(row = 1, column = 5)
Label_list3.grid(row = 1, column = 7)
Label_list4.grid(row = 4, column = 1)
Label_list5.grid(row = 4, column = 3)
Label_list6.grid(row = 4, column = 5)
Label_list7.grid(row = 4, column = 7)


bouton_0 = BoutonS(2, 1, "Tete", Tete)
bouton_1 = BoutonS(2, 3, "Snake", Snake)
bouton_2 = BoutonS(5, 3, "Ghost", Ghost)
bouton_3 = BoutonS(5, 5, "Minesweeper", Minesweeper)
bouton_4 = BoutonS(5, 7, "Pendu", Pendu)
bouton_5 = BoutonS(5, 1, "Tetris", Tetris)
bouton_6 = BoutonS(2, 5, "Pong", Pong)

root_main.mainloop()
