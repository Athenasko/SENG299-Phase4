#Copied Socket server segement
import select
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
address = (host, port)
user_list = []
user_list.append(s)
print('Starting Server...')
s.bind(address)
s.listen(20)
while True:
	ready_to_read, ready_to_write, in_error = select.select(user_list, [], [])
	for sock in ready_to_read:
	 	if sock == s:
	 	    client, addr = s.accept()
    		data = client.recv(4096)
     		if data == "Quit":
     			break
     		print('%s:%s says >> %s' % (addr[0], addr[1], data))
     		#messageBroadcast(s, sock, data)
     	else:
     		data = sock.recv(4096)
     		if data:
     			print('%s:%s says >> %s' % (addr[0], addr[1], data))
     			#messageBroadcast(s, sock, data)
     		else:
     			user_list.remove(sock)
    #client, addr = s.accept()
    #alias = client.recv(1024)
    #data = client.recv(1024)
    #if data == "Quit":
    #	break
    #if alias:
    #	print('%s says >> %s' % (alias, data))
    #else:
	#print('%s:%s says >> %s' % (addr[0], addr[1], data))

def messageBroadcast (s, sock, data):
	for socket in user_list:
		if socket != s and socket != sock:
			socket.send(data)