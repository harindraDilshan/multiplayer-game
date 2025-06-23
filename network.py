import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("192.168.8.102", 5555))
# client.send('Hello from client'.encode())

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.8.102"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect() # playe initial position
        
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)