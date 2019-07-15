import socket

students = []
with open('student_information', 'r+') as f:
    for line in f:
        students.append(line.strip().split(" "))

s = socket.socket()
# 获取本地 IP 地址
ip_address = socket.gethostbyname(socket.gethostname())
s.bind((ip_address, 8888))
s.listen(0)

print("server ip address:", ip_address)

while True:
    print('waiting for a connection')
    connection, client_address = s.accept()
    try:
        print('connected from', client_address)
        connection.send(str("你已成功连接").encode("utf-8"))

        while True:
            data = connection.recv(1024).decode("utf-8")
            if data:
                # 业务逻辑处理
                print(list(client_address)[0], end="")
                print(":%s" % data)
                new_data = str(input("请输入要发送的消息:")).encode("utf-8")
                connection.send(new_data)
    finally:
        connection.close()
