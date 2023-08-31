grocery_list = {}
while True:
    try:
        i = input().capitalize()
        if i in grocery_list:
            grocery_list[i] += 1
        else:
            
    except EOFError:
