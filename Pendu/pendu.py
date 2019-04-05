 from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *

class pendu:
    def __init__(self, user):
        self.user = user
        self.score = 0
        with open("Pendu/ressources/liste_francais.txt") as f:
            sefl.data = f.read().lower().split("\n")
        



def Pendu(user):
    partie = pendu(user)
    return partie.score