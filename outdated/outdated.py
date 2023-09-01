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
    #try:
        i = input("Date: ")
        if i[0].isalpha():
            m, d, y = i.split()
            if d[-1] == ",":
                d = d.strip(',')
            else:
                continue
        else:
            m, d, y = i.split("/")

        m = m.strip()
        if int(d) in range(1,32):
            if m in months:
                print(f"{y}-{(int(months.index(m))+1):02}-{int(d[0]):02}")
                break
            elif int(m) in range(1, 13):
                print(f"{y}-{int(m):02}-{int(d):02}")
                break
            else:
                continue
        else:
            continue
    #except Exception:
    #  continue