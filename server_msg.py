import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("192.168.0.106",1234))
sock.listen(2)
print("Waiting for connection \n")
c,adr =sock.accept()
msg=c.recv(100)
print(msg.decode())
msg="what if you are client \n"
c.send(msg.encode("utf-8"))
sock.close()
