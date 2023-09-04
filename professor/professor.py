import random

def main():
    while True:
        i = input("")

def get_level():
    while True:
        try:
            i = int(input("Level: "))
            if i in [1,2,3]:
                return i
            else:
                continue
        except Exceptation:
            continue

def generate_integer(level):
    i = random.randrange(10^(level-1), 10^level)
    return i

if __name__ == "__main__":
    main()