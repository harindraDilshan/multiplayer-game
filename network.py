import socket
import pickle
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("192.168.8.102", 5555))
# client.send('Hello from client'.encode())

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.8.102"
        self.port = 5557
        self.addr = (self.server, self.port)
        self.p = self.connect() # playe initial position
        
    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)