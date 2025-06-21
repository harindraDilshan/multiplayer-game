import socket

'''TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

client.send('Hello from client'.encode())
print(client.recv(1024))
'''

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto('Hello from client'.encode(), ('127.0.0.1', 9999))

data, addr = client.recvfrom(1024)
print(data.decode())
