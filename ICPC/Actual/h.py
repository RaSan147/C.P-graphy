def fact(n):
	return n
	res = 1
	while n:
		res = mod(res * n)
		n -= 1

	return res

def mod(x):
	return x #% 998244353

def main():
	for t in range(int(input())):
		n, m, k = map(int, input().split())

	print(mod((m-2) * fact(k-4)) * mod((n-2) * fact(k-4)) + (2*m + 2*n - 4) * mod(fact(k-2)))

main()