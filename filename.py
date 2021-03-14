filename = open("file.txt")
# print(filename.readlines())
l= filename.read().split("\n")
# print(l)
for i in l:
        # print(i)
        p = i.split()
        # print(p)
        print(f"Your username is {p[0]}  and password is {p[1]}")

filename.close()
