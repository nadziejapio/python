import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-lines arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
i = sys.argv