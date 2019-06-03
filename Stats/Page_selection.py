from tkinter import *

sys.path.append("../Reseau")
from Stats.Page_stat import *
from Reseau.client import *

class Stats:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.protocol()

        self.Gros_Titre_Sa_Mere = Label(self.root, text = "Page de sélection des graphs à afficher")
        self.Gros_Titre_Sa_Mere.place(x = 200, y = 20)

        app = Graph_3(self.root)

        self.root.mainloop()

a = get_statistics()

print(a)
"""
players = []
for player in get_score_list():
    players.append(player[0])

max_score = []
for player in get_score_list():
    max_score.append(player[1])




for cle,valeur in a[1].items():
    for i in range(valeur):
        x.append(cle[0]+1)
        y.append(abs(cle[1]-20))

for cle,valeur in a[0].items():
    print(cle, valeur)

print(x)
print(y)
"""
