#!/usr/local/bin/python3

import os
import socket
import threading

PORT = 2222

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind(("0.0.0.0", PORT))

print("====>  UDP CHAT APP  <=====")
print("===========================")
name = socket.gethostname()
print("\nType 'quit' to exit.")
ip = input("Connect to: ")
if ip == "quit":
    os._exit(0)

def send():
    while True:
        message = input(">> ")
        if message == "quit":
            os._exit(0)
        message = "{}: {}".format(name, message)
        s.sendto(message.encode(), (ip, int(PORT)))

def recv():
    while True:
        message = s.recvfrom(1024)
        print("\t\t\t\t >> " +  message[0].decode(), flush=True)
        print(">> ", flush=True)

x1 = threading.Thread( target = send )
x2 = threading.Thread( target = recv )
x1.start()
x2.start()
