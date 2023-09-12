import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches:= re.search(r"(\d\d?):(\d\d) [AP]M to (\d\d?):(\d\d) [AP]M", s):
        h1, m1, h2, m2 = matches.groups()
        if not 0 <= int(m1) < 60:
            raise ValueError
        if not 0 <= int(m2) < 60:
            raise ValueError

        return h1, m1, h2, m2

if __name__ == "__main__":
    main()