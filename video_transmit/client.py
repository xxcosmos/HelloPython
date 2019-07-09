import cv2
import numpy
import socket
import struct

HOST = '192.168.12.1'
PORT = 9999
buffSize = 65535

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print('now waiting for frames')

while True:
    data, address = server.recvfrom(buffSize)
    if len(data) == 1 and data[0] == 1:
        server.close()
        cv2.destroyAllWindows()
        exit()
    if len(data) != 4:
        length = 0
    else:
        length = struct.unpack('i', data)[0]
    data, address = server.recvfrom(buffSize)
    if length != len(data):
        continue
    data = numpy.array(bytearray(data))
    image_decode = cv2.imdecode(data, 1)
    print('have received one frame')
    cv2.imshow('frame', image_decode)
    if cv2.waitKey(1) == 27:
        break
server.close()
cv2.destroyAllWindows()
