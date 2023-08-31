menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        i = input("Item: ").title()
        if i in menu:
            total += menu[i]
            print(f"Total: ${format(total, '.2f')}")
        else:
            continue
    except EOFError:
        print()
        break
    except KeyError:
        continue