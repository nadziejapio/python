import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")
else:
    try:
        
        with open('before.csv') as file:
            reader = csv.DictReader(file)
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')