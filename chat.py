import socket
import threading
import sys

class Server:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []

	def __init__(self):
		self.s.bind(('0.0.0.0', 4444))
		self.s.listen(1)

	def handler(self, c, a):
		while True:
			try:
				data = c.recv(1024)
				for connection in self.connections:
					connection.send(data)
			except:
				print(str(a[0]) + ':' + str(a[1]), 'disconnected')
				self.connections.remove(c)
				c.close()
				break

	def run(self):
		while True:
			c, a = self.s.accept()
			cThread = threading.Thread(target=self.handler, args=(c, a))
			cThread.deamon = True
			cThread.start()
			self.connections.append(c)
			print(str(a[0]) + ':' + str(a[1]), 'connected')

class Client:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def sendMsg(self):
		while True:
			try:
				self.s.send(bytes(input(''), "utf-8"))
			except Exception as e:
				print(f"Error: {str(e)}")

	def __init__(self, address):
		self.s.connect((address, 4444))

		iThread = threading.Thread(target=self.sendMsg)
		iThread.deamon = True
		iThread.start()

		while True:
			try:
				data = self.s.recv(1024)
				print(str(data, 'utf-8'))
			except:
				pass


if (len(sys.argv) > 1):
	client = Client(sys.argv[1])
else:
	server = Server()
	server.run()