grocery_list = {}
while True:
    try:
        i = input().capitalize()
        if i in grocery_list:
            grocery_list[i] += 1
        else:
            grocery_list[i] = 1
    except EOFError:
        print(grocery_list)