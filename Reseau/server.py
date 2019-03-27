import socket #imports
import select
import pickle

players = {"gwenilapeuf": {"Tete": 20, "Morpion": 30}}

def process(msg):
    list = msg.split(" ")

    command = list[0]
    if command == "add":
        print(f"player {list[1]} scored {list[3]} in {list[2]}")
        return b"ok"

    if command == "list":
        return pickle.dumps(players)

Host = "localhost"
Port = 1243

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
s.bind((Host, Port)) #on lie l'adresse ip et le ports
s.listen(5) #nombre de connections simultanées entrantes acceptées
print(f"Server is listening port {Port}.")

launched = True
client_list = [] #liste des clients connectés
while launched == True:

    connection_asked, wlist, xlist = select.select([s], [], [], 0.05) #on rangerde les clients qui veullent commencer une connection

    for connection in connection_asked: #on accepte les connections et on stocke les sockets
        clientsocket, adress = connection.accept()
        print(f"connected to {adress[0]}")
        client_list.append(clientsocket)

    Client_To_Read = []

    try:
        Client_To_Read, wlist, xlist = select.select(client_list, [], [], 0.05) #si possible, on regarde les messages envoyés par les clients
    except select.error:
        pass
    else:
        for client in Client_To_Read: #pour chaque client, on observe le message envoyé
            try:
                msg = client.recv(1024).decode("utf-8")
                answer = process(msg)
                client.send(answer)
                if msg == "end":
                    launched = False
            except:
                print(f"lost connection")
                client_list.remove(client) #si on a une erreur, cela veut dire que le client s'est déconnecté, on le supprime

print("Ending connections")
for client in client_list: #fin des connections
    client.close()
s.close()
