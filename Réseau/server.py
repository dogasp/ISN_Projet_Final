import socket #imports
import select
import pickle

Host = "localhost"
Port = 1243

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket
s.bind((Host, Port)) #on lie l'adresse ip et le ports
s.listen(5) #nombre de connections simultanées entrantes acceptées
print(f"Server is listening port {Port}.")

launched = True
client_list = []
while launched == True:

    connection_asked, wlist, xlist = select.select([s], [], [], 0.05)

    for connection in connection_asked:
        clientsocket, adress = connection.accept()
        print(f"connected to {adress[0]}")
        client_list.append(clientsocket)

    Client_To_Read = []

    try:
        Client_To_Read, wlist, xlist = select.select(client_list, [], [], 0.05)
    except select.error:
        pass
    else:
        backup = Client_To_Read.copy()
        for client in Client_To_Read:
            try:
                msg = client.recv(1024).decode("utf-8")
                print(f"Get: {msg}")
                client.send(b"got it")
                if msg == "end":
                    launched = False
            except:
                print(f"lost connection")
                client_list.remove(client)

print("Ending connections")
for client in client_list:
    client.close()
s.close()
