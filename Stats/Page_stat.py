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

class Graph_jeux_1_exe(App_stat):
    def __init__(self, master):
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect="equal"))


        def func(pct, allvals):
            absolute = int(pct/100.*np.sum(allvals))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(score_app, autopct=lambda pct: func(pct, score_app),
                                        textprops=dict(color="w"))

        ax.legend(wedges, name_game, title="Jeux",loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("Matplotlib bakery: A pie")
        super().__init__(master,fig)

class Graph_1_exe(App_stat):
    def __init__(self, master,max_score,players):

        score_moyen = (14,12,10,7,6,6,5,4,2,1)

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

class Graph_2_exe(App_stat):
    def __init__(self, master, user_name, grille):

        grille = np.zeros((20, 20), dtype = int)

        fig, ax = plt.subplots(figsize=(4, 4))
        im = plt.imshow(grille) # later use a.set_data(new_data)

        ax.set_xlim(-0.5, 19.5)
        ax.set_ylim(-0.5, 19.5)

        plt.colorbar()
        super().__init__(master,fig)


class Graph_3_exe(App_stat):
    def __init__(self, master,user_name, x,y):

        fig, ax = plt.subplots(figsize=(4, 4))
        fig.suptitle('Example Of Scatterplot')
        ax.set_xlim(1, 20)
        ax.set_ylim(1, 20)
        # Create the Scatter Plot
        ax.scatter(x, y, color="blue", s=500, alpha=0.1, linewidths=1)
        fig.tight_layout()
        super().__init__(master,fig)
