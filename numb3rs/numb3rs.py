import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+).(\d+).(\d+).(\d+)$", ip):
        for i in matches.groups():
            if int(i) > 255:
                return False
        return True

if __name__ == "__main__":
    main()