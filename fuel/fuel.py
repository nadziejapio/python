while True:
    x,y = input("Fraction: ").split("/")
    try:
        ans = int(x)/int(y)*100
        print(f"{ans}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
