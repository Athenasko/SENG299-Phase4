#copied Socket Client segement 
import socket
s = socket.socket()
host = socket.gethostname()
port = 9999
address = (host, port)
msg = raw_input("Please input your message: ")
s.connect(address)
s.send(msg)