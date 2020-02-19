#!/usr/bin/env python3

import socket
import time
import struct


HOST = '192.168.1.228'  # Standard loopback interface address (localhost)
PORT = 65433       # Port to listen on (non-privileged ports are > 1023)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    print (data.decode())
                    if not data:
                        break
    except:
        continue
                #conn.sendall(b"Recieved")
