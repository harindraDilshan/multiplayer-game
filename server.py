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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0,0),(100,100)] # Player 1 staring pos and player 2 starting pos
def threaded_client(client, clientId):
    client.send(str.encode(f"{pos[clientId]}"))
    replay = ""
    while True:
        try:
            data = read_pos(client.recv(2048).decode())
            pos[clientId] = data

            if not data:
                print("Disconnected")
                break
            else:
                if clientId == 1:
                    replay = pos[0]
                else:
                    replay = pos[1]

                print("Recevied : ", data)
                print("Sending : ", replay)

            client.sendall(str.encode(make_pos(replay)))

        except:
            break
    
    print("Lost connection")
    client.close()

currentPlayer = 0
while True:
    client, addr = server.accept()
    print("Connected to : ", addr)

    start_new_thread(threaded_client, (client, currentPlayer))

    currentPlayer += 1
