'''
FUNCTIONS
'''

# forward reference - works like a prototype
def get_str() -> str: ...

print(get_str())

def get_str():
	return "hello world"
# ============================================================= #

# how to state param datatype
def prt(msg : str):
	print(msg)

# show function return value:

# multiple return value
from typing import Tuple

def rt() -> Tuple[int, str]:
	return 1, "hello"

def ab() -> Tuple[int, str]:
	a: int = 1
	b: str = "hello"
	return a, b

from typing import Union

def process(value: int) -> Union[int, str]:
	if value > 0:
		return value * 2  # Returns an integer
	else:
		return "Negative value"  # Returns a string


# one return value
def add(a: int, b: int) -> int:
	return a + b

