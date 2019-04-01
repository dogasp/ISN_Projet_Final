from tkinter import * #@UnusedWildImport
from tkinter.messagebox import *
from time import sleep
sys.path.append('../Reseau')
from Reseau.client import *
sys.path.append('../Scoreboard')
from Scoreboard.scoreboard import *

class snake:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x700")

def Snake():
    jeux = snake()

if __name__ == "__main__":
    Snake()
