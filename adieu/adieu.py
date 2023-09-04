import inflect
p = inflect.engine()

names = []
while True:
    try:
        i = input("Name: ")
        names.append(i)
    except EOFError:
        print("Adieu, adieu, to", p.join(names, final_sep=""))
        break