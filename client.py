#Importing socket module from python library 
import socket

#AF_INET for IPv4 and SOCK_STREAM for TCP protocol. Creating client object 
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Host can be given IP of the server explicitly. Port should match
host = socket.gethostname()
port = 444

clientsocket.connect((host, port))

#Specifying maximum amount of data coming through the port
message = clientsocket.recv(1024)

#Client side socket closed for decoding message 
clientsocket.close()

#Message to be decoded after socket closed 
print(message.decode('ascii'))


