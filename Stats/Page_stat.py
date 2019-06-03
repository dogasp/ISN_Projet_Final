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

class App_stat:

    def __init__(self, master):

        global frame
        frame = Frame(master)
        frame.pack(side=TOP)

        self.quitbutton = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quitbutton.grid(row=4,column=0,sticky=W)

        self.hi_there = Button(frame, text="LOAD",command=self.loadfile)
        self.hi_there.grid(row=0,column=0,sticky=W)

        self.cutbutton = Button(frame, text="CUT", fg="purple",command=self.cut)
        self.cutbutton.grid(row=1,column=0,sticky=W)

        global canvas, ax, f

        f = Figure(figsize=(20,4))
        ax = f.add_subplot(111)
        ax.set_xlabel('Time(s)',fontsize=20)
        ax.set_ylabel('Current(nA)',fontsize=20)
        canvas = FigureCanvasTkAgg(f, master=root)
        #canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)

        toolbar1 = NavigationToolbar2Tk( canvas, root )
        toolbar1.update()
        f.tight_layout()


    def loadfile(self):
        ax.clear()
        self.data=np.random.rand(1000)
        self.t=np.arange(0,len(self.data))
        ##############################################plot data
        self.baseline=np.median(self.data)
        self.var=2*(np.std(self.data))
        ax.plot(self.t,self.data,'b')

        ax.set_xlabel('Time(s)',fontsize=20)
        ax.set_ylabel('Current(nA)',fontsize=20)
        ax.axhline(linewidth=2, y=self.baseline, color='g')
        ax.set_xlabel('Time(s)',fontsize=20)
        ax.set_ylabel('Current(nA)',fontsize=20)
        canvas.draw()

    def cut(self):
        pts=np.array(f.ginput(2))
        pts=pts[:,0]
        print (pts)
        self.data=np.delete(self.data,pts)

        ax.clear()
        self.baseline=np.median(self.data)
        self.t=np.arange(0,len(self.data))
        ax.plot(self.t,self.data,'b')
        ax.axhline(linewidth=2, y=self.baseline, color='g')
        canvas.draw()




root = Tk()

app = App_stat(root)

root.mainloop()
root.destroy()
