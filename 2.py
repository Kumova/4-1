nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def gen(*args, **kwargs):
	for i in (i for lst in nested_list for i in lst):
		yield i

for item in gen():
	print(item)

