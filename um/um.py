import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ans = re.findall(r"\b[Uu]m\b", s)
    return len(ans)

if __name__ == "__main__":
    main()