# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time


host = sys.argv[1]
textport = sys.argv[2]
number = int(sys.argv[3])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
increment = 0
while 1:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    
    if not len(data):
        break
    while(increment < number):
        increment = increment + 1
        data+= str(increment)
        

        #s.sendall(data.encode('utf-8'))
        #Sending response
        print("Sending %s" % data)
        s.sendto(data.encode('utf-8'), server_address)
        data = data[:-1]
        

        # Receiving response
        print("Waiting to receive response")
        sender=s.recvfrom(port)
        print(" Response received %s" % data)

s.shutdown(1)

