import sys
import random
from figlet import Figlet

figlet = Figlet()

def main(argv):
	if set_figlet_font(argv):
		return 0
	else:
		sys.exit("Invalid usage")

def set_figlet_font(argv):
	font_list = figlet.getFonts()

if __name__ == "__main__":
	main(sys.argv)
