import socket
import threading
import sys
from tkinter import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sendMsg():
	while True:
		try:
			s.send(bytes(input("> "), "utf-8"))
		except Exception as e:
			print("Error {}".format(str(e)))


def client(address):
	s.connect((address, 4444))

	iThread = threading.Thread(target=sendMsg)
	iThread.deamon = True
	iThread.start()

	while True:
		try:
			data = s.recv(1024)
			print(str(data, 'utf-8'))
		except:
			pass

"""def screen():
	screen = Tk()
	screen.title('communicator')

	txt_input = ''
	print(txt_input)

	#screen.geometry("445x500")
	Display = Entry(screen, font=('arial', 30), justify='right', textvariable=txt_input)
	Display.grid(columnspan = 3)
	BtnEnt = Button(screen, fg='blue', font=('arial',30), text='ENTER', command=sendMsg(txt_input))
	BtnEnt.grid(row=1, columnspan=4) 
	screen.mainloop()"""

if len(sys.argv) > 1:
	client(sys.argv[1])
else:
	print("Nie można połączyć z serwerem. Sprawdź IP serwera")
	sys.exit()