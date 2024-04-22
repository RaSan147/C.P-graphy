# write the seive of Eratosthenes
# to find all prime numbers up to 1000
# optimized by eliminating even numbers

from time import perf_counter




def seive_of_eratosthenes(LIMIT, seive):
	for i in range(3, LIMIT, 2):
		if seive[i // 2]:
			for j in range(i * i, LIMIT, i):
				seive[j // 2] = False

def is_prime(n, seive):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	return seive[n // 2]

def main(limit):
	LIMIT = limit
	seive = [True] * (LIMIT // 2)

	seive_of_eratosthenes(LIMIT, seive)


for t in range(10):
	start = perf_counter()
	main(int(1e6))
	end = perf_counter()

	print("Test case", t + 1,
		f"Time taken: {end - start:.6f}s")
