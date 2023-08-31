while True:
    try:
        x,y = input("Fraction: ").split("/")
        ans = int(x)/int(y)*100
        print(f"{int(ans)}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
