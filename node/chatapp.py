#!/usr/local/bin/python3

import os
import sys
import socket
import threading

PORT = 2222

# Socket
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind(("0.0.0.0", PORT))

# Local
name = socket.gethostname()

# Remote
ip = None
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    ip = input("Connect to: ")
    print("")
try:
    socket.getaddrinfo(ip, None, socket.AF_UNSPEC)
except socket.gaierror as e:
    print(e, file=sys.stderr)
    exit(1)

# Start
print("====>  UDP CHAT APP  <=====")
print("===========================")
print("\nType 'quit' to exit.")

# Subs
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
