#!/usr/bin/env python3

import socket
import time
import struct


HOST = ''  # Standard loopback interface address (localhost)
PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

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
