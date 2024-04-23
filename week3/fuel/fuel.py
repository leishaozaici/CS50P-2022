while True:
    try:
        x, y = input("Fraction: ").split("/")
        ans = round(int(x) / int(y) * 100)
        if int(x) > int(y):
            continue
        print("E" if ans <= 1 else "F" if ans >= 99 else f"{ans}%")
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break
