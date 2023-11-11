# https://dimikoj.com/problems/8/small-to-large

# WHERE IS THE FUN IF WE USE PYTHON .sort() OR sorted([1,3,2])
def sort_of_3(n1, n2, n3):
	# n1, n2, n3 will be our final sequence n1>n2>n3
	if n2 > n1: # if n2 is bigger than n1, we'll swap them to make n1 larger
		n1, n2 = n2, n1
	if n3 > n1: # if n3 is larger than n1, then its the largest, so we push n1, n2 back, and place n3 in n1
		n1, n2, n3 = n3, n1, n2
	if n3 > n2: # if n3 is larger than n2, then  we push n2 back, and place n3 in n2
		n2, n3 = n3, n2

	# since the question wants us in reverse order small to big...
	return n3, n2, n1

for T in range(int(input())):
	list_of_numerical_str = input().split()
	list_of_numbers = map(int, list_of_numerical_str) # convert ["1", "2"] -> [1, 2]
	print(f"Case {T+1}:", *sort_of_3(*list_of_numbers))



# The lazy Process:
"""
for T in range(int(input())):
	list_of_numerical_str = input().split()
	list_of_numbers = map(int, list_of_numerical_str) # convert ["1", "2"] -> [1, 2]

	sorted_list = sorted(list_of_numbers) # will auto sort it
	print(f"Case {T+1}:", *sorted_list)
"""
