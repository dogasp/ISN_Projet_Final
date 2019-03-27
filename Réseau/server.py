import socket #imports
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
s.bind((socket.gethostname(), 1243)) #on lie l'adresse ip et le ports
s.listen(5) #nombre de connections entrantes acceptées

while True: #boucle
    clientsocket, address = s.accept() #récupération des informations de connection
    print(f"Connection from {address} has been established.")

    d = {1:"hi", 2: "there"} #data a envoyer
    msg = pickle.dumps(d) #on le sérialise
    clientsocket.send(msg) #envoi de la data au client
