# num =int(input("Enter a range to find the fibonaci series"))
a=0
b=1
c=0
print("The Fibonaci series From 1 to 100 is ")
print(a,b,end=" ")
for i in range(0,10):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
