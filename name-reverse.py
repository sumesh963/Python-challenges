name = input("Enter the names \n")
n=list(name.split(" "))
j=[]

for i in n:
    o = "".join(i)
    j.append(o[::-1])
    s=" ".join(j)
print("The reveresd name is\n",s)