#this code for the server which will be responsible for recieving video packets sent from raspberry pi so that we can stream videos from raspberry pi to our application
import socket
import cv2
import pickle
import struct
import get_router_assigned_ip_address

#creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#this line allows the server to use the same Address otherwise it will throw an exception error address already in use
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name = socket.gethostname()
#get Host Ip address assgined to host by a router in the local area network over wifi
IP_ADDR = get_router_assigned_ip_address.Addr
host_ip = socket.gethostbyname(IP_ADDR)
print("[HOST IP] ", host_ip)
port = 9000
socket_address = (host_ip, port)

#Socket Binding code
server_socket.bind(socket_address)

#code for socket to listen on the incoming packets of video feed sent by the raspberry pi
server_socket.listen(5)
print("[Video Stream Server Starting] Listening At....",socket_address)

#Accepting video data stream packets sent by raspberry pi to the server side
while True:
    client_socket, addr = server_socket.accept()
    print("[Got Connection From] ",addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            #Q means an unsigned long long integer that will take 8 bytes
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF #display
            if key == ord('q'):
                client_socket.close()
