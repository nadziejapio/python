import inflect
p = inflect.engine()

names = []
while True:
    try:
        i = input()
        names.append(i)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(names, final_sep=""))
        break