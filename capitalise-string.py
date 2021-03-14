name = input("Enter a name \n")
n=list(name.split(" "))
j=[]

for i in n:
    j=i[0].upper()+i[1:len(i)]
    print(j,end=" ")



