import re
import sys


def main():
    print(convert(input("Hours: ")))


# 9:00 AM to 5:00 PM
# 9:30 AM to 5:30 PM
# 9:30 PM to 5:30 AM
# 12 AM to 10 PM
# 09:00 to 17:00
# 12:00 AM to 12:00 PM
# 00:00 to 12:00
def convert(s):
    pattern = re.compile(r"(\w\w?):?(..)* (AM|PM) to (\w\w?):?(..)* (PM|AM)")
    obj = re.search(pattern, s)
    if obj:
        try:
            t1 = int(obj.group(1))
            t3 = int(obj.group(4))
            t2 = int(obj.group(2))
            t4 = int(obj.group(5))
            if t2 >= 60 or t4 >= 60 or t1 > 12 or t3 > 12:
                raise ValueError
        except (IndexError, TypeError):
            t2 = 0
            t4 = 0
        if obj.group(3) == "PM":
            if t1 < 12:
                t1 += 12
            if t3 == 12:
                t3 = 0
        else:
            if t3 < 12:
                t3 += 12
            if t1 == 12:
                t1 = 0

        return f"{t1:02}:{t2:02} to {t3:02}:{t4:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
