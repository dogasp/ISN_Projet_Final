from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from Tete_chercheuse.data import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *
from Tetris.tiles import *
from random import choice, randint

class tetris:
    def __init__(self, user):
        self.user = user
        self.score = 0

def Tetris(user):
    jeux = tetris(user)
    return jeux.score