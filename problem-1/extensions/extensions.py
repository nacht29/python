global img, app, txt

img = ["gif", "jpg", "jpeg", "png"]
app = ["zip", "pdf"]
txt = ["txt"]

def main():
	file = input("File name: ").lower().strip()
	if " " in file:
		print("Invalid file")
	else:
		find_extension(file)

def find_extension(file):
	file = file.split(".")
	match file[len(file) - 1]:
		case file if file in img:
			print(f"image/{file}")
		case file if file in app:
			print(f"application/{file}")
		case file if file in txt:
			print(f"text/{file}")
		case _:
			print("applicattion/octet-stream ")

if __name__ == '__main__':
	main()
