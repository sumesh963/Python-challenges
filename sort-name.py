name =input("Enter the list of name \n")
n=list(name.split(" "))
j=[]
s=sorted(n)
print(s)
for i in s:

    m=sorted(i)
    o="".join(m)
    j.append(o)

print(j)