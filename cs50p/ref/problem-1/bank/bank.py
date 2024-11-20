greeting = input('Greeting: ').strip().lower()
if greeting[:5]=='hello':
	print('$0')
elif greeting[0]=='h' and greeting[:5]!='hello':
	print('$20')
elif len(greeting)<=1:
	print('$100')
else:
	print('$100')
