import inflect
import sys

p = inflect.engine()
li = []
while True:
    try:
        s = input()
        if not li:
            li.append("Adieu, adieu, to " + s)
        else:
            li.append(s)

    except EOFError:
        print(p.join(li, sep=","))
        sys.exit()
