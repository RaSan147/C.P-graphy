from sys import stdin, stdout
input = stdin.readline



for _ in range(int(input())):
	kk, x = tuple(map(int, input().split()))

	for k in range(kk):
		if x%2:
			x*=2
		else:

			# x_= (x-1)%3
			# if x_:
			# 	x*=2
			# else:
			# 	x = (x-1)/3
			if (x-1)%3:
				x *= 2
			else:
				x = (x-1)/3

	print(int(x))
