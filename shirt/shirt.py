import sys
import csv
import PIL
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")
elif sys.argv[1]