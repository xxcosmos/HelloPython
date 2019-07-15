import socket


def build_socket(ip_address, port):
    s = socket.socket()
    s.connect((ip_address, port))
    return s


s = build_socket('192.168.1.241', 8888)
try:
    while True:
        new_data = str(input("请输入要发送的消息:")).encode("utf-8")
        s.sendall(new_data)
        data = s.recv(1024).decode("utf-8")
        print(data)
finally:
    s.close()
