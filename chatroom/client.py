#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket , sys , select
from threading import Thread
from  tkinter import Tk , scrolledtext , Button , Listbox , END , Text ,Label

"""argv[0] is name of program """

"""

host = sys.argv[1]
port = sys.argv[2]

"""

def handle_thread():

    while True:
        message = client.recv(1024)
        length = len(message)
        message_list.insert(END , message[2:length-3])  


def send_message():
    
    message = username.get("1.0" ,END)
    length = len(message)
    message = message[0:length-1]
    message += " : "
    message += text.get("1.0" , END)
    text.delete("1.0" , END)
    print(message)
    client.send(str.encode(message))

window = Tk()
window.title("Chat Room")
window.geometry('680x430')

message_list = Listbox(window, height=10, width=49)
message_list.grid(column=0,row=11)

lbl = Label(window, text="Kullanıcı Adı")
lbl.grid(column=0, row=0)

username = Text(window, height = 1, width=20)
username.grid(column = 1 , row = 0)

text = Text(window, height = 2 , width=48)
text.grid(column = 0 , row = 12)

btn = Button(window, text="Send", command = send_message)
btn.grid(column=1, row=12)

host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host , port))

thread = Thread(target=handle_thread)
thread.start()

window.mainloop()
client.close()


