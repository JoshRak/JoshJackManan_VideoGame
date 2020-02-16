#!/usr/bin/env python3

import socket
from datetime import datetime
import time
import struct


HOST = '192.168.43.227'  # The server's hostname or IP address
PORT = 65432		# The port used by the server

masterDict = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	# l = open("main.py", "rb").read(1024)
	i = 0
	runningSum = 0
	maxi = -100000000000000
	mini = 100000000000000
	for i in range(0, 100000):
		try:
			something = time.time() # struct.pack("<d", time.time())
			# print(time.time())
			# s.sendall(b'banana')
			s.sendall(struct.pack("<d", something))
			data = s.recv(1024)
			# data = struct.unpack("<d", data)[0]
			result = (time.time() - something)/2
			if result < mini:
				mini = result
			if result > maxi:
				maxi = result
			runningSum += result
			if i % 100 == 0:
				print("Average: {} | Minimum {} | Maximum {}".format(runningSum/(i+1), mini, maxi), end="\r")

			masterDict.append(result)

		except KeyboardInterrupt:
			break

print (sum(masterDict)/len(masterDict))
print (max(masterDict))
print (min(masterDict))
# print(time.time())
# print(time.time(), repr(data))