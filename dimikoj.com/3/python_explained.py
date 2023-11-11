# https://dimikoj.com/problems/3/descending-number

# there was a issue in the output test. they keep the \t even it should be the end of line


for i in range(1000,0,-1): # range in reverse order
	print(i, end="\t") # every number has a tab at the end of it

	# LETS DIVE INTO BETTER THINKING
	# 1000    999    998    997    996
	# lets % mod them with 5 (since we must have 5 numbers each line)
	# 0       4      3      2      1
	# thats the sequence we get for every lines of 5 numbers (if we start from 1000)
	# as we can see every time (num % 5) == 1; we gotta hit a new line
	if i%5==1:
		print()