#From ChatGPT:
#Uses a |||dictionary|||
def get_file_type(filename):
	file_extension = filename.split(".")[-1].lower()
	file_types = {
		"gif": "image/gif",
		"png": "image/png",
		"jpg": "image/jpeg",
		"jpeg": "image/jpeg",
		"pdf": "application/pdf",
		"txt": "text/plain",
		"zip": "application/zip"
	}
	return file_types.get(file_extension, "application/octet-stream")

filename = input("File name: ").strip()
file_type = get_file_type(filename)
print(file_type)



# Faulty solution
# Unable to handle e.g. hand.txt.pdf
'''
def properfile(f):
	global file, filetype
	try:
		file,filetype=f.split(".")
		return True
	except ValueError:
		return False

name=input("File name: ").lower().strip()
if properfile(name)==False:
	print("application/octet-stream")
elif properfile(name)==True:
	match filetype:
		case "gif" | "png":
			print("image/"+filetype)
		case "jpg" | "jpeg":
			print("image/jpeg")
		case "pdf" | "txt" | "zip":
			print("application/"+filetype)
		case _:
			print("application/octet-stream")
'''
#Beginner solution
'''
name=input("File name: ").lower().strip()
if name.ends_with("png"):
	print("image/png")
#and so on
'''
