from sys import stdin, stdout
input = stdin.readline

from math import gcd
from itertools import permutations


for _ in range(int(input())):
	input()
	xx = tuple(map(int, input().split()))

	for yy in permutations(xx):
		if all(gcd(xx[i]+yy[i], xx[i+1]+ yy[i+1])>2 for i in range(len(xx)-1)):
			print(*yy)
			break

	# print([gcd(xb[i]+yy[i], xb[i+1]+ yy[i+1]) for i in range(len(xx)-1)])