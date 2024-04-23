def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError
    if y == "0":
        raise ZeroDivisionError
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
