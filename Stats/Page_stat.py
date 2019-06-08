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
        self.frame_stat_main.pack(fill = BOTH)

        canvas = FigureCanvasTkAgg(fig, self.frame_stat_main)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.frame_stat_main)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.quitbutton = Button(self.frame_stat_main, text="Retour", fg="red", command=self.back_home )
        self.quitbutton.pack(side = RIGHT)

    def back_home(self):
        self.frame_stat_main.destroy()
            

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
    def __init__(self, master,x0,y0, x1,title, Legend1, Legend2):
        print(Legend2)
        ind = np.arange(len(x0))  # the x locations for the groups
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(7, 5))
        rects1 = ax.bar(ind - width/2, x0, width,
                        label=Legend1)
        rects2 = ax.bar(ind + width/2, x1, width,
                        label=Legend2)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title(title)
        ax.set_xticks(ind)
        plt.gca().xaxis.set_tick_params(labelsize = 8)

        ax.set_xticklabels(y0)
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
