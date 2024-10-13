'''
FUNCTIONS
'''

# forward reference - works like a prototype
def get_str() -> str: ...

print(get_str())

def get_str():
	return "hello world"
