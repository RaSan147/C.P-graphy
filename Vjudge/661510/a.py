# WA

scores = {
	'a': 0,
	'b': 0,
	'c': 0,
}
# sumA = (0, 'x')
# sumB = (0, 'x')
# sumC = (0, 'x')
# sumA_ = (0, 'x')
# for i in range(int(input())):
# 	a, b, c = map(int, input().split())
# 	scores['a'] = a
# 	scores['b'] = b
# 	scores['c'] = c


# 	if sumA[1] == 'x':
# 		sumA = (a, 'a')
# 		sumB = (b, 'b')
# 		sumC = (c, 'c')

# 	else:
# 		sumA_ = max([(scores[x], x) for x in scores if x != sumA[1]], key=lambda x: x[0])
# 		sumB_= max([(scores[x], x) for x in scores if x != sumB[1]], key=lambda x: x[0])
# 		sumC_ = max([(scores[x], x) for x in scores if x != sumC[1]], key=lambda x: x[0])

# 		sumA = (sumA[0] + sumA_[0], sumA_[1])
# 		sumB = (sumB[0] + sumB_[0], sumB_[1])
# 		sumC = (sumC[0] + sumC_[0], sumC_[1])


# print(max(sumA[0], sumB[0], sumC[0]))

current = 'x'
score = 0

limit = int(input())

cache = []

for i in range(limit):
	a, b, c = cache or map(int, input().split())
	cache = []
	scores['a'] = a
	scores['b'] = b
	scores['c'] = c

	other1, other2 = [(scores[x], x) for x in scores if x != current]
	if other1[0] == other2[0] and i < limit - 1:
		cache = [int(x) for x in input().split()]
		current1, current2 = other1[1], other2[1]




	current = other[1]
	score += other[0]

print(score)