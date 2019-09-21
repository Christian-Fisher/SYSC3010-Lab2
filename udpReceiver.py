# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

textport = sys.argv[1]
host = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    
    if not len(buf):
        break
    print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))
    print("ACK: %s" % buf)

    #if buf:
    #    messageSent = s.sendto(buf, address)
    #    print("sent %s bytes back to %s" % (messageSent, address))


    print ("Enter data to reply: ENTER to quit")
    datareceive = sys.stdin.readline().strip()

        #s.sendall(data.encode('utf-8'))
    #Sending response
    print("Sending %s" % datareceive)
    s.sendto(datareceive.encode('utf-8'), server_address)
        

    # Receiving response
    print("Waiting to receive response")
    sender=s.recvfrom(port)
    print(" Response received %s" % datareceive)
s.shutdown(1)
