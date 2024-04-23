import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dic = r.json()
    t = float(sys.argv[1])
except (requests.exceptions.JSONDecodeError, requests.RequestException):
    pass
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    print(f"${dic["bpi"]["USD"]["rate_float"]*t:,.4f}")
