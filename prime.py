num = int(input("Enter a number greater than 1 \n"))

if (num==1):
     print("Please Enter a number greater than 1")
else:
    for i in range(2,num):
        if(num%i==0):
            print("The number",num,"not a prime number")
            break

    else:
         print("The number",num, "is a prime number")


