num =int(input("Enter a number : \n"))
temp=num
sum =0


while temp>0:
    i=temp%10
    sum=sum+i**3
    temp//=10



if sum==num:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")