import socket
import threading
import json


def send_student_list(connection):
    connection.send(bytes(repr(json.dumps(students)).encode('utf-8')))


def data_procession(data, connection):
    if data:
        print("receive data is ", data)
        if data == "1":
            send_student_list(connection)
        elif data == "2":
            pass


def on_new_connection(s, connection, client_address):
    print('connected from', client_address)
    try:
        while True:
            data = s.recv(1024).decode("utf-8")
            data_procession(data, connection)
    finally:
        connection.close()


def build_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_address = socket.gethostbyname(socket.gethostname())
    print("server ip address:", ip_address)
    s.bind((ip_address, port))
    s.listen(5)
    print('waiting for a connection')
    return s


students = []
with open('student_information', 'r+') as f:
    for line in f:
        students.append(line.strip().split(" "))

s = build_socket(8888)

while True:
    connection, client_address = s.accept()
    t = threading.Thread(target=on_new_connection, args=(s, connection, client_address))
    t.start()
