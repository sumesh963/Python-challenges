name = input("Enter a string \n")
num = int(input("Enter a number to wrap the string \n"))
j=0
while (j<len(name)):
    print(name[j:j+num],end="\n")
    j=j+num




