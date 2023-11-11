
from math import sqrt

for T in range(int(input())):
	sq = sqrt(int(input()))
	print(sq)
	print("NO" if sq%1>=1 else "YES")  