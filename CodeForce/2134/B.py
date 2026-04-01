# https://codeforces.com/contest/2134/problem/B
# https://chatgpt.com/share/68bc987c-6214-800e-9559-61233f68265f


from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def to_multiple(x, k):
	x = int(x)
	return str(x + (x%(k+1))*k)

for _ in range(int(input())):
	n, k = map(int, input().split())
	# a = list(map(to_multiple, input().split()))
	a = (to_multiple(x, k) for x in input().split())

	print(' '.join(a) + '\n')
