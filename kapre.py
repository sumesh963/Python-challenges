num1 = int(input("Enter a number \n"))
s = len(str(num1))
str1 = str(num1 * num1)
#print("Square of the number is",str1)
while (len(str1) / 2) != s:
    str1 = "0" + str1

num2 = ""
num3 = ""
for eq1 in range(int(len(str1) / 2)):
    num2 += str1[eq1]
#print(num2)
for eq2 in range(int(len(str1) / 2), len(str1)):
    num3 += str1[eq2]
#print(num3)
add = int(num2) + int(num3)

if add == num1:
    #print(num1,"is equal to", add)
    print("It is kaprekar number")
else:
    #print(num1,"is not equal to ",add)
    print("It is not a kaprekar number")
