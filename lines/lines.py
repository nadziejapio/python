import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-lines arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        counter = 0
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.rstrip()
                if line.lstrip().startswith("#"):
                    continue
                elif line.startswith(" "):
                    print(line)
                    continue
                else:
                    counter += 1
        print(counter)
        sys.exit()
    except FileNotFoundError:
        sys.exit("File not found")