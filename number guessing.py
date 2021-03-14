import random
print("For 1.easy (0-5) \n 2.hard(0-10) ")
choice = int(input("Enter the level \n"))

if (choice==1):
    num=int(input("Enter a number to Guess \n"))
    r=random.randint(0,5)
    # print(r)
    if (num==r):
        print("You Guessed it right")
    else:
        print("Sorry your Guess was wrong,correct guess was",r," try again")
elif (choice==2):
    num =int(input("Enter a number to Guess \n"))
    r=random.randint(0,10)
    if (num==r):
        print("You Guessed it right")
    else:
        print("Sorry your Guess was wrong,correct guess was",r," try again")

