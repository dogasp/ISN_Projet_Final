from tkinter import *
from head import *
from maps import *


head = Head(1, 1, 1)
head.move()
head.rotate()
head.move()




root = Tk()

root.geometry('700x500')


Frame_right = Frame(root, width = 500, height = 500)
Frame_left = Frame(root, width = 200, height = 500, bg = 'red')

Table = Canvas(Frame_right,width = 500, height = 500, bg ='green')

nbcases_width = 10
nbcases_height = 10

Frame_right.pack(side = RIGHT)
Frame_left.pack(side = LEFT)
Table.pack(fill = BOTH)

for i in range(nbcases_width):
    Table.create_line((500/nbcases_len)*i,0,(500/nbcases_len)*i,500)

for j in range(nbcases_height):
    Table.create_line(0,(500/nbcases_width)*j,500,(500/nbcases_width)*j)

Table.create_rectangle(2,2,500,500)



















root.mainloop()
