import sys
import csv
import PIL
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")
elif os.path.splitext(sys.argv[1])[1].lower() not in [".jpg", ".jpeg", ".png"] or os.path.splitext(sys.argv[2])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit(")