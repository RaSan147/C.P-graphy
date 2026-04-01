from collections import Counter

for _ in range(int(input())):
	input()
	arr = Counter(int(i) for i in input().split())

	s = int(sum([(x - x % n) for n, x in arr.items()]))

	print(">>", s)
