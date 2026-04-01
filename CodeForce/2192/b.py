def flip_except_n(x, n, width):
    return x ^ (((1 << width) - 1) ^ (1 << n))


class NeX(Exception):
	pass

for _ in range(int(input())):
	n = int(input())
	s = input().strip()
	si = int(s, 2)

	def counts1():
		return si.bit_count()
	def counts2():
		return n - si.bit_count()

	flipped = set()

	def positions_of_ones(x):
		positions = set()
		pos = 0
		while x:
			if x & 1 and pos not in flipped:
				positions.add(pos)
			x >>= 1
			pos += 1
		return positions

	def positions_of_zeros(x, width):
		zeros = set()
		for i in range(width):
			if not (x & (1 << i)) and i not in flipped:
				zeros.add(i)
		return zeros

	steps = 0

	picked = 1

	try:

		while si != 0:
			if picked == 1:
				positions = positions_of_ones(si)
				if len(positions) == 0:
					raise NeX()
				nxt = positions.pop()
				flipped.add(nxt)
				si = flip_except_n(si, nxt, n)
				picked = 0

			else:
				positions = positions_of_zeros(si, n)
				if len(positions) == 0:
					raise NeX()
				nxt = positions.pop()
				flipped.add(nxt)
				si = flip_except_n(si, nxt, n)
				picked = 1

	except NeX:
		print(-1)
		continue

	# print("=================")
	print(len(flipped))
	if len(flipped) > 0:
		print(" ".join(str(x+1) for x in flipped))
	# print("=================")


			


