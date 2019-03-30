import socket #imports
import select
import pickle
import os

Host = "192.168.1.30" #"90.91.3.228" #variables
Port = 1243

if os.path.isfile("./data"):
    with open("data", "rb") as f:
        players = pickle.load(f)
else:
    players = {} #dictionnaire des joueurs
players = {"Beta_Test": {"Tete": 10}}

def save():
    with open("data", "wb") as f:
        pickle.dump(players, f)

def process(msg): #fonction pour décider de ce qu'il faut retourner au client
    global players
    list = msg.split(" ") #on split

    command = list[0] #la commande est le premier mot, on le stocke pour plus de simplicité
    if command == "add": #si la commande est add, on ajoute le score
        print("player {} scored {} in {}".format(list[1], list[3], list[2]))
        try:
            if players[list[1]][list[2]] < float(list[3]): #si le score marqué est plus grand que le précédent, on le retiends
                players[list[1]][list[2]] = float(list[3])
        except:
            players[list[1]] = {"Tete": 0}   #création d'un nouveau joueur et ajout du score
            players[list[1]][list[2]] = float(list[3])
        save()
        return b"ok" #le retour n'est pas important

    if command == "list": #si c'est la liste, on sérialise le dictionnaire et on l'envois
        total_score = []
        for player in players.keys():
            sum = 0
            for jeu in players[player].values():
                sum += jeu
            total_score.append((player, sum))
        total_score.sort(key = lambda list: list[1], reverse = True)
        return pickle.dumps(total_score[:10])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
s.bind((Host, Port)) #on lie l'adresse ip et le ports
s.listen(5) #nombre de connections simultanées entrantes acceptées
print("Server is listening port {}.".format(Port))

launched = True
client_list = [] #liste des clients connectés
while launched == True: #tant que cette vairable est vraie, le serveur tourne

    connection_asked, wlist, xlist = select.select([s], [], [], 0.05) #on regarde les clients qui veullent commencer une connection

    for connection in connection_asked: #on accepte les connections et on stocke les sockets
        clientsocket, adress = connection.accept()
        print("connected to {}".format(adress[0]))
        client_list.append(clientsocket) #on ajoute les clients cceptés à la liste des clients

    Client_To_Read = []

    try:
        Client_To_Read, wlist, xlist = select.select(client_list, [], [], 0.05) #si possible, on regarde les messages envoyés par les clients
    except select.error:
        pass
    else:
        for client in Client_To_Read: #pour chaque client, on observe le message envoyé
            try: #on essaye de décoder le message
                msg = client.recv(1024).decode("utf-8")
                answer = process(msg) #on créé la réponse suivant la demande
                client.send(answer) #et on renvois cette réponse
                if msg == "end": #si un utilisateur envoie end , on stoppe le serveur
                    launched = False
            except: #si on ne peut pas lire le message, c'est que le socket n'est pas valide donc le client est déconnecté, on le supprime de la liste
                print("lost connection")
                client_list.remove(client) #si on a une erreur, cela veut dire que le client s'est déconnecté, on le supprime

print("Ending connections")
for client in client_list: #fin des connections
    client.close()
s.close()
save()
