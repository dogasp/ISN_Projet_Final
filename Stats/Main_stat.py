from tkinter import *
import matplotlib
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import imshow, show, colorbar


import tkinter as tk
from tkinter import ttk
sys.path.append('../Reseau')
from Reseau.client import *

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Menu stats")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self, text="Graph 2 Page",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button5 = ttk.Button(self, text="Graph 3 Page",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        max_score = (25,24,23,21,17,15,10,7,4,2)
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
        ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5','G6', 'G7', 'G8', 'G9', 'G10'))
        ax.legend()
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        a = get_statistics()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph 3 Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        import matplotlib.pyplot as plt
        # Data
        x = []
        y = []

        for cle,valeur in a[1].items():
            for i in range(valeur):
                x.append(cle[0]+1)
                y.append(abs(cle[1]-20))

            print (cle, valeur)


        fig, ax = plt.subplots(figsize=(4, 4))
        fig.suptitle('Example Of Scatterplot')
        ax.set_xlim(1, 20)
        ax.set_ylim(1, 20)

                # Create the Scatter Plot
        ax.scatter(x, y, color="blue", s=500, alpha=0.1, linewidths=1)

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        a = get_statistics()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph 3 Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        b = np.zeros((20, 20), dtype = int)
        # Data
        x = []
        y = []

        for cle,valeur in a[1].items():
            #for i in range(valeur):
            b[abs(cle[1]-19)][cle[0]]+= valeur

        
        fig, ax = plt.subplots(figsize=(4, 4))
        im = plt.imshow(b) # later use a.set_data(new_data)

        ax.set_xlim(-0.5, 19.5)
        ax.set_ylim(-0.5, 19.5)

        plt.colorbar()
        canvas = FigureCanvasTkAgg(fig, self)
        #canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
