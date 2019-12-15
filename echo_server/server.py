import socket

port_number = 12345
host_adress = '127.0.0.1'

#create socket objcet
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#binding hostname and port number
server.bind((host_adress , port_number))

#listen needss to queue size
server.listen(2)

#waiting for client

while True: 

    """ 
    -Accept the connection
    -Return value is a piar connection and adress
    -Connection is a new socket object usable send and recv data on the connection
    -Adress other end of adress

    """

    connection , adress = server.accept()
    print("Connected ", adress)
    
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
        
