from tkinter import *
sys.path.append('../')
from Reseau.client import *

class Scoreboard:
    def __init__(self, parent, jeux):

        TopFrame = Frame(parent, width = 550, height = 425, relief = GROOVE)
        TopFrame.place(x = 60, y = 45)

        TopFrame.after(500,lambda: ranking_game.place(x = 120, y= 20 ))
        ranking_game = Label(TopFrame, text = 'Classement du jeu', font = ("Berlin Sans FB", 35), relief = GROOVE) #,command =Ranking

        players = get__game_score_list(jeux)
        Label(TopFrame, text = "Ranking" + " "*15 + "Name" + " "*35 + "Score" ).place(x = 120, y = 80)

        for i in range(len(players)):
            Label(TopFrame,text = "#{} : {}".format(i+1, players[i][0]),font = ("Helvetica", 15)).place(x = 120, y = 100 +i*25)
            Label(TopFrame, text = "{}".format(str(int(players[i][1]))),font = ("Helvetica", 15)).place(x = 350, y = 100 +i*25)
        for i in range(10-len(players)):
            Label(TopFrame,text = "#{} :".format(i+1+len(players)),font = ("Helvetica", 15)).place(x = 120, y = 100 + 25*len(players) +i*25)

        Bouton_continue = Button(TopFrame, text = 'Continue...',command = quit_ranking)
        TopFrame.after(2000,lambda: Bouton_continue.place(x = 300,y = 420 ))

def quit_ranking():
    show_rules.destroy()
    show_rules.quit()
