p = []
pal=[]

def prime(num):
    for i in range(1,num):
        for j in range(2,i):
            if(i%j==0):
              break
        else:
            p.append(i)
    return p
def palindrome(p):
    temp=p

    for k in temp:
        c=k
        reverse_num = 0
        while(k>0):
            digit=k%10
            reverse_num=reverse_num*10+digit
            k//=10

        if(c==reverse_num):
            pal.append(c)
    print(f"The list of Palindrome till {num} is ")
    for l in pal:
        print(l,end=" ")
num = int(input("Enter a number till which range you want to find the palindrome numbers \n"))
pr=prime(num)
palindrome(pr)




