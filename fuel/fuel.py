while True:
    x = input("Fraction: ")
    try:
        x = round(float(x)*100)
        print(f"{x}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
