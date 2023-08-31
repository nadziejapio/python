while True:
    try:
        x,y = input("Fraction: ").split("/")
        ans = int(x)/int(y)*100
        if ans > 99:
            print("F")
        elif ans < 1:
            print ("E")
        else:
            print(f"{round(ans)}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
