months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        m, d, y = input("Date: ").split("/")
        if int(d) in range(1,32):
            if m in months:
                print(f"{y}-{m}-{int(d):02}")
                break
            elif int(m) in range(1, 13):
                print(f"{y}-{int(m):02}-{int(d):02}")
                break
            else:
                continue
        else:
            continue
    except Exception:
        continue