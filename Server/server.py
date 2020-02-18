#!/usr/bin/env python3

import socket
import time
import struct


<<<<<<< HEAD
HOST = ''  # Standard loopback interface address (localhost)
PORT = 8888        # Port to listen on (non-privileged ports are > 1023)
=======
HOST = '192.168.86.25'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
>>>>>>> c030830feee7f79b521f5cc5f4ff69049efaa2d7

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)

                # data = struct.unpack('<d', data)[0]
                try:
                    data = struct.unpack('<d', data)[0]
                except:
                    break
                if not data:
                    break
                conn.sendall(b"Recieved")
