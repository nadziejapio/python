import random
import sys

def main():
    while True:
        i = input("Level: ")
        if i.isdecimal() and int(i)>0:
            guess(i)
        else:
            continue

def guess(level):
    number = random.randint(1, int(level))
    while True:
        g = input("Guess: ")
        if g.isdecimal():
            g = int(g)
            if g>number:
                print("Too large!")
                continue
            elif g<number:
                print("Too small!")
                continue
            else:
                sys.exit("Just right!")
        else:
            continue

if __name__ == "__main__":
    main()