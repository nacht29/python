# Just like what I did in the Einstein problem, I created a fucntion to check if the file has an extension
# I learned the f.split(".")[-1] method via ChatGPT
# I did this to handle the error incurred by filenames such as hi.txt.pdf as this allows me to just use the last part of the str
# In the full solution proposed by ChatGPT  dictionary is used. Please refer to extensions_alt.py
def properfile(f):
	global filetype
	try:
		filetype=f.split(".")[-1]
		return True
	except Exception:
		return False

name=input("File name: ").lower().strip()
if properfile(name)==False:
	print("application/octet-stream")
else:
	match filetype:
		case "gif" | "png":
			print("image/"+filetype)
		case "jpg" | "jpeg":
			print("image/jpeg")
		case "pdf" | "zip":
			print("application/"+filetype)
		case "txt":
			print("text/plain")
		case _:
			print("application/octet-stream")
