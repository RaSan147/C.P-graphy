# https://dimikoj.com/problems/5/box-1

Times = int(input())

for T in range(Times):
	n = int(input()) # how many starts will be in 1 side
	line = "*"*n + "\n" # n times *, then a new line
	square = line*n # n times line will produce a square

	print(square)