def main():
    i = input("Fraction: ")
    convert(i)

def convert(fraction):
    x,y = fraction.split("/")
    while True:
        try:
            ans = round(int(x)/int(y)*100)
            

def gauge(percentage):

if __name__ == "__main__":
    main()
while True:
    try:
        x,y = input("Fraction: ").split("/")
        ans = int(x)/int(y)*100
        if ans > 100:
            continue
        elif ans < 2:
            print ("E")
        elif ans > 98:
            print("F")
        else:
            print(f"{round(ans)}%")
        break
    except (ValueError, ZeroDivisionError):
        continue

