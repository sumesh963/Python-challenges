import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.0.100",1234))
print("Binded")
sock.listen(5)
print("Listening")
c, addr = sock.accept()
print("Connection received: ", addr)
c.send("You can start sending your messages".encode())
c.send("server".encode())
while True:
    print("client->",end=" ")
    data = c.recv(1024).decode()
    if data == "quit":
        print("Ending Connection now")
        c.send("Ending the connection now".encode())
        break
    print(data)
    msg = input("Server->")
    c.send(msg.encode())
    if msg == "quit":
        print("Ending Connection now")
        c.send("Ending the connection now".encode())
        break
sock.close()