from tkinter import *
#import messagebox library from tkinter
from tkinter import messagebox

#import client_manager class from client.py
from client import client_manager
from client_video import client_video_manager
from video_recv import video_reciever
# import threading
import multiprocessing
import webbrowser

#import dev_info.py module in the module which contains info about the developer
import dev_info

#if the import of ImageTk does't work then
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
#this module allows us to use png and jpg images in our program
from PIL import ImageTk,Image

main = Tk()

###################SETTING UP MAIN WINDOW SIZE AND TITLE OF THE APPLICATION##########################
main.title("Raspberry pi Robot Controller Application")
main.geometry("1024x142+0+0")

# setting up the minimum size and maximum size for the application's main window
# set minimum window size value
main.minsize(1024, 142)

# set maximum window size value
main.maxsize(1024, 142)
###########################################################################################################################################

##############################DETECTING KEY PRESSES USING tKINTER KEY BOARD INPUTS##########################################################
#output window UI element for arrow key press commands send to the server
#frame that will contain UI elements related to command sent to raspberry pi and display it in the output box
Display_frame_background = "#155263"
Display_frame = LabelFrame(main,text="Output",font = ("times new roman",20,"bold"),padx=5,pady=5, bd=5, relief=RIDGE,fg = "white", bg = Display_frame_background)
Display_frame.place(x=390,y=0,width= 635, height= 80)
Label(Display_frame, text = "Command sent to the server : ", bg = Display_frame_background, font = ("times new roman",15,"bold"), fg="white").grid(row=0,column=0)
output_text = StringVar()
output_field = Entry(Display_frame, font = ("times new roman",15,"bold"),bg="#f6e4ad", fg="black", textvariable = output_text)
output_field.grid(row=0,column=1,sticky = W+E)

#this function will show developer information in a new window
def openNewWindow():
    #show developer information
    print("developer info")
    # Toplevel object which will
    # be treated as a new window
    developer_window = Toplevel(main)

    # sets the title of the
    # Toplevel widget
    developer_window.title("Developer Info")

    # sets the geometry of toplevel
    developer_window.geometry("530x500")

    # setting up the minimum size and maximum size for the application's developer window
    # set minimum window size value
    developer_window.minsize(628, 500)

    # set maximum window size value
    developer_window.maxsize(628, 500)

