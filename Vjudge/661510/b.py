from collections import Counter

for t in range(int(input())):
	_ = input()

	arr = list(map(int, input().split()))

	count = Counter(arr)

	# get the most common element
	most_common = count.most_common(1)[0][0]
	# print('mc', most_common)

	print(len(arr) - count[most_common])



