#chat_client.py

import sys
import socket
import select
 
def chat_client():
	if(len(sys.argv) < 3):
		print 'Usage: python chat_client.py hostname port'
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
     
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.settimeout(2)
     
	#connect to remote host
	try:
		server_socket.connect((host, port))
	except:
		print 'Unable to connect'
		sys.exit()
     
	print 'Connected to remote host. You can start sending messages'
	sys.stdout.write('[Me] '); sys.stdout.flush()
     
	while 1:
		socket_list = [sys.stdin, server_socket]
         
		#Get the list sockets which are readable
		ready_for_reading, ready_for_writing, error_condition = select.select(socket_list , [], [])
         
		for sock in ready_for_reading:             
			if sock == server_socket:
				#incoming message from remote server, server_socket
				data = sock.recv(4096)
				if not data:
					print '\nDisconnected from chat server'
					sys.exit()
				else:
					#print data
					sys.stdout.write(data)
					sys.stdout.write('[Me] '); sys.stdout.flush()     
            
			else:
				#user entered a message
				message_data = sys.stdin.readline()
				server_socket.send(message_data)
				sys.stdout.write('[Me] '); sys.stdout.flush() 

def Broadcast(server_socket, city, message):
	message = "[" + user.alias + "]: " + message

class City:
	def __init__(self, name):
		self.user_list = []
		self.name = name

class User:
	def __init__(self, socket, name = "Anonymous"):
		socket.setblocking(0)
		self.alias = name

if __name__ == "__main__":

	sys.exit(chat_client())
