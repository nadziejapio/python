grocery_list = {}
while True:
    try:
        i = input().upper()
        if i in grocery_list:
            grocery_list[i] += 1
        else:
            grocery_list[i] = 1
    except EOFError:
        for j in grocery_list:
            print(grocery_list.get(j), j)
        break