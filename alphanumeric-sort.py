name= input("Enter an alphanumeric string \n")
a=""
n=""
l=""
u=""
e=[]
o=[]
e1=""
o1=""
for i in name:
    if i.isalpha():
        a=a+i
    elif i.isdigit():
        n=n+i
for j in a:
    if j.islower():
        l=l+j

    else:
        u=u+j
print(l[::-1]+u[::-1],end="")
for k in n:
    if int(k)%2==0:
        e.append(int(k))
        e.sort()
    else:
        o.append(int(k))
        o.sort()
for j in o:
    e1=e1+str(j)
for i in e:
    e1=e1+str(i)
print(e1)