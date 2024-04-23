def main():
    t = convert(input("What time is it? "))
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")


def convert(time):
    time_list = time.split(":")
    return float(time_list[0]) + float(time_list[1]) / 60


if __name__ == "__main__":
    main()
