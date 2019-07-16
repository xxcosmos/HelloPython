import socket

s = socket.socket()

server = input("Enter Server IP:")
s.connect((server, 8888))

data = s.recv(1024).decode("utf-8")
print(server + ":", data)

while True:
    try:
        new_data = str(input("请输入要发送的消息:")).encode("utf-8")
        s.sendall(new_data)
        data = s.recv(1024).decode("utf-8")
        print(server, ":", data)
    finally:
        s.close()
