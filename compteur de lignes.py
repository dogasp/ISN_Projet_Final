from os import listdir
from os.path import isfile, join
path = "./"
fichiers = listdir(path)

lignes = 0
total = 0
for file in fichiers:
    if isfile(join(path, file)):
        if file.split(".")[1] == "py" and file != "compteur de lignes.py":
            with open(join(path,file), "r") as fichier:
                temp = fichier.readlines()
                for i in temp:
                    lignes += 1
                print(file,  lignes) 
                total += lignes
                lignes = 0
    else:
        for under in listdir(join(path,file)):
            if len(under.split(".")) > 1 and under.split(".")[1] == "py" and under != "morpion.py":
                with open(join(path,file,under), "r") as fichier:
                    temp = fichier.readlines()
                    for i in temp:
                        lignes += 1
                    print(under, lignes)
                    total += lignes
                    lignes = 0
print("total de lignes = ", total)
input()
