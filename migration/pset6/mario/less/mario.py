from cs50 import get_int
# main


def main():
    n = get_pint()
    for i in range(n):
        space(n - i - 1)
        for j in range(i + 1):
            print("#", end="")
        print()

# spaces


def space(i):

    for n in range(i):
        print(" ", end="")

# get positive int


def get_pint():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:
            break
    return n


# execute
main()