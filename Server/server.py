#!/usr/bin/env python3

import socket
import time
import struct

HOST = '192.168.43.35'  # Standard loopback interface address (localhost)
PORT = 65433       # Port to listen on (non-privileged ports are > 1023)


feedbackForHacker = None
feedbackForNonHacker = None

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    print("here")
                    data = conn.recv(1024)
                    data1 = data.decode()
                    data = data1
                    data = data.split(" ")
                    print (data)
                    if data[3] == 'True':
                        feedbackForNonHacker = data1
                        if feedbackForHacker:
                            print("here2")
                            conn.sendall(feedbackForHacker.encode())
                        else:
                            print("here3")
                            conn.sendall("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0".encode())
                    else:
                        feedbackForHacker = data1
                        if feedbackForNonHacker:
                            conn.sendall(feedbackForNonHacker.encode())
                        else:
                            conn.sendall("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0".encode())
                    #s.close()
                    if not data:
                        break
    except Exception as e:
        print(e)
            # delay(10000)        
        continue
