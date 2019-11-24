import socket
import sys
from threading import Thread

"""

- Her gelen istek için ayrı ayrı thread oluşturmamız gerekiyor
- select 
"""


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP = "127.0.0.1"
PORT = 12345

server.bind((IP, PORT)) 

server.listen(4) 
client_list  = []

def thread_func(connection , adress):
    
    connection.send("Welcome to this chatroom!".encode("utf8")) 
    while True:
        data = connection.recv(1024)
        if data:
            print(str(data))
            message = str(data)
            send_function(message , connection)


def send_function(data , connection):
    for client in client_list:
        client.send(data.encode("utf8"))

while True:
    
    #burada yeni bir thread oluşturmamız gerekiyor
    connection , adress = server.accept()
    
    #bu listeyi sürekli kontrol etmemiz gerekiyor
    client_list.append(connection)
    
    print(adress[0] + " bağlandı")

    thread = Thread(target=thread_func , args=(connection , adress))
    thread.start()



    