########################UI ELEMENTS OF DEV INFO WINDOW###########################################################################################################################
    #background color for Menu_frame
    Developer_frame_backgrount_color = "#3e4a61"
    Developer_frame = LabelFrame(developer_window,text="Developer Information",bd=7,relief=GROOVE,font=("times new roman", 15, "bold"),fg = "white", bg = Developer_frame_backgrount_color)
    #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
    # relwidth is the welative width of the frame relative to the other ui components of the application
    Developer_frame.place(x=0,y=0,width=628,height=500)

    #developer info is shown here using Labels
    #name
    Dev_name_Label = Label(Developer_frame,text="Name:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=0,column=0,padx=5,pady=5,sticky="w")
    Dev_name_aditya_Label = Label(Developer_frame,text=dev_info.Name,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=0,column=1,padx=5,pady=5,sticky="w")
    #roll number
    Roll_Number_Label = Label(Developer_frame,text="Roll no:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=1,column=0,padx=5,pady=5,sticky="w")
    Roll_number_Label = Label(Developer_frame,text=dev_info.Roll_Number,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=1,column=1,padx=5,pady=5,sticky="w")
    #College_code
    College_code_Label = Label(Developer_frame,text="College code:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=2,column=0,padx=5,pady=5,sticky="w")
    College_code_Label = Label(Developer_frame,text=dev_info.College_code,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=2,column=1,padx=5,pady=5,sticky="w")
    #Branch
    Branch_Label = Label(Developer_frame,text="Branch:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=3,column=0,padx=5,pady=5,sticky="w")
    Branch_2_Label = Label(Developer_frame,text=dev_info.Branch,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=3,column=1,padx=5,pady=5,sticky="w")
    #Course
    Course_Label = Label(Developer_frame,text="Course:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=4,column=0,padx=5,pady=5,sticky="w")
    Course_2_Label = Label(Developer_frame,text=dev_info.Course,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=4,column=1,padx=5,pady=5,sticky="w")

    #import image from the directory
    #make canvas and img varables into global variable otherwise the image will not show up in the application
    global canvas
    global img
    canvas = Canvas(Developer_frame, width =229, height = 355)
    canvas.grid(row=0,column=2,rowspan=5)
    # #if the import of ImageTk does't work then
    # #type in terminal :- for python3.5 and abclient_video_managerove--> sudo apt-get install python3-pil python3-pil.imagetk
    # #this module allows us to use png and jpg images in our program
    # from PIL import ImageTk,Image before using ImageIk
    img = ImageTk.PhotoImage(Image.open("dev.png"))
    #canvas.create_image(x = 2,y = 2, anchor=NW, image=img)
    #canvas will start drawing the image from the coordinates 2,2
    canvas.create_image(2, 2, anchor=NW, image=img)

    #Dev_info social media Links
    Dev_Search_Url = "https://radiant-bastion-62859.herokuapp.com/profile/3947f970-07f0-4863-bdf6-0d247c0b2e82/"
    GitHub_Url = "https://github.com/aryan68125?tab=repositories"
    Linked_in_Url = "https://www.linkedin.com/in/aditya-kumar-74700520a/"
    new = 1
    def openDevSearch():
        webbrowser.open(Dev_Search_Url,new=new)
    def openGithub():
        webbrowser.open(GitHub_Url,new=new)
    def openLinkedin():
        webbrowser.open(Linked_in_Url,new=new)

    social_media_Label = Label(Developer_frame,text="Social Media Links:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=5,column=0,padx=5,pady=5,sticky="w")
    Open_devsearch = Button(Developer_frame, text = "Dev search",command=openDevSearch)
    Open_devsearch.grid(row=6,column=0,padx=5,pady=5,sticky="w")
    Open_github = Button(Developer_frame, text = "Github",command=openGithub)
    Open_github.grid(row=6,column=1,padx=5,pady=5,sticky="w")
    Open_Linkedin = Button(Developer_frame, text = "Linkedin",command=openLinkedin)
    Open_Linkedin.grid(row=6,column=2,padx=5,pady=5,sticky="w")
########################UI ELEMENTS OF DEV INFO WINDOW###########################################################################################################################

########################UI ELEMENTS OF HELP INFO WINDOW###########################################################################################################################
#Help window creation
def openHelpWindow():
    #show developer information
    print("Controls Information")
    # Toplevel object which will
    # be treated as a new window
    Help_window = Toplevel(main)

    # sets the title of the
    # Toplevel widget
    Help_window.title("Help window")

    # sets the geometry of toplevel
    Help_window.geometry("650x715")

    # setting up the minimum size and maximum size for the application's developer window
    # set minimum window size value
    Help_window.minsize(650, 715)

    # set maximum window size value
    Help_window.maxsize(650, 715)

    #importing images from the directory when creating the help window
    # #if the import of ImageTk does't work then
    # #type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
    # #this module allows us to use png and jpg images in our program
    # from PIL import ImageTk,Image before using ImageIk
    global img1,img2, imageList
    img1 = ImageTk.PhotoImage(Image.open("controls.png"))
    img2 = ImageTk.PhotoImage(Image.open("camera_controls.png"))
    #creating an image list so that we can scroll through the images in our application
    imageList=[img1,img2]

    #background color for Menu_frame
    Help_frame_backgrount_color = "#8a1253"
    Help_frame = LabelFrame(Help_window,text="Help",bd=7,relief=GROOVE,font=("times new roman", 15, "bold"),fg = "white", bg = Help_frame_backgrount_color, padx= 5,pady=5)
    #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
    # relwidth is the welative width of the frame relative to the other ui components of the application
    Help_frame.place(x=0,y=0,width=650,height=715)
    #import image from the directory
    #make canvas and img varables into global variable otherwise the image will not show up in the application
    Canvas_background_color = "#f0ab8d"
    Canvas_Frame = LabelFrame(Help_frame,text="",bd=7,relief=GROOVE,font=("times new roman", 15, "bold"),fg = "white", bg = Canvas_background_color, padx= 5,pady=5)
    Canvas_Frame.place(x=0,y=50,width=625,height=625)

    #make canvas and img varables into global variable otherwise the image will not show up in the application
    global canvas
    canvas = Canvas(Canvas_Frame, width =600, height = 600)
    canvas.grid(row=0,column=0,rowspan=5)
    #puttin image on the screen in our application
    #canvas will start drawing the image from the coordinates 2,2
    canvas.create_image(2, 2, anchor=NW, image=img1)

    def OpenRobotControlsHelp(image_list_index):
            canvas = Canvas(Canvas_Frame, width =600, height = 600)
            canvas.grid(row=0,column=0,rowspan=5)
            #puttin image on the screen in our application
            #canvas will start drawing the image from the coordinates 2,2
            canvas.create_image(2, 2, anchor=NW, image=imageList[image_list_index])
    def OpenRobotCameraControlsHelp(image_list_index):
            canvas = Canvas(Canvas_Frame, width =600, height = 600)
            canvas.grid(row=0,column=0,rowspan=5)
            #puttin image on the screen in our application
            #canvas will start drawing the image from the coordinates 2,2
            canvas.create_image(2, 2, anchor=NW, image=imageList[image_list_index])

    #button to display the help related to show Robot's Movement controls
    Movement_Help_button = Button(Help_frame,text="Robot Controls", command = lambda : OpenRobotControlsHelp(0), font = ("times new roman",15,"bold"),bg="#c51350", fg="black")
    Movement_Help_button.grid(row=0,column=0, sticky="w", pady=5 ,padx=5)

    #button to display the help related to show Robots Camera controls
    Camera_Help_button = Button(Help_frame,text="Camera Controls", command = lambda : OpenRobotCameraControlsHelp(1), font = ("times new roman",15,"bold"),bg="#c51350", fg="black")
    Camera_Help_button.grid(row=0,column=1, sticky="w", pady=5 ,padx=5)
########################UI ELEMENTS OF HELP INFO WINDOW###########################################################################################################################


#devInfo and Help Frame UI elements
devInfo_frame_background = "#9fd3c7"
devInfo_frame = LabelFrame(main,text="",font = ("times new roman",20,"bold"),padx=5,pady=5, bd=5, relief=RIDGE,fg = "white", bg = devInfo_frame_background)
devInfo_frame.place(x=390,y=80,width= 635, height= 60)

#A button to run test Motor module for testing and debugging before actual operation
dev_button = Button(devInfo_frame,text="Developer Information", command = openNewWindow, font = ("times new roman",15,"bold"),bg="#e0ffcd", fg="black")
dev_button.grid(row=0,column=0, sticky="w", pady=2)
#help_button
help_button = Button(devInfo_frame,text="Help", command = openHelpWindow, font = ("times new roman",15,"bold"),bg="#e0ffcd", fg="black")
help_button.grid(row=0,column=1, sticky="w", pady=2 ,padx=5)

#open camera
def start_camera():
    def start_camera():
        #initializing video recv class that will actually recieve video from the raspberry pi
        global video_reciever_class
        ip_addrc = ip_addr_text.get()
        print("server_vido_ip : ", ip_addrc)
        video_reciever_class = video_reciever(9000,str(ip_addrc))
        client_socket= video_reciever_class.connect_to_server()
        video_reciever_class.recv(client_socket)
    output_text_command = output_text.get()
    if output_text_command != "Video streaming: ON":
        if output_text_command != "Oops! Try again" and output_text_command != "Turn Left" and output_text_command != "Turn Right" and output_text_command != "Forward" and output_text_command != "Reverse" and output_text_command != "Stop":
            try:
                print("starting video transmission")
                output_field.configure(state='normal')
                output_field.delete(0,"end")
                output_field.insert(END,"Video streaming: ON") #commands_Sent are the commands that is sent to the server
                output_field.configure(state='disabled')
                client_video_class.send("e", client_video_id)
                global proc
                proc = multiprocessing.Process(target=start_camera, args=())
                proc.start()
            except:
                print("Oops Try again")
                output_field.configure(state='normal')
                output_field.delete(0,"end")
                output_field.insert(END,"Oops! Try again") #commands_Sent are the commands that is sent to the server
                output_field.configure(state='disabled')
        else:
            messagebox.showerror("ERROR (69x420)","Camera is already on!!")
            return
    else:
        messagebox.showerror("ERROR (69x420)","Camera is already on!!")
        return

def stop_camera():
    output_field.configure(state='normal')
    output_field.delete(0,"end")
    output_field.insert(END,"Video streaming: OFF")
    output_field.configure(state='disabled')
    proc.terminate()


camera_ON_button = Button(devInfo_frame,text="Camera On", command = start_camera, font = ("times new roman",15,"bold"),bg="#e0ffcd", fg="black")
camera_ON_button.grid(row=0,column=2, sticky="w", pady=2 ,padx=5)

camera_OFF_button = Button(devInfo_frame,text="Camera Off", command = stop_camera, font = ("times new roman",15,"bold"),bg="#e0ffcd", fg="black")
camera_OFF_button.grid(row=0,column=3, sticky="w", pady=2 ,padx=5)

#detecting left arrow key press
def leftKey(event):
    print ("LeftArrow key pressed")
    #left(speed=0.5, t=0)
    # motor.left(1,0.1)
    Command_sent = "a"
    client_class.send(Command_sent, client_id)
    output_field.configure(state='normal')
    output_field.delete(0,"end")
    output_field.insert(END,"Turn Left")
    output_field.configure(state='disabled')

#detecting right arrow key press
def rightKey(event):
    print ("RightArrow key pressed")
    #right(speed=0.5, t=0)
    # motor.right(1,0.1)
    Command_sent = "d"
    client_class.send(Command_sent, client_id)
    output_field.configure(state='normal')
    output_field.delete(0,"end")
    output_field.insert(END,"Turn Right")
    output_field.configure(state='disabled')

#detecting up arrow key press
def upKey(event):
    print ("upArrow key pressed")
    #forward(speed=0.5, t=0)
    # motor.forward(1,0.1)
    Command_sent = "w"
    client_class.send(Command_sent, client_id)
    output_field.configure(state='normal')
    output_field.delete(0,"end")
    output_field.insert(END,"Forward") #commands_Sent are the commands that is sent to the server
    output_field.configure(state='disabled')

#detecting up arrow key press
def downKey(event):
    print ("downArrow key pressed")
    #reverse(speed=0.5, t=0)
    # motor.reverse(1,0.1)
    Command_sent = "s"
    client_class.send(Command_sent, client_id)
    output_field.configure(state='normal')
    output_field.delete(0,"end")
    output_field.insert(END,"Reverse") #commands_Sent are the commands that is sent to the server
    output_field.configure(state='disabled')

#detecting b key for applying breaks
def halt(event):
    print ("downArrow key pressed")
    #reverse(speed=0.5, t=0)
    # motor.reverse(1,0.1)
    Command_sent = "b"
    client_class.send(Command_sent, client_id)
    output_field.configure(state='normal')
    output_field.delete(0,"end")
    output_field.insert(END,"Stop") #commands_Sent are the commands that is sent to the server
    output_field.configure(state='disabled')

frame = Frame(main, width=1, height=1)

#binding keys with the UI
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.bind('<Down>', downKey)
main.bind('b', halt)

frame.pack()
######################################################################################################################################


##################DEFINING UI COMPONENTS OF THE APPLICATION RELATED TO CONNECT AND DISCONNECT #########################################

#backend of UI elements related to connect and disconnect
# #this will handle the client disconnect process
DISCONNECT_MESSAGE = "!DISCONNECT"
def disconnect():
    print("disconnecting from raspberry pi....")
    #close Robot motor controller server
    client_class.send(DISCONNECT_MESSAGE, client_id)
    client_video_class.send(DISCONNECT_MESSAGE, client_video_id)
    connect_button["state"]="normal"
    disconnect_button["state"]="disabled"
    output_field.delete(0,"end")

def connect():
  print("connecting to raspberry pi....")
  #connect to robot's motor controller server
  global server_ip
  global ip_addr
  ip_addr = ip_addr_text.get()
  if ip_addr== "":
       messagebox.showerror("Required Fields", "Input Fields are NULL!")
       return
  else:
      server_ip = ip_addr
  print(ip_addr)
  # client_manager(HEADER, PORT, FORMAT, SERVER)
  global client_class
  client_class = client_manager(128, 5050, 'utf-8', str(ip_addr))
  #getting client id on the local area network
  global client_id
  client_id = client_class.connect_to_server()
  ERR = client_id
  client_class.send("start_signal_from_client", client_id)
  if ERR==True:
      messagebox.showerror("ERROR", "Cannot find your Robot on the network \nMake sure you and the server are on the same LAN network")
      connect_button["state"]="normal"
      disconnect_button["state"]="disabled"
      return

  #client video manager that will start the video transmission server when e button is pressed so that video reciever
  # can recieve video from raspberry pi
  print(ip_addr)
  # client_manager(HEADER, PORT, FORMAT, SERVER)
  global client_video_class
  client_video_class = client_video_manager(128, 5000, 'utf-8', str(ip_addr))
  #getting client id on the local area network
  global client_video_id
  client_video_id = client_video_class.connect_to_server()
  ERR = client_video_id
  client_video_class.send("start_signal_from_client", client_video_id)
  if ERR==True:
      messagebox.showerror("ERROR", "Cannot find your Robot on the network \nMake sure you and the server are on the same LAN network")
      connect_button["state"]="normal"
      disconnect_button["state"]="disabled"
      return
  connect_button["state"]="disabled"
  disconnect_button["state"]="normal"

#frame that will contain UI elements related to connect and disconnect to raspberry pi
connect_frame_background = "#5b446a"
connect_frame = LabelFrame(main,text="",padx=5,pady=5, bd=5, relief=RIDGE,fg = "white", bg = connect_frame_background)
connect_frame.place(x=0,y=0, width= 390, height= 140)

#input field to enter the ip address of the raspberry pi
ip_addr_text = StringVar()
ip_addr_input = Entry(connect_frame,font = ("times new roman",15,"bold"),bg="#f6e4ad", fg="black", textvariable = ip_addr_text).grid(row=0,column=0,pady=5,padx=7, columnspan=2, sticky=W+E)

#connect to raspberry pi button
connect_Label = Label(connect_frame, text="Connect to robot : ", font = ("times new roman",15,"bold"), bg = connect_frame_background)
connect_Label.grid(row=1,column=0, sticky="w")
connect_button = Button(connect_frame,text="Connect", command=connect, font = ("times new roman",15,"bold"),bg="#906387", fg="black")
connect_button.grid(row=1,column=1, sticky=W+E)

#disconnect from raspberry pi robot
connect_Label = Label(connect_frame, text="Disconnect from robot : ", font = ("times new roman",15,"bold"), bg = connect_frame_background)
connect_Label.grid(row=2,column=0, sticky="w")
disconnect_button = Button(connect_frame,text="Disconnect", command=disconnect, font = ("times new roman",15,"bold"),bg="#906387", fg="black")
disconnect_button.grid(row=2,column=1, sticky="w")
disconnect_button["state"]="disabled"

##################################################################################################################################################

main.mainloop()
