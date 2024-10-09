'''
DICTIONARIES
'''
# finding a key among a list of dicts
students = [
	{"name": "Chan", "age": 18},
	{"name": "Yeo", "age": 18}
]

find = "Chan"
for search in students:
	if search["name"] == find:
		print(search)
		# this is how you format the output
		print(search["name"], search["age"], sep = ',')

# finding one key from a single dict
ppl = {
	"Her": 18,
	"Ron": 18,
}
# for loop iterates thru the keys
# hence, search means the key
# ppl[search] prints out the value of key
find = "He"
for search in ppl:
	if find == search:
		print(search, ppl[search])
# one interesting trick:
# this also return an output because He is a substr of Her
# hence, He is in Her
find = "He"
for search in ppl:
	if find in search:
		print(search, ppl[search])
