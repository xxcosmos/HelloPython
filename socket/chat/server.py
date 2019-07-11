import socket

s = socket.socket()
ip_address = socket.gethostbyname(socket.gethostname())

s.bind((ip_address, 8888))
s.listen(1000)

print("server ip address:", ip_address)

while True:
    print('waiting for a connection')
    connection, client_address = s.accept()
    try:
        print('connected from', client_address)
        connection.send(str("now you are connected").encode("utf-8"))

        while True:
            data = connection.recv(1024).decode("utf-8")
            if data:
                print(list(client_address)[0], end="")
                print(":%s" % data)
                new_data = str(input("You:")).encode("utf-8")
                connection.send(new_data)
    finally:
        connection.close()
