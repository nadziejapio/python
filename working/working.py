import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches:= re.search(r"(\d\d?)(?::(\d\d))? ([AP]M) to (\d\d?)(?::(\d\d))? ([AP]M)", s):
        h1, m1, a1, h2, m2, a2 = matches.groups()
        if m1:
            if not 0 <= int(m1) < 60:
                raise ValueError
        else:
            m1 = "00"
        if m2:
            if not 0 <= int(m2) < 60:
                raise ValueError
        else:
            m2 = "00"

        if a1 == "PM":
            h1 = int(h1) + 12
        if a2 == "PM":
            h2 = int(h2) + 12

        return f"{h1}:{m1} to {h2}:{m2}"

if __name__ == "__main__":
    main()