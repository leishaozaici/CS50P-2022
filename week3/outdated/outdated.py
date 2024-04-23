mon = [
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
    "December",
]
while True:
    try:
        s = input("Date: ").strip()
        if " " in s:
            m, d, y = s.split(" ")
            d = d.replace(",", "")
        else:
            m, d, y = s.split("/")
        if ((m in mon and "," in s) or int(m) <= 12) and int(d) <= 31:
            print(f"{y}-{mon.index(m)+1 if m in mon else int(m):02}-{int(d):02}")
            break
    except ValueError:
        pass
