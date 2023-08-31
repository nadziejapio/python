while True:
    try:
        x,y = input("Fraction: ").split("/")
        ans = int(x)/int(y)*100
        if ans > 100:
            continue
        elif ans < 2:
            print ("E")
        elif ans > 98:
            print("F")
        else:
            print(f"{round(ans)}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
