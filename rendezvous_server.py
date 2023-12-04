import socket

placeholder_IP = "0.0.0.0"
# ASSUMED TO BE OPEN. TODO: figure out how to check which ports are availabe to use as rendezvous
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET = IPv4
sock.bind((placeholder_IP, 55555))

while True:
    clients = []

    while True:
        data, address = sock.recvfrom(128)
        print('Connection received from: {}'.format(address))
        clients.append(address)

        sock.sendto('ready'.encode(), address)

        if len(clients) == 2:
            print("Two clients have connected. Exchanging data for hole punch.")
            break
    
    c2 = clients.pop()
    c1 = clients.pop()
    c1_address, c1_port = c1
    c2_address, c2_port = c2

    sock.sendto('{} {}'.format(c1_address, c1_port).encode(), c2)
    sock.sendto('{} {}'.format(c2_address, c2_port).encode(), c1)
    break
