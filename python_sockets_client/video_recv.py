#This is a client which will send the video feed to the host server from rpi -> to another computer where the server is Listening
import socket, cv2, pickle, struct, numpy

class video_reciever():
    def __init__(self,PORT,SERVER):
        self.PORT = PORT #5050
        self.SERVER = SERVER #"192.168.29.222"
    def connect_to_server(self):
        #create a socket for connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #get the ip address of another computer where the remote Tk software is installed
        #and send it to rpi via sockets which is used to send the commands fwd() ,reverse(), left and right to the robot

        #server_ip = "192.168.29.235"
        #print("server_ip_address = ",server_ip)
        #port = 9000
        Addr_server = (self.SERVER, self.PORT)
        client_socket.settimeout(20)
        global ERR
        ERR = False
        try:
            # client.connect(ADDR)
            client_socket.connect(Addr_server)
            ERR = False
            # return client
            return client_socket
        except socket.error:
            print("Cannot find server on the network")
            print("make sure you are on the same network as your raspberry pi robot")
            ERR = True
            return ERR
    def recv(self, client_socket):
        client_socket = client_socket
        #initialize the data variable as an empty string
        data = b""
        #Q means an unsigned long long integer that will take 8 bytes
        payload_size = struct.calcsize("Q")
        try:
             while True:
                 while len(data)<payload_size:
                     #here we will use 4kb buffer
                     packet = client_socket.recv(4*1024)
                     if not packet: break
                     data+=packet
                 #The first 8 bytes contains the size of the packed message so at here we will use data from 0 to payload_size
                 packed_msg_size = data[:payload_size]
                 #the rest of the data contains our video frame
                 data = data[payload_size:]
                 msg_size = struct.unpack("Q",packed_msg_size)[0]

                 while len(data)< msg_size:
                     data +=client_socket.recv(4*1024)
                 #here we are getting the packed message size and wun the while loop until we wecieve all the data from the client_socket for a frame
                 frame_data = data[:msg_size]
                 data = data[msg_size:]
                 frame = pickle.loads(frame_data)

                 #display video
                 cv2.imshow("Recieved", frame)
                 key = cv2.waitKey(1) & 0xFF #display
                 # if key == ord('q'):
                 #     cv2.destroyAllWindows() #break
                 #     client_socket.close()
                 # global key
                 # key = ""
                 #letter q to quit
                 # if key == 'camera_stop': break
             # client_socket.close()
        except Exception:
            client_socket.close()
