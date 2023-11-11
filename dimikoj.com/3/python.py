# https://dimikoj.com/problems/3/descending-number

# there was a issue in the output test. they keep the \t even it should be the end of line

for i in range(1000,0,-1):
	print(i, end="\t")
	if i%5==1:
		print()