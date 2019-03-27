import socket #imports
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
s.connect((socket.gethostname(), 1243)) #on lie l'adresse ip et le ports

while True:
    msg = s.recv(1000) #on cherche a recevoir un message

    print(pickle.loads(msg)) #on affiche le message après l'avoir désérialisé
