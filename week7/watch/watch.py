import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    obj = re.search(r"<iframe.*youtube.com/embed/(\w+).*</iframe>", s)
    if obj:
        return f"https://youtu.be/{obj.group(1)}"


if __name__ == "__main__":
    main()
