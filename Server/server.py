#!/usr/bin/env python3

import socket
import time
import struct
import json

HOST = '192.168.43.227'  # Standard loopback interface address (localhost)
PORT = 65432       # Port to listen on (non-privileged ports are > 1023)


feedbackForHacker = None
feedbackForNonHacker = None

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # s.settimeout()
            s.bind((HOST, PORT))    # creates socket and listens for input from either player as JSON string
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024).decode() # decodes message
                    data = json.loads(data) # converts into dictionary
                    print(data)
                    if data["isHacker"] == True:    # checks is player is hacker or admin, sends appropriate feedback
                        feedbackForNonHacker = json.dumps(data) # converts back to string for sending to client
        
                        if feedbackForHacker:
                            conn.sendall(feedbackForHacker.encode())
                        else:
                            conn.sendall("NONE".encode())   # sends NONE if nothing to send
                    else:
                        feedbackForHacker = json.dumps(data)    # convest back to string for sending to client
                        print("Feedback for Hacker")
                        if feedbackForNonHacker:
                            conn.sendall(feedbackForNonHacker.encode())
                        else:
                            conn.sendall("NONE".encode())   # sends NONE if nothing to send
                    #s.close()
                    if not data:
                        break
    except Exception as e:
        print(e)
            # delay(10000)        
        continue
