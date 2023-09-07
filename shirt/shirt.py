import sys
import csv
import PIL
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")

in_ext_1 = os.path.splitext(sys.argv[1])[1].lower()
in_ext_2 = os.path.splitext(sys.argv[1])[1].lower()

if in_ext_1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif in_ext_2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalif output")
elif in_ext_1 != in_ext_2:
    sys.exit("Input and output have different extensions")
else:
    try:
        
    except FileNotFoundError:
        sys.exit("Input does not exist")