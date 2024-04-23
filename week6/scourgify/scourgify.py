import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    with open(sys.argv[1], "r", newline="") as inf, open(
        sys.argv[2], "w", newline=""
    ) as ouf:
        reader = csv.DictReader(inf)
        writer = csv.DictWriter(ouf, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            writer.writerow(
                {
                    "first": row["name"].split(",")[1].lstrip(),
                    "last": row["name"].split(",")[0],
                    "house": row["house"],
                }
            )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
