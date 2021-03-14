t=int(input("Input :\n"))
l=[]
for i in range(0,t):
    a,o,k=input().split()
    m=int(min(a,o))
    n=int(max(a,o))
    e=False
    while int(k)>0:
        if n-m==0:
            e=True
            break
        else:
            m=m+1
            k=int(k)-1
            s=n-m
            e=False
    if e==True:
        l.append(0)
    else:
        l.append(s)
print("Output:")
for i in l:
    print(i)