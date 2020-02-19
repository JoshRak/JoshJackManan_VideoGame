#!/usr/bin/env python3

import socket

HOST = '192.168.86.25'  # The server's hostname or IP address
PORT = 65432     # The port used by the server

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b"Hello")
            data = s.recv(1024)
            print(data)
    except:
        continue
