# import socket
# import time
#
# host = '192.168.12.1'
# port = 8001
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((host, port))
# sock.listen(5)
# while True:
#     connection, address = sock.accept()
#     try:
#         connection.settimeout(10)
#         buf = connection.recv(1024)
#         if buf:
#             connection.send(b'welcome to server!')
#             print('Connection success')
