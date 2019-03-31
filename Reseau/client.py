import socket #imports
import pickle

Host = "90.91.3.228" #création des variables
Port = 1243

def push_score(pseudo, game, score):
    """pour ajouter un score après une partie """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
    s.connect((Host, Port)) #on lie l'adresse ip et le port
    msg_To_send = "add {} {} {}".format(pseudo, game, score) #on envois la commande pour ajouter la partie actuelle
    s.send(msg_To_send.encode())
    response = s.recv(1024) #la réponse n'est pas utile mais il y en a une
    s.close()

def get_score_list():
    """ récupérer le scoreboard"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
    s.connect((Host, Port)) #on lie l'adresse ip et le port
    s.send(b"list") #on demande la liste
    response = s.recv(1024)
    response = pickle.loads(response) #on désérialise la réponse pour récupérer un dictionnaire
    s.close()
    return response #on renvois le scoreboard

def get_game_score_list(game):
    """ récupérer le scoreboard pour un jeu spécifique"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
    s.connect((Host, Port)) #on lie l'adresse ip et le port
    s.send("game_list {}".format(game).encode("utf-8")) #on demande la liste
    response = s.recv(1024)
    response = pickle.loads(response) #on désérialise la réponse pour récupérer un dictionnaire
    s.close()
    return response #on renvois le scoreboard

def get_player_score(User_name):
    """récupération des scores d'un joueur"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
    s.connect((Host, Port)) #on lie l'adresse ip et le port
    s.send("player_score {}".format(User_name).encode("utf-8")) #on demande la liste
    response = s.recv(1024)
    response = pickle.loads(response) #on désérialise la réponse pour récupérer un dictionnaire
    s.close()
    return response #on renvois le scoreboard
#https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
