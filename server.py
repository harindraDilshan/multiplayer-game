import socket
from _thread import *
import sys
from player import *
import pickle
from constants import *
from Ball import *
import time

def server():
    server_ip = "192.168.8.102"
    port = 5557

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((server_ip, port))
    except socket.error as e:
        str(e)

    server.listen(2)
    print("Waiting For a Connection, Server Started")


    player_1_pos = (0, int(SCREEN_HEIGHT/2))
    player_2_pos = (SCREEN_WIDTH - 50, int(SCREEN_HEIGHT/2))

    players = [Player(player_1_pos[0], player_1_pos[1], 10, 50, (255, 0, 0), 1), Player(player_2_pos[0], player_1_pos[1], 10, 50, (0, 255, 0), 2)] # Player 1 staring pos and player 2 starting pos
    b = Ball(100, 100, 5, (255, 0, 0))

    def threaded_ball():
        while True:
            b.move(players)
            time.sleep(1/60) # TODO: this should be same as FPS in client side.

    def threaded_client(client, playerId):
        client.send(pickle.dumps(players[playerId]))
        replay = ()
        while True:
            try:
                data = pickle.loads(client.recv(2048))
                players[playerId] = data

                if not data:
                    print("Disconnected")
                    break
                else:
                    # b.move(players)
                    if playerId == 1:
                        replay = players[0], b
                    else:
                        replay = players[1], b

                    print("Recevied : ", data)
                    print("Sending : ", replay)

                    # b.move(b) # x-speed and y-speed

                client.sendall(pickle.dumps(replay)) # I want to send ball object as well

            except:
                break
        
        print("Lost connection")
        client.close()

    currentPlayer = 0
    while True:
        client, addr = server.accept()
        print("Connected to : ", addr)

        if currentPlayer < 2:
            start_new_thread(threaded_client, (client, currentPlayer))
            start_new_thread(threaded_ball, ())
        else:
            print("Room Full")

        currentPlayer += 1
