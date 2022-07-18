from cs50 import get_float

# main


def main():
    n = get_change()
    n = round(n*100)
    q = int(n / 25)
    d = int((n - (q * 25)) / 10)
    i = int((n - (q * 25) - (d * 10)) / 5)
    p = int(n - (q * 25) - (d * 10) - (i * 5))
    print(f"{q + d + i + p}")

# get input


def get_change():
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            break
    return n


# execute
main()