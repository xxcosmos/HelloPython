import socket
import cv2
import numpy

HOST = '192.168.12.128'
PORT = 9999
buffSize = 65535

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print('now waiting for frames...')
while True:
    data, address = server.recvfrom(buffSize)
    if len(data) == 1 and data[0] == 1:
        server.close()
        cv2.destroyAllWindows()
        exit()
    try:
        data = bytearray(data)
        print('have received one frame')
        data = numpy.array(data)
        imgdecode = cv2.imdecode(data, 1)  # 解码并窗口显示
        print("here i am")
        cv2.imshow('frames', imgdecode)
        if cv2.waitKey(1) == 27:  # 按下ESC退出
            break
    except:
        continue

server.close()
cv2.destroyAllWindows()
