greeting = input('Greeting: ').strip().lower()
if greeting.startswith('hello'):
	print('$0')
elif greeting.startswith('h'):
	print('$20')
# elif len(greeting):
else:
	print('$100')
