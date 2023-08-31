while True:
    try:
        x,y = input("Fraction: ").split("/")
        ans = int(x)/int(y)*100
        if ans > 98:
            print("F")
        elif ans < 2:
            print ("E")
        elif ans > 100:
            continue
        else:
            print(f"{round(ans)}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
