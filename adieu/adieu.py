import inflect
p = inflect.engine()

names = []
while True:
    try:
        i = input()
        names.append(i)
    except EOFError:
        print("Adieu, adieu, to", p.join(names))
        break