import requests
import json
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    n = float(sys.argv[1])
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    print(response.json()['bpi']['USD']['rate_float'])
    #print(json.dumps(response.json(), indent=2))

except requests.RequestException:
    pass
except ValueError:
    sys.exit("Command-line is not a number")