
i = input("Greeting: ")
if i.strip().lower().find("hello") == 0:
    print("$0")
elif i.strip().lower().find("h") == 0:
    print("$20")
else:
    print("$100")