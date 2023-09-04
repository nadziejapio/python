import requests
import sys

try:
    if len(sys.argv) != 2:
        print(""Missing )
    n = float(sys.argv[1])

except requests.RequestException:

except ValueError:
    sys.exit("Command-line is not a number")