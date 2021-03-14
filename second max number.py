num =int(input("Enter the numbers for the list \n"))
j=[]
for i in range(0,num):
    k=int(input("Enter the number to find second highest"))
    j.append(k)
j.sort(reverse=True)
print("The second largest number from the given list is",j,j[1])

