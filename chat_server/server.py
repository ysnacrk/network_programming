#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

server.listen(1) 

while True:
    
    connection , adress = server.accept()

    while True:
        sendData=input("Mesaj :")
        connection.send(str.encode(sendData))
        data = connection.recv(1024)
        if data:
            print(data.decode())
    



    

