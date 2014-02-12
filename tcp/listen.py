import socket
import sys


TCP_IP = '10.35.1.245'
TCP_PORT = 10010
BUFFER_SIZE = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
    data = s.recv(1024)
    if data:
        data = data.split()
    print data
#while 1:
#    data = ''
#    while 1:
#        data += s.recv(1)
#        if data[-1] == '\n':
#            break
#        if not data:
#            break
#    if not data:
#        break
#    data = data.split()
#    if data[0] == '9a10':
#        print data
