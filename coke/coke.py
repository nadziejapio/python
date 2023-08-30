a = 50
while True:
    if a > 0:
        print ("Amount Due:", a)
        i = int(input("Insert Coin: "))
        if i == 25 or i == 10 or i == 5:
            a -= i
    else:
        print("Change Owed:", -a)
        break