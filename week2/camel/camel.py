s = input("camelCase: ")
for c in s:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")
