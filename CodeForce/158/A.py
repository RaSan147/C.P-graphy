# https://codeforces.com/contest/158/problem/A

from collections import Counter
from sys import stdin, stdout
input = stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
s = sorted(c.keys(), reverse=True)

m = 0
for x in s:
	if x <= 0:
		break

	m += c[x]

	if m >= k:
		break
print(m)