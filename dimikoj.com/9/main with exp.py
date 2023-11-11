# https://dimikoj.com/problems/9/square-number

from math import sqrt

for T in range(int(input())):
	sq = sqrt(int(input()))

	# now we just gotta check if the number is a float or integer
	print("NO" if int(sq)!=sq else "YES")  