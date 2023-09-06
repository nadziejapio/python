def main():
    while True:
        try:
            i = input("Fraction: ")
            print(f"{gauge(convert(i))}%")
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    x,y = fraction.split("/")
    ans = round(int(x)/int(y)*100)
    if ans > 100:
        raise ValueError
    elif y == "0":
        raise ZeroDivisionError
    else:
        return ans

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percantage}%"


if __name__ == "__main__":
    main()