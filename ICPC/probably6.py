# write the seive of Eratosthenes
# to find all prime numbers up to 1000
# optimized by eliminating even numbers

from time import perf_counter
from math import sqrt



def seive_of_eratosthenes(LIMIT):
	seive = [True] * (LIMIT + 1)
	seive[0] = seive[1] = False
	for i in range(2, int(sqrt(LIMIT))+1):
		print(i, seive[i])
		if seive[i]:
			print(i)
			for j in range(i * i, LIMIT+1, i):
				seive[j] = False

	return seive

def is_prime(n, seive):
	return seive[n]

def main(limit):
	LIMIT = limit

	seive = seive_of_eratosthenes(LIMIT)

	return seive

Limit = int(1e7)
Limit = 7

for t in range(10):
	start = perf_counter()
	s = main(Limit)
	end = perf_counter()

	print("Test case", t + 1,
		f"Time taken: {end - start:.6f}s")
	

print(s)
print(*[i for i in range(1, Limit+1) if s[i]], sep=", ")
