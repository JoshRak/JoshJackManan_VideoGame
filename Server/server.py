#!/usr/bin/env python3

import socket
import time
import struct
import json

HOST = '192.168.86.23'  # Standard loopback interface address (localhost)
PORT = 65433       # Port to listen on (non-privileged ports are > 1023)


feedbackForHacker = None
feedbackForNonHacker = None
# defaultDict = {'x': 250, 'y': 250, 'roomNum': 1, 'isHacker': False, 'imageStr': 'restingDownImage', 'roomThreeCompleted': False, 'roomFourCompleted': False, 'roomFiveCompleted': False, 'roomSixCompleted': True, 'roomSevenCompleted': False, 'roomEightCompleted': False, 'roomNineCompleted': False, 'roomTenCompleted': False, 'roomElevenCompleted': False, 'roomTwelveCompleted': False}
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024).decode()
                    data = json.loads(data)
                    print(data)
                    if data["isHacker"] == True:
                        feedbackForNonHacker = json.dumps(data)
        
                        if feedbackForHacker:
                            conn.sendall(feedbackForHacker.encode())
                        else:
                            conn.sendall("NONE".encode())
                    else:
                        feedbackForHacker = json.dumps(data)
                        print("Feedback for Hacker")
                        if feedbackForNonHacker:
                            conn.sendall(feedbackForNonHacker.encode())
                        else:
                            conn.sendall("NONE".encode())
                    #s.close()
                    if not data:
                        break
    except Exception as e:
        print(e)
            # delay(10000)        
        continue
