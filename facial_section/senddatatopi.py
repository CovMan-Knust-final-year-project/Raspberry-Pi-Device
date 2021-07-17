import socket


class senddatatoPi:
    def __init__(self, name):
        self.person_name = name
    
    def sendData(self):

        ip = "192.168.43.75" # IP of Raspberry Pi

        # connect to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, 8080))
        print("CLIENT: connected")

        # send person name to Pi
        msg = self.person_name
        client.send(msg.encode())

        # recive a message and print it
        from_server = client.recv(4096).decode()
        print("Recieved: " + from_server)

        # exit
        client.close()
