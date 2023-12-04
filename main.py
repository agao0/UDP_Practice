import socket

localIP = "192.168.1.136"
localPort = 5005
bufferSize = 1024

msgToSend = "HELLO\n"
bytesToSend = str.encode(msgToSend)

# Set up UDP stuff
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP Server is online")

while True:
    bytesAndAddress = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAndAddress[0].decode()
    address = bytesAndAddress[1]

    print("Message: " + message)
    print("Client IP: " + address)

    UDPServerSocket.sendto(bytesToSend, address)