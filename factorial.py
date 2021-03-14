num=int(input("Enter a Positive number to get its' factorial \n"))
fact=1
for i in range(1,num + 1):
       fact = fact*i
print("The factorial of",num,"is",fact)