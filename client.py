#Socket Client segment provided by Caleb Shortt.
import socket
s = socket.socket()
host = socket.gethostname()
port = 9999
address = (host, port)
msg = 'test 123'
s.connect(address)
s.send(msg)
