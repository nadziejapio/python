i = input("camelCase: ")
for c in i:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()