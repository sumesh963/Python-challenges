import urllib.request
url = "https://raw.githubusercontent.com/noobsecurity/sample_data/master/log.txt"
req = urllib.request.urlopen(url)
lt = []
for i in req:
    i = i.decode('utf-8')
    try:
        if i.startswith("From"):
            s = i.split()
            p = s[2]
            lt.append(s[1])
    except IndexError as e:
        continue
for i in range(len(lt)):
    print("{}. {}".format(i+1, lt[i]))
print("\nThere are {} email ids in the file with From as the first word ".format(len(lt)))
