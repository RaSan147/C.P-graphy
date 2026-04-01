class block:
	def __init__(self, char, count):
		self.char = char
		self.count = count

def count_blocks(s):
	blocks = []
	for c in s:
		if len(blocks) == 0 or blocks[-1].char != c:
			blocks.append(block(c, 1))
		else:
			blocks[-1].count += 1
	return blocks


def count_blocks(s, n=0):
	blocks = []
	for i in range(len(s)):
		ix = (i+n) % len(s)
		# print(ix, len(s))
		c = s[ix]
		if len(blocks) == 0 or blocks[-1].char != c:
			blocks.append(block(c, 1))
		else:
			blocks[-1].count += 1
	return blocks

for _ in range(int(input())):
	N = int(input())
	s = input()

	blocks = count_blocks(s)

	if len(blocks) == 0:
		print(0)
		continue

	if len(blocks) == 1:
		print(1)
		continue

	maxx = len(blocks)
	for i in range(1, N - 1):
		bs = count_blocks(s, i)
		maxx = max(maxx, len(bs))

	print(maxx)
