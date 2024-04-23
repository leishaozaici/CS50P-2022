from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
f = None
arg2 = sys.argv[1]
if len(sys.argv) >= 2:
    if ("-f" != arg2 and "--font" != arg2) or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        f = sys.argv[2]
else:
    f = random.choice(fonts)
figlet.setFont(font=f)
print(figlet.renderText(input("Input: ")))
