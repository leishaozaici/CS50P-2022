import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
try:
    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        table = [x for x in reader]
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
