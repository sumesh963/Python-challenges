import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.100" # server address
port = 1234 #server port
s.connect((host,port))
print(s.recv(1024).decode())
print(s.recv(1024).decode())
while True:
    message = input("client-> ")
    s.send(message.encode()) #sending message to the server.
    if message == "quit":
        print(s.recv(1024).decode())
        break
    print("Server->",end=" ")
    d=s.recv(1024).decode()
    if d == "quit":
        print("Ending Connection now")
        print(d)
        break
    else:
        print(d)
        continue
s.close()
