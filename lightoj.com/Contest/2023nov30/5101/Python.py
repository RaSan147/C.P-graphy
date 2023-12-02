# https://lightoj.com/contest/2023nov30/arena/problem/5101


l = []

for _ in range(5):
	l.append(input().split('|'))

trans = list(map(list, zip(*l)))

input()

for _ in range(30):
	t = input()
	for n, c in enumerate(t):
		if c not in trans[n]:
			break

	else:
		print(t.upper())

	
