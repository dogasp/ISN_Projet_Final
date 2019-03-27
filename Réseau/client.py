import socket #imports
import pickle

Host = "localhost"
Port = 1243

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
s.connect((Host, Port)) #on lie l'adresse ip et le ports

msg_To_send = b""
while msg_To_send != b"end":
    msg_To_send = input("> ").encode("utf-8")
    s.send(msg_To_send)
    msg_Recived = s.recv(1024)
    print("server response: " + msg_Recived.decode("utf-8"))

print("ending connections")
s.close()



#msg = s.recv(1000) #on cherche a recevoir un message

#print(pickle.loads(msg)) #on affiche le message après l'avoir désérialisé
#https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
