import cv2
import numpy
import socket
import struct

HOST = '192.168.12.1'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.connect((HOST, PORT))
print('now start to send frames')

capture = cv2.VideoCapture(0)
try:
    while True:
        success, frame = capture.read()
        while not success and frame is None:
            success, frame = capture.read()
        result, image_encode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        server.sendall(struct.pack('i', image_encode.shape[0]))
        server.sendall(image_encode)
        print('have sent 1 frame')
except Exception as e:
    print(e)
    server.sendall(struct.pack('c', 1))
    capture.release()
    server.close()
