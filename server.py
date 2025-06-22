import socket
from _thread import *
import sys

server_ip = "192.168.8.102"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((server_ip, port))
except socket.error as e:
    str(e)

server.listen(2)
print("Waiting For a Connection, Server Started")

def threaded_client(client):
    client.send(str.encode("Connected"))
    replay = ""
    while True:
        try:
            data = client.recv(2048)
            replay = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recevied : ", replay)
                print("Sending : ", replay)

            client.sendall(str.encode(replay))

        except:
            break
    
    print("Lost connection")
    client.close()

while True:
    client, addr = server.accept()
    print("Connected to : ", addr)

    start_new_thread(threaded_client, (client, ))
