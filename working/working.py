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
        if a1 == "AM":
            if h1 == "12":
                h1 = 00
        if a2 == "AM":
            if h2 == "12":
                h2 = 00
        if a1 == "PM":
            if h1 == "12":
                h1 = 12
            else:
                h1 = int(h1) + 12
        if a2 == "PM":
            if h2 == "12":
                h2 = 12
            else:
                h2 = int(h2) + 12

        return f"{int(h1):02}:{m1} to {int(h2):02}:{m2}"
    else:
        raise ValueError
if __name__ == "__main__":
    main()