# solution on 110100
from math import sqrt, ceil, floor


def sqrt_up_n_down(n):
	m = n-1
	x = m*2
	s = sqrt(x)
	up = ceil(s)
	base = floor(s)
	if up==base: up+=1
	down = base-1

	#print([x, s, base, up, base*up, n])
	if x == base*up:
		return (1)
	else:
		return (0)
		

for i in range(int(input())):
	spot = int(input())
	
	print(sqrt_up_n_down(spot), end=' ')

