import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ans = re.findall(r"\bum\b", s)
    return count(ans)

if __name__ == "__main__":
    main()