import random

raw = [1, 2, 3]


def main():
    count = 0
    level = get_level()
    ans = 0
    while count < 10:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            t = input(f"{x} + {y} = ")
            if not is_valid(t) or int(t) != x + y:
                print("EEE")
                temp = 2
                while temp > 0:
                    t = input(f"{x} + {y} = ")
                    if not is_valid(t) or int(t) != x + y:
                        print("EEE")
                        temp -= 1
                    else:
                        break
                print(f"{x} + {y} = {x+y}")
            else:
                ans += 1
        except ValueError:
            pass
        else:
            count += 1
    print(f"Score: {ans}")


def is_valid(s):
    if s.isdigit():
        return True
    else:
        return False


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in raw:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level not in raw:
        raise ValueError
    else:
        return random.randrange(
            10 ** (level - 1) * (1 if level > 1 else 0), 10**level
        )


if __name__ == "__main__":
    main()
