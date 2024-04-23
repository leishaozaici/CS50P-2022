import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
count = 0
try:
    with open(sys.argv[1]) as f:
        for line in f:
            if not line.lstrip().startswith("#") and len(line.lstrip()) != 0:
                count += 1
except FileNotFoundError:
    pass
else:
    print(count)
