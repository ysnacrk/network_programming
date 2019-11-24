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

username = input("Username : ")

while True:
    sockets_list = [sys.stdin, client] 

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
    for socks in read_sockets:
        if socks == client:
            message = socks.recv(2048) 
            print(message)
        else:
            message = input()
            message = username + " : " + message
            client.send(message.encode("utf8"))

client.close()