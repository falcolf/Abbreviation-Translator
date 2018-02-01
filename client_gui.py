import socket
import sys
import time
import tkinter 
from translation import *

flag = 1
	
#Connection
s=socket.socket()
host = "Ava"
#host=input(str("please enter the host name:"))
port=12052
s.connect((host,port))
print("Connected to the chat network")
abbreviations_dictionary = file_to_dictionary("abbreviations_dictionary.txt")


#def to send message to the server
def sendMessage(event):
	global flag
	message=translate_message(abbreviations_dictionary, box.get())
	msg = "[ Client ] says : " + message + " \n"
	disp.insert(tkinter.INSERT , msg)
	#disp.insert(tkinter.INSERT , "Waiting for Reply")
	msg=msg.encode()
	box.delete(first = 0 , last = len(box.get()))
	#box.config(state='disabled')
	s.send(msg)
	print("sent")
	flag = 0
	
	
def showMessage(msg):
	disp.insert(tkinter.INSERT, msg)



#initializing window
root = tkinter.Tk()
root.geometry("500x200")
root.title("Chat App")
#Label
lab = tkinter.Label(root ,  width = 25 , text = "Enter Message Here ").grid(row = 1)
#Text Box for message
box = tkinter.Entry(root, width = 25 )
box.grid(row=1 , column = 1)

#Text Display
disp = tkinter.Text(root, width = 50 , height = 10)
disp.grid(row=3 , column= 0 , columnspan = 4)
disp.insert(tkinter.INSERT , "Welcome to Chat\n\n")

#Send button
bsend = tkinter.Button(root , text = "Send Message",fg = 'blue' )
bsend.pack()
bsend.grid(row = 1 , column = 2)
		
#button event
bsend.bind('<Button-1>' ,sendMessage)


while 1:
	print(flag)
	if flag == 1:
		print("Allowed to send")
	if flag == 0:
		print("now recieve")
	while flag == 0:
		income_message=s.recv(1024)
		income_message=income_message.decode()
		showMessage(income_message)
		if income_message:
			flag = 1
		
	box.config(state = 'normal')
	root.update_idletasks()
	root.update()
	
	
	




