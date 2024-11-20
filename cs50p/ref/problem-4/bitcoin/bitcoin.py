import requests
import sys
from json import dumps

def isfloat(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json?amount=1")
feedback=url.json()
print(dumps(feedback, indent = 2))

try:
	# calculates the price of n bitcoin
	price = feedback["bpi"]["USD"]["rate_float"] * float(sys.argv[1])
except ValueError:
	sys.exit("Command-line argument is not a number")
except IndexError:
	sys.exit("Missing command-line argument")
else:
	print(f"${price:,}")
