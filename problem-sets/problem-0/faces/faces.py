def main():
	usr = input()
	convert(usr)

def convert(usr):
	usr = usr.replace(":)", "🙂")
	usr = usr.replace(":(", "🙁")
	print(usr)

if __name__ == '__main__':
	main()
	