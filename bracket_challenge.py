n = int(input())
lt = []
d = {"{":"}","(":")","[":"]"}
k = 0
e = 1
r = []
for i in range(n):
    b = input()
    rev_b = b[::-1]
    l = int(len(b) / 2)
    for i in b:
        if e == 0 or k == l:
            break
        for j in range(l):
            if d[i] == rev_b[j + k]:
                break
            else:
                e = 0
                break
        k += 1
    if e == 1:
        r.append("Yes")
    else:
        r.append("No")
for i in r:
    print(i)
