def main():
    i = convert(input("What time is it? "))
    if 7 <= i <= 8:
        print("breakfest time")
    elif 12 <= i <= 13:
        print("lunch time")
    elif 18 <= i <= 19:
        print("dinner time")

def convert(time):
    h, m = int(time.split(":"))
    return h + (m/60)

main()