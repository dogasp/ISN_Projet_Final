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
        self.frame_stat_main = Frame(master)
        self.frame_stat_main.pack(fill = BOTH)

        self.quitbutton = Button(self.frame_stat_main, text="Quitter", fg="red", command=self.back_home )
        self.quitbutton.pack(side = TOP)


        canvas = FigureCanvasTkAgg(fig, self.frame_stat_main)
        toolbar = NavigationToolbar2Tk(canvas, self.frame_stat_main)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        canvas._tkcanvas.pack(expand=True)

    def back_home(self):
        self.frame_stat_main.destroy()


class Graph_1_exe(App_stat):
    def __init__(self, master,user_name,x0,y0, x1,title, Legend1, Legend2,name_y_axe):
        ind = np.arange(len(x0))  # the x locations for the groups
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots(figsize=(7, 5))
        if x1 == []:
            rects1 = ax.bar(ind, x0, width,
                            label=Legend1)

        else:
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
    def __init__(self, master, user_name, x0, title,Legend1): #, user_name, grille)

        grille = np.zeros((20, 20), dtype = int)
        print(x0)
        for elt in x0:
            grille[abs(elt[1]-19),abs(elt[0])] += x0[elt]

        fig, ax = plt.subplots(figsize=(5, 5))
        im = plt.imshow(grille) # later use a.set_data(new_data)
        ax.set_xlim(-0.5, 19.5)
        ax.set_ylim(-0.5, 19.5)
        fig.suptitle(title)
        cbar = plt.colorbar()
        cbar.set_label(Legend1)
        super().__init__(master,fig)


class Graph_3_exe(App_stat):
    def __init__(self, master,user_name, x0,title,Legend1):

        x =[]
        y =[]
        print(x0)
        for elt in x0:
            for elt2 in range(x0[elt]):
                x.append(elt[0])
                y.append(abs(elt[1]-19))

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-0.25, 19.25)
        ax.set_ylim(-0.25, 19.25)
        fig.suptitle('Example Of Scatterplot')
        # Create the Scatter Plot
        ax.scatter(x, y, color="blue", s=500, alpha=0.1, linewidths=1)
        #fig.tight_layout()
        super().__init__(master,fig)


class Graph_4_exe(App_stat):
    def __init__(self, master,user_name,score_app,game, x1,title,title2, Legend1, Legend2,name_y_axe):
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect="equal"))
        explode = []

        for score in score_app:
            explode.append(score/40000)

        def func(pct, score_app):
            absolute = int(pct/100*sum(score_app))
            return "{:.1f}%\n({:d} pts)".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(score_app, explode=explode, labels=game, autopct=lambda pct: func(pct, score_app),
                colors = ['red', 'green', 'yellow', 'blue', 'orange', 'pink', 'lightgrey','brown','purple'],pctdistance = 0.7, labeldistance = 1.2,shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        ax.legend(wedges, game, title=title2,loc="center right", bbox_to_anchor=(0.6, 0, 0.5, 0.5))

        plt.setp(autotexts, size=7)

        ax.set_title(title)
        super().__init__(master,fig)
