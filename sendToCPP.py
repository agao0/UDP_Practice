import socket
import sys
import threading
import random, time

OTHER_ADDRESS = ('192.168.1.66', 55555)

MY_SOURCE_PORT = 50002
mySourceSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySourceSocket.bind(('0.0.0.0', MY_SOURCE_PORT))


# Hole Punch
print("Punching hole")

mySourceSocket.sendto(b'0', OTHER_ADDRESS)

print("Ready to chat\n")

# SENDING
doubles = []
start = time.time()
print("START TIME")
while len(doubles) < 100000:
    msg = str(random.random())
    mySourceSocket.sendto(msg.encode(), OTHER_ADDRESS)
    doubles += [msg]
print("TIME ELAPSED: " +str(time.time() - start))

mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS) # Need multiple in case it gets lost...
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)
mySourceSocket.sendto("stop".encode(), OTHER_ADDRESS)


outputFile = open("output.txt", 'w')
for i in doubles:
    outputFile.write(i+'\n')