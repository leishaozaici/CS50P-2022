lis = {}
while True:
    try:
        item = input().upper()
        if item in lis:
            lis[item] += 1
        else:
            lis[item] = 1
    except EOFError:
        for k in sorted(lis):
            print(str(lis[k]) + " " + k)
        break
