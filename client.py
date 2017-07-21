#copied Socket Client segement 
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

address = (host, port)

while True:
	s.connect(address)
	#try:
	#	alias = raw_input("Please input an alias: ")
	#except :
	#	alias = host

	msg = raw_input("Please input your message: ")
	#s.send(alias)
	s.send(msg)