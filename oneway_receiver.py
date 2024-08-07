import socket
import sys
import threading
import time

RENDEZVOUS_ADDRESS = ('192.168.1.66', 55555)

MY_SOURCE_PORT = 50002
mySourceSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySourceSocket.bind(('0.0.0.0', MY_SOURCE_PORT))

# LISTENING
xvals = []
yvals = []
while True:
    data = mySourceSocket.recv(2048) # How does this matter if the buffer is still in the socket? I thought UDP doesn't know where a message ends...
    # OBSERVATIONS: 
    # If buffer is set to 2, only got "0." once decoded
    # If buffer is set to 4, only got "0.XX" once decoded. Got it, buffer is max size of the payload. I.e. if buffer is less than payload, payload is truncated.
    #   -> AND DATA IS LOST: sent over 100k doubles, only got 85647
    #   -> AND TRANSFER IS SLOWER: Took 1.5 seconds to run input loop, and even sending data was slower (maybe computer just slowing down? Print statement may be too slow)
    # If buffer is set to 6, get "0.XXXX" once decoded.
    #   -> INTERESTINGLY: took longer and lost more data, took 1.94 seconds to input, 1.65 seconds to send, only got 80598 data points.
    # ...
    # If buffer is set to 1024, and removed print, and added 3 stops, lost 1 data packet on 275th double, but back to full speed sending 1.18, full speed input 1.21s. 
    # If buffer is set to 2048, lost no data, also even faster sending and input. Interesting...
    data = mySourceSocket.recv(2048)
    string = data.decode()
    line = string.split(' ')
    xvals += [float(line[0])]
    yvals += [float(line[1])]
    print(xvals[-1], yvals[-1])

    

outputFile = open("test.txt", 'w')
for i in doubles:
    outputFile.write(i+'\n')
