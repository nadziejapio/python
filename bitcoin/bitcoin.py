import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    n = float(sys.argv[1])
    response = request.response('https://api.coindesk.com/v1/bpi/currentprice.json')
    print(response.json())

except requests.RequestException:

except ValueError:
    sys.exit("Command-line is not a number")