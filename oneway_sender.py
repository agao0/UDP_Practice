import socket
import sys
import threading
import random, time

RENDEZVOUS_ADDRESS = ('192.168.1.136', 55555)
MY_SOURCE_PORT = 50002

print("Connecting to rendezvous")
mySourceSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySourceSocket.bind(('0.0.0.0', MY_SOURCE_PORT))
mySourceSocket.sendto(b'0', RENDEZVOUS_ADDRESS)

while True:
    data = mySourceSocket.recv(1024).decode()

    if data.strip() == 'ready':
        print("Checked in with server, waiting until pair is complete.")
        break

# Rendezvous server gives the info of the other client
data = mySourceSocket.recv(1024).decode() # SOMETIMES RENDEZVOUS MAY HAVE LOSS
ip, sport= data.split(' ')
OTHER_SOURCE_PORT = int(sport)

print("\nGot peer:")
print("    ip:   {}".format(ip))
print("    port:    {}".format(sport))

OTHER_ADDRESS = (ip, OTHER_SOURCE_PORT)

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

outputFile = open("output.txt", 'w')
for i in doubles:
    outputFile.write(i+'\n')