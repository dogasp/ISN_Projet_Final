import socket #imports
import pickle

Host = "localhost"
Port = 1243


"""
msg_To_send = b""
while msg_To_send != b"end": #tant qu'on a des messages a envoyer
    msg_To_send = input("> ").encode("utf-8")
    s.send(msg_To_send)
    msg_Recived = s.recv(1024)
    print("server response: " + msg_Recived.decode("utf-8"))

print("ending connections")
s.close()

msg = s.recv(1000) #on cherche a recevoir un message

print(pickle.loads(msg)) #on affiche le message après l'avoir désérialisé
https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/"""


def push_score(pseudo, game, score):
    """pour ajouter un score après une partie """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
    s.connect((Host, Port)) #on lie l'adresse ip et le port
    msg_To_send = "add {} {} {}".format(pseudo, game, score)
    s.send(msg_To_send.encode())
    response = s.recv(1024)
    s.close()

def get_score_list():
    """ récupérer le scoreboard"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
    s.connect((Host, Port)) #on lie l'adresse ip et le port
    s.send(b"list")
    response = s.recv(1024)
    response = pickle.loads(response)
    s.close()
    return response
