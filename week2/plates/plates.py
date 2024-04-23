def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if "." in s or " " in s:
        return False
    if "0" in s and s.find("0") != len(s) - 1:
        return False
    for k, c in enumerate(s):
        if c.isdigit() and k + 1 < len(s) and s[k + 1].isalpha():
            return False
    return True


main()
