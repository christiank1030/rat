#!/usr/bin/env python3

import socket

host = ''
port = 65430

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while(True):
        msg = input("Your command: ")
        s.sendall(str.encode(msg))
        if(msg == "exit"):
            break
        data = s.recv(2048)
        print("Target recieved command\n", data.decode())