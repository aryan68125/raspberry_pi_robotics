#!/usr/bin/env python
import socket
#threading is a way to create multiple threads in a single python program
import threading
import time
import get_router_assigned_ip_address

#this module handles the motor controller operations
from Motor_no_Ena import Motor
#############SETTINGS#################################
motor = Motor( 3, 5, 11, 7) #create motor object
######################################################

#ip address returned by the get_router_assigned_ip_address module
IP_ADDR = get_router_assigned_ip_address.addr
# print(IP_ADDR)

HEADER = 128 #create a header of 64bytes its gonna be used in handle_client function for guessing how many bytes we are gonna recieve from the client
PORT = 5050 #use this port so that you don't cause any conflict with programs that are using the network on your device
#SERVER = socket.gethostbyname(socket.gethostname()) #this will get the ipaddress of the computer this script is running on
SERVER = IP_ADDR

ADDR = (SERVER, PORT)

#for encoding and decoding messages between server and the client
FORMAT = 'utf-8'

#this will handle the client disconnect process
DISCONNECT_MESSAGE = "!DISCONNECT"

#create a socket that will open up the host device to other connections
# step 1 pick the PORT and pick the SERVER
# step 2 pick the socket
# step 3 bind the socket to that address

#create a new socket
#server = socket.socket(family of socket that we want, socket.SOCK_STREAM = streaming data through the sockets)
#INET means over the internet
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #this line allows the server to use the same Address otherwise it will throw an exception error address already in use
#now we will bind the socket to an address ADDR
server.bind(ADDR)

def handle_client(conn, addr):
    #this function will handle the communication between the client and the server
    #this function will run concurrently for each client
    print("[NEW CONNECTION] {} connected".format(addr))
    connected = True
    while connected:
        #wait to recieve information from the connected client
        #and when we recieve information from the client then we are going to do something with it
        #conn.recv(how many bytes we want to recieve)
        #in order to guess how many bytes the client is gonna send we need some kind of protocol
        #define a header of 64 bytes
        #the 1st message from the client is gonna be a header which will tell us the length of the message thats gonna come next Later we need to this on the client side also
        #we will not pass this line of code until we recieve a message from the client
        msg_length = conn.recv(HEADER).decode(FORMAT) #converting bytes into a string
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            #disconnect the client from the server if we recieve a disconnect message from the client
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print("[CLIENT LOGGED OUT] client left")
                print("connection closed")
                #sending message back to the client from this server
                conn.send("You disconnected from the server".encode(FORMAT))
            elif msg == "w":
                #call forward fnction from Motor.py module
                #forward(speed=0.5, t=0)
                motor.forward()
            elif msg == "s":
                #call reverse fnction from Motor.py module
                #reverse(speed=0.5, t=0)
                motor.reverse()
            elif msg == "a":
                #call left fnction from Motor.py module
                #left(speed=0.5, t=0)
                motor.left()
            elif msg == "d":
                #call right fnction from Motor.py module
                #right(speed=0.5, t=0)
                motor.right()
            elif msg == "b":
                motor.stop()

            #print(f"[{addr}] {msg}")
            #printing the messages recieved from the client
            print("[{}] {}".format(addr, msg))

            #sending message back to the client
            conn.send("Message reieved".encode(FORMAT))
    conn.close()

#start function is going to start the socket server for us
def start():
    #in this function we will write the code to allow our server to start listening for connections
    #and pass them to handle_client function which will run in our new thread
    server.listen()
    print("[LISTENING] Server is listening on ipaddress {}".format(SERVER))
    while True:
        #addr will store the ipaddress and port of the client
        #conn (Socket Object) will store an object that will allow us to send information back to the client
        conn, addr = server.accept()
        #start a new thread which is equal to handle_client function
        thread = threading.Thread(target=handle_client, args = (conn,addr))
        #start the thread
        thread.start()
        #print the active connections to the server
        #threading.activeCount() -1 tells us how many threads are currently active in this python process
        #the amount of threads will tell the number of clients because we are going to create a new thread for each client
        NumberOf_clients_connected = threading.activeCount() -1
        print("[ACTIVE CONNECTIONS] {}".format(NumberOf_clients_connected))


print("[STARTING] server is starting...")
start()
