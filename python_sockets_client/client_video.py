import socket
# HEADER = 64 #create a header of 64bytes its gonna be used in handle_client function for guessing how many bytes we are gonna recieve from the client
# PORT = 5050 #use this port so that you don't cause any conflict with programs that are using the network on your device
#
# #for encoding and decoding messages between server and the client
# FORMAT = 'utf-8'
#
# #this will handle the client disconnect process
DISCONNECT_MESSAGE = "!DISCONNECT"
#
# SERVER = "192.168.29.222"
# ADDR = (SERVER, PORT)
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)

class client_video_manager():
    def __init__(self, HEADER, PORT, FORMAT, SERVER):
        self.HEADER = HEADER #64
        self.PORT = PORT #5050
        self.FORMAT = FORMAT #'utf-8'
        self.SERVER = SERVER #"192.168.29.222"
    def connect_to_server(self):
        ADDR = (self.SERVER, self.PORT)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(60)   # set the timeout for the client of 5 seconds throw an exception if server is not found after 5 seconds
        global ERR
        ERR = False
        try:
            client.connect(ADDR)
            ERR = False
            return client
        except socket.error:
            print("Cannot find server on the network")
            print("make sure you are on the same network as your raspberry pi robot")
            ERR = True
            return ERR

    def send(self, msg, client_id):
        client = client_id
        message = msg.encode(self.FORMAT) #it will convert the messages from string to bytes format
        msg_length = len(message)
        if ERR == False: # this if statement will anly allow client to send message when it successfully connects to the server
            send_length = str(msg_length).encode(self.FORMAT)
            #now here we will make sure that our messages are 64 bytes long like the HEADER message
            #b' ' = byte spaces
            send_length += b' ' * (self.HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            #recieving message from the server testing ONLY
            #print(client.recv(800000).decode(self.FORMAT))

#declaring main function
def main():
    #testing client
    #getting client id on the local area network
    client_id = client_class.connect_to_server()
    client_class.send("e", client_id)
    client_class.send("!DISCONNECT", client_id)

if __name__ == '__main__':
    # client_manager(HEADER, PORT, FORMAT, SERVER)
    client_class = client_manager(128, 5051, 'utf-8', "192.168.29.235")
    main()

# #now here we are gonna send some messages to the server
# def send(msg):
#     message = msg.encode(FORMAT) #it will convert the messages from string to bytes format
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     #now here we will make sure that our messages are 64 bytes long like the HEADER message
#     #b' ' = byte spaces
#     send_length += b' ' * (HEADER - len(send_length))
#     client.send(send_length)
#     client.send(message)
#     #recieving message from the server testing ONLY
#     print(client.recv(800000).decode(FORMAT))

# send("MSI workstation says hello!")
# send("MSI workstation says I am testing sockets")
# send("MSI workstation says Sending message from client to the server")
# send(DISCONNECT_MESSAGE)
