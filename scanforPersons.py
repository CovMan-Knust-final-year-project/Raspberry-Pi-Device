import socket
from FetchUserIdFromDatabase import *

def startServer():
    ip = "192.168.43.75" # IP of Raspberry Pi

    # start server
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, 8080))
    serv.listen(5)
    print("SERVER: started")

    while True:
        # establish connection
        conn, addr = serv.accept()
        from_client = ''
        print("SERVER: connection to Client established")

        while True:
            # receive data and print
            data = conn.recv(4096).decode()
            if not data: break
            from_client += data
            print("Recieved: " + from_client)

            # send message back to client
            msg = "Raspberry pi device"
            conn.send(msg.encode())

            #use the data gathered from the camera to fetch the details of the person
            FetchUserIdFromDatabase(from_client).fetchPersonId()

        # close connection and exit
        #conn.close()
        #break

if __name__ == '__main__':
    startServer()

