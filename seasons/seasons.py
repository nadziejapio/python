from datetime import date
from os import sys
import inflect

p = inflect.engine()

def main():
    today = date.today()
    try:
        subs = today - get_date(input("Date of Birth: "))
    except Exception:
        sys.exit("Invalid date")
    mins = subs.days * 24 * 60
    print(p.number_to_words(mins, andword="").title() + " minutes")

def get_date(s):
    return date.fromisoformat(s)


if __name__ == "__main__":
    main()
