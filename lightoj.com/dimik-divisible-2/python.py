# https://lightoj.com/problem/dimik-divisible-2

import sys

for t in range(int(input())):
	a, b, x = map(int, input().split(' '))

	H = max([a, b])
	L = min([a, b])

	n = L
	while True:
		M = H*n
		if M>x:
			break

		if M%L==0:
			sys.stdout.write(f'{M}\n')

		n += L

	sys.stdout.write("\n")
