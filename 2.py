nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
for lst in nested_list:
    for i in lst:
        print(i)