import random

def main():
    lvl = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == (x+y):
                    if i == 0:
                        score += 1
                        break
                    else:
                        break
                else:
                    raise ValueError

            except ValueError:
                print("EEE")
                continue
    print("Score:", score)

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