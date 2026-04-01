class block:
	def __init__(self, char, count):
		self.char = char
		self.count = count

for _ in range(int(input())):
	__ = input()
	s = input()

	blocks = []
	for c in s:
		if len(blocks) == 0 or blocks[-1].char != c:
			blocks.append(block(c, 1))
		else:
			blocks[-1].count += 1

	if len(blocks) == 0:
		print(0)
		continue

	if len(blocks) == 1:
		print(1)
		continue

	if len(blocks) == 2:
		# ab
		if blocks[0].count == 1 and blocks[1].count == 1:
			print(2)
			continue
		else:
			print(3)
			continue
			

	if blocks[0].char == blocks[-1].char:
		# if blocks[0].count == 1 and blocks[-1].count == 1:
			# abbbccca
			# bcccaabb
			# ccaabbbc
			# abbbdccca

		print(len(blocks))
		continue 
	else:
		# abccca
		# bcccaab
		# ccaabbc
		if any(blocks[i].count > 1 for i in range(1, len(blocks) - 1)):
			print(len(blocks) + 1)
			continue

		print(len(blocks))
		continue

