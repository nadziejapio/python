import inflect
p = inflect.engine()

names = []
while True:
    try:
        i = input("Name: ")
        names.append(i)
    except EOFError:
        print(p.join((name for name in names), final_sep=""))