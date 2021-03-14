lt = []
i = True
while i:
    try:
        n = input("Enter a number: ")
        if n.lower() == "completed":
            print("Maximum is ", max(lt))
            print("Minimum is ", min(lt))
            break
        lt.append(int(n))
    except ValueError as e:
        print("Invalid input ")
