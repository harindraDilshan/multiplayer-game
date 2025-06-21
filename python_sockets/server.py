import socket

''' TCP

First we want to define sockets in python.
What are the family of sockets. For example Internet socket, Blutooth sockets, etc.
Type of the socket means Connection is TCP or UDP.
server = socket.socket(Define family of sockets, Type of the socket. Connection oriented or connection less)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM <-- TCP)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Buind the connection

if this is in server ip_address will be private ip address of the searver or 0.0.0.0 
server.bind((ip_address, port number))

server.bind(("0.0.0.0", 9999))

# server.listen(number of connections)

server.listen(5)

while True:
    client, arr = server.accept()
    print(client.recv(1024).decode())
    client.send('Hello from server'. encode())

'''



server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 9999))

while True:
    data, addr = server.recvfrom(1024)
    print(data.decode())
    server.sendto('Hello from server'. encode(), addr)
