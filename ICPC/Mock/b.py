import math


for t in range(int(input())):
	a, b = input().split()
	oA = ord(a)-32
	oB = ord(b)-32

	for RL in range(1, 95):
		CL = math.ceil(94/RL)

		if oA % RL == oB % RL:

			print(RL, CL)

	print()

