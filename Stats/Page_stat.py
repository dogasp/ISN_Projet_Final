from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import imshow, show, colorbar
import numpy as np

sys.path.append('../Reseau')
from Reseau.client import *

class App_stat:
    def __init__(self, master, fig):
        self.frame_stat_main = Frame(master, width = 1020, height = 600)
        self.frame_stat_main.place(x = 0, y = 0)

        canvas = FigureCanvasTkAgg(fig, master)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, master)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.quitbutton = Button(master, text="Retour", fg="red", command=master.quit)
        self.quitbutton.place(x = 100, y = 50)

class Graph_1(App_stat):
    def __init__(self, master, user_name, grille):

        grille = np.zeros((20, 20), dtype = int)

        fig, ax = plt.subplots(figsize=(4, 4))
        im = plt.imshow(grille) # later use a.set_data(new_data)

        ax.set_xlim(-0.5, 19.5)
        ax.set_ylim(-0.5, 19.5)

        plt.colorbar()
        super().__init__(master,fig)


class Graph_2(App_stat):
    def __init__(self, master,user_name, x,y):

        fig, ax = plt.subplots(figsize=(4, 4))
        fig.suptitle('Example Of Scatterplot')
        ax.set_xlim(1, 20)
        ax.set_ylim(1, 20)
        # Create the Scatter Plot
        ax.scatter(x, y, color="blue", s=500, alpha=0.1, linewidths=1)
        fig.tight_layout()
        super().__init__(master,fig)

class Graph_3(App_stat):
    def __init__(self, master):

        
        score_moyen = (14,12,10,7,6,6,5,4,2,1)

        players = []
        for player in get_score_list():
            players.append(player[0])

        max_score = []
        for player in get_score_list():
            max_score.append(player[1])


        ind = np.arange(len(max_score))  # the x locations for the groups
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(7, 5))
        rects1 = ax.bar(ind - width/2, max_score, width,
                        label='Score max')
        rects2 = ax.bar(ind + width/2, score_moyen, width,
                        label='Score moyen')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title('Score max et moyenne des joueurs du Top 10')
        ax.set_xticks(ind)


        ax.set_xticklabels(players)
        ax.legend()
        fig.tight_layout()
        super().__init__(master,fig)
