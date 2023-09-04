import random
import sys

def main():
    lvl = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        answer = x + y
        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == answer:
                    if i == 0:
                        score += 1
                        break
                    else:
                        break
                else:
                    raise ValueError

            except ValueError:
                print("EEE")
                if i == 2:
                    print(f"{x} + {y} = {answer}")
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
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        i = random.randrange(10**(level-1)-1, 10**level-1)
    else:
        i = random.randrange(10**(level-1), 10**level-1)
    return i

if __name__ == "__main__":
    main()