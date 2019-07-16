import socket
import threading
import json


def send_student_list(connection):
    connection.send(bytes(repr(json.dumps(students)).encode('utf-8')))


def delete_student(student_id):
    is_deleted = 0
    for s in students:
        if s[0] == student_id:
            is_deleted = 1
            students.remove(s)
            break
    connection.sendall(str(is_deleted).encode('utf-8'))


def data_procession(data, connection):
    if data:
        print("receive data is ", data)
        command, data = data.split(" ")
        if command == "1":
            send_student_list(connection)
        elif command == "4":
            delete_student(data)


def on_new_connection(s, connection, client_address):
    print('connected from', client_address)
    while True:
        data = s.recv(1024).decode("utf-8")
        data_procession(data, connection)


def build_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_address = socket.gethostbyname(socket.gethostname())
    print("server ip address:", ip_address)
    s.bind((ip_address, port))
    s.listen(0)
    print('waiting for a connection')
    return s


students = []
with open('student_information', 'r+') as f:
    for line in f:
        students.append(line.strip().split(" "))

s = build_socket(8888)

while True:
    connection, client_address = s.accept()
    on_new_connection(s, connection, client_address)
