from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    s = input("Date of Birth: ")
    if len(s.split("-")) != 3:
        sys.exit("Invalid date")

    print(convert(s))


def convert(s):
    d = date.fromisoformat(s)
    return (
        p.number_to_words(
            round(((date.today() - d).days) * 24 * 60), andword=""
        ).capitalize()
        + " minutes"
    )


if __name__ == "__main__":
    main()
