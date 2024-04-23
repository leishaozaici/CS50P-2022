import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if len(ip.replace(".", "")) != len(ip) - 3:
        return False
    obj = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if obj:
        for i in range(1, 5):
            d = int(obj.group(i))
            if d < 0 or d > 255:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()
