# import time, socket, sys
#
# new_socket = socket.socket()
# host_name = socket.gethostname()
# s_ip = socket.gethostbyname(host_name)
#
# port = 8080
#
# new_socket.bind((host_name, port))
# print("Binding successful!")
# print("This is your IP: ", s_ip)
#
# print("Binding successful!")
# print("This is your IP: ", s_ip)
#
name = input('Enter name: ')
#
# new_socket.listen(1)
#
# conn, add = new_socket.accept()
#
# print("Received connection from ", add[0])
# print('Connection Established. Connected From: ', add[0])
#
# client = (conn.recv(1024)).decode()
# print(client + ' has connected.')
#
# conn.send(name.encode())
# while True:
#     message = input('Me : ')
#     conn.send(message.encode())
#     message = conn.recv(1024)
#     message = message.decode()
#     print(client, ':', message)

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.0.100",1234))
print("Binded")
name = input('Enter name: ')
sock.listen(2)
print("Listening")
c, addr = sock.accept()
print("Connection received: ", addr)
client=(c.recv(1024).decode())
# c.send("You can start sending your messages".encode())
# c.send("server".encode())
c.send(name.encode())
while True:
    # print(data)
    msg = input("Server->")
    c.send(msg.encode())
    print("client->", end=" ")
    if msg == "quit":
        print("Ending Connection now")
        c.send("Ending the connection now".encode())
        break
    data = c.recv(1024).decode()
    if data == "quit":
        print("Ending Connection now")
        c.send("Ending the connection now".encode())
        break
sock.close()