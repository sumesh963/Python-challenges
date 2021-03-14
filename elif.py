name = input("What is your name? \n")
if (name.lower() == "alice"):
    print("Hi Alice")
else:
    age = int(input("what is your age"))

    if age <= 12:
        print("You are not Alice Kiddo")
    elif 100<age<=2000:
        print("You are not Alice grannie")
    elif age>2000:
        print("Unlike you Alice is not undead vampire")

