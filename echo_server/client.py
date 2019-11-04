import socket , sys , datetime , time

"""argv[0] is name of program """

"""
host = sys.argv[1]
port = sys.argv[2]

"""
host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host , port))


while True:
    time.sleep(0.5)
    client.sendall(bytes(host , 'utf-8'))
    print(client.recv(1024))


