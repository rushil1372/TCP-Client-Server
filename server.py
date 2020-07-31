#Importing socket module from python library 
import socket 

#Creating serversocket object that calls socket function and takes socket family and socket type as parameters.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Create host with gethostname function and specify port number. gethostname returns back server ip (helps in automation).
host = socket.gethostname()
port = 444

#Bind the host and the port number to the socket object.
serversocket.bind((host, port))

#Set up listener for the serversocket. Parameters specify number of connections we can listen to.
serversocket.listen(3)

#Executes while all conditions are true
while True:

    #Accepts info from the client
    clientsocket, address = serversocket.accept()

    print("Recieved address from " % str(address))
    
    #Message sent to client once connected to the server
    message = "Connected to server" + "\r\n"

    #Message is encoded before sending or process would fail 
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()

