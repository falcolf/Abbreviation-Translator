import socket
import sys
import time
import tkinter
from translation import *
import threading




class MyClient(threading.Thread):

	flag = 0
	def run(self):
		#initializing window
		self.root = tkinter.Tk()
		self.root.geometry("550x200")
		self.root.title("Chat App")
		#Label
		self.lab = tkinter.Label(self.root ,  width = 25 , text = "Enter Message Here ").grid(row = 1)

		#Text Box for message
		self.box = tkinter.Entry(self.root, width = 25 )
		self.box.grid(row=1 , column = 1)
		
		#Text Display
		self.disp = tkinter.Text(self.root, width = 50 , height = 10)
		self.disp.grid(row=3 , column= 0 , columnspan = 4)
		self.disp.insert(tkinter.INSERT , "Welcome to Chat (Server)\n\n")

		#Send button
		self.bsend = tkinter.Button(self.root , text = "Send Message",fg = 'blue' )
		self.bsend.pack()
		self.bsend.grid(row = 1 , column = 2)
		#button event
		self.bsend.bind('<Button-1>' , self.sendMessage)

		if flag==0:
			self.getMessage()

		self.root.mainloop()

	#def to send message to the server
	def sendMessage(self , event):
		message=translate_message(abbreviations_dictionary, self.box.get())
		msg = "[ Client ] says : " + message + " \n"
		self.disp.insert(tkinter.INSERT , msg)
		self.disp.insert(tkinter.INSERT , "Waiting for Reply")
		msg=msg.encode()
		self.box.delete(first = 0 , last = len(self.box.get()))
		self.s.send(msg)
		print("sent")
		self.box.config(state='disabled')
		f=0

	def getMessage(self):
		if f==0:
			income_message=conn.recv(1024)
			income_message=income_message.decode()
			print("A1>> ",income_message)
			#app.showMessage(msg = income_message)
			print(" ")
			f=1
			self.box.config(state = 'normal')
	
	

	#def to show messge
	def showMessage(self , msg):
		self.disp(tkinter.INSERT, msg)

	def __init__(self,s):
		threading.Thread.__init__(self)
		self.s = s
		self.start()



#Connection
s=socket.socket()
host="Ava"
print('server started on '+ host)
port=1234
s.bind((host,port))
print('server successfully binded to host and port')
print('')
print("Waiting for connection")
s.listen(5)
conn,addr=s.accept()
print(addr, " has connected to the server")
print(" ")
abbreviations_dictionary = file_to_dictionary("abbreviations_dictionary.txt")

app = MyClient(s)


print("thread spawned")
