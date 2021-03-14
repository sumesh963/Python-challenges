def add(v):
    name=v[0]
    s=0
    a=int(v[1])
    b=int(v[2])
    s=a+b
    print(f"The sum of {a} and {b} entered by {name}  is ",s)

name=input("Enter your name and enter 2 value to find their sum \n")
s=list(name.split())

add(s)