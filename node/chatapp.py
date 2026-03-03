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
HOST = None
if len(sys.argv) >= 2:
    HOST = sys.argv[1]
else:
    HOST = input("Connect to host: ")
    print("")
try:
    socket.getaddrinfo(HOST, None, socket.AF_UNSPEC)
except socket.gaierror as e:
    print(e, file=sys.stderr)
    sys.exit(1)

# Start
print("====>  UDP CHAT APP  <=====")
print("===========================")
print("\nType 'quit' to exit.")

# Subs
def send() -> None:
    """Send message."""
    while True:
        message = input(">> ")
        if message in ('quit', 'exit'):
            os._exit(0)   # use os._exit() to kill the threads, sys.exit() doesn't
        if message == '': # skip blank lines (just pressing `Enter`)
            continue
        message = f"{name}: {message}"
        s.sendto(message.encode(), (HOST, int(PORT)))

def recv() -> None:
    """Receive message."""
    while True:
        message = s.recvfrom(1024)
        print("\t\t\t\t >> " +  message[0].decode(), flush=True)
        print(">> ", flush=True)

x1 = threading.Thread( target = send )
x2 = threading.Thread( target = recv )
x1.start()
x2.start()
