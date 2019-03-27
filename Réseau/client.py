import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

while True:
    new_msg = True
    while True:
        msg = s.recv(1000)

        print(pickle.loads(msg))
