# https://dimikoj.com/problems/9/square-number

from math import sqrt

for T in range(int(input())):
	sq = sqrt(int(input()))

	print("NO" if int(sq)!=sq else "YES")  