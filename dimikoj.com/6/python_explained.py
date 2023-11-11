# https://dimikoj.com/problems/6/summation

for T in range(int(input())):
	x = input()
	list_of_ints = map(int,[x[0], x[-1]])
	r = sum(list_of_ints)
	# map(x, [1,2,3]) will return [x(1), x(2), x(3)]
	# sum([1,2,3]) => 6
	
	# why are we not doing mathematical operation by converting it to int
	# >> because converting a large number to int is CPU expensive and often used for server attacks. So it is less recommended to convert large string to int

	print(f"Sum = {r}")

	# The mathematical way :
	"""
	x = input()
	num = int(x) # a 5 digit number based on question
	_1 = num//10000 # will return the 1st digit (left most)
	_5 = num % 10 # will return the last digit

	r = _1 + _5
	
	print(f"Sum = {r}")
	"""