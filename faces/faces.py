def convert(i):
    return i.replace(":)", "🙂").replace(":(", "🙁")

def main():
    i = input("Write with emoji. ")
    print(convert(i))

main()