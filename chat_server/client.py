#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket , sys , select

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

    data = client.recv(1024)
    if data:
        print(data.decode())

    sendData=input("Mesaj :")
    client.send(str.encode(sendData))

    


    