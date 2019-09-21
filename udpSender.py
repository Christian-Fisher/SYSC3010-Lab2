# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
num = int(sys.argv[3])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

x=1
while 1:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
    x=1
    while (x<=num):
        data += str(x)
        s.sendto(data.encode('utf-8'), server_address)
        data = data[:-1]
        x=x+1
        ackBuffer,AckAdd =  s.recvfrom(port)
        print (ackBuffer)
        
s.shutdown(1)

