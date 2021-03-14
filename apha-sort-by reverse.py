name = input("Enter your name \n").upper()

for i in name:
    d=ord(i)%65
    s=90-d
    print(chr(s),end=" ")