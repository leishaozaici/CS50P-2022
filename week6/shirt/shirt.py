import sys
from os.path import splitext
from PIL import Image, ImageOps

raw = [".jpg", ".jpeg", ".png"]
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
ext1 = splitext(sys.argv[1].lower())[1]
ext2 = splitext(sys.argv[2].lower())[1]
print(ext1, ext2)
if ext1 not in raw or ext2 not in raw:
    sys.exit("Invalid output")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")
try:
    ph2 = Image.open("shirt.png")
    ph1 = ImageOps.fit(Image.open(sys.argv[1]), ph2.size)
    ph1.paste(ph2, ph2)
    ph1.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
