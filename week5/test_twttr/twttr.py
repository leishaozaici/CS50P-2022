aeoi = ["a", "e", "i", "o", "u"]


def main():
    print(shorten(input("Input: ")))


def shorten(word):
    s = ""
    for c in word:
        if c.lower() not in aeoi:
            s += c
    return s


if __name__ == "__main__":
    main()
