import sys
import socket
import select

host = '' #localhost - local area network
recv_buffer = 4096
socket_list = []
port = 6969 #this is the default port number


def server():
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#makes socket reusable 
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				
	server_socket.setblocking(0)
	server_socket.bind((host, port))

 	#for 20 client connection
	server_socket.listen(20)

	#adds server socket to the list
	socket_list.append(server_socket)
	server_valid = 1
	
	 	
	print "Server started on Port: " + str(port)
	
	
	while 1:
		
		#set all sockets for ready for reading
		#create empty list for all the sockets that may be written into
		#create empty list for sockets to be checked for errors	
		#0 represent timeout value so no blocking 
		ready_for_reading,ready_for_writing,error_condition = select.select(socket_list, [], [], 0)

		for sock in ready_for_reading:
			#new connection
			if sock == server_socket:
				sock_forward, address = server_socket.accept()
				socket_list.append(sock_forward)
				print "Client %s %s connected to server" % address
				 
				broadcast(server_socket, sock_forward, "[%s:%s] entered the room \n Greet them pleasantly!\n" % address)
			#message for already connected client
			else: 
				#process message data
				try:	
					#receive data from socket					
					message_data = sock.recv(recv_buffer)
					#if there is a message broadcast it
					if message_data:
						broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + ']' + message_data)

				
					else:

						#if socket is broken remove it
						if socket in socket_list:
							socket_list.remove(socket)
						#broadcast disconnection
						broadcast(server_socket, sock, "Client (%s, %s) is now offline, hopefully they said goodbye\n" % address)
				
				except:
					broadcast(server_socket, sock, "Client (%s, %s) is now offline, hopefully they said goodbye\n" % address)
					continue



	server_socket.close()

			 
				
#function to broadcast to all clients
def broadcast(server_socket, sock, message):
		
	for socket in socket_list: 
		#so it doesn't send to sender
		if socket != server_socket and socket != sock:
			try:
				socket.send(message)
			except:
				#broken connection
				socket.close()
				#if socket is broken remove it
				if socket in socket_list:
					socket_list.remove(socket)

if __name__ == "__main__":

	sys.exit(server()) 
			
				




		
	
		


