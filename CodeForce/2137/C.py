from sys import stdin, stdout
import bisect, math

input = stdin.readline

def sieve(limit: int):
    """Return a list of primes up to limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False
    return [i for i, v in enumerate(is_prime) if v]

primes = sieve(10**5)

def closest_prime_index(primes, b):
    """Return the index of the largest prime <= sqrt(b)."""
    root = math.isqrt(b)
    idx = bisect.bisect_right(primes, root) - 1
    return idx if idx >= 0 else None

def prime_factors(b):
    """Return the prime factorization of b as {p: exp}."""
    factors = {}
    idx = closest_prime_index(primes, b)
    if idx is not None:
        for i in range(idx, -1, -1):
            p = primes[i]
            if p * p > b:
                continue
            if b % p == 0:
                cnt = 0
                while b % p == 0:
                    b //= p
                    cnt += 1
                factors[p] = cnt
            if b == 1:
                break
    if b > 1:  # leftover prime
        factors[b] = factors.get(b, 0) + 1
    return factors

def all_divisors(factors):
    """Generate all divisors from prime factors."""
    divisors = [1]
    for p, exp in factors.items():
        new_divs = []
        for d in divisors:
            mul = 1
            for _ in range(exp):
                mul *= p
                new_divs.append(d * mul)
        divisors += new_divs
    return sorted(divisors)

cache = {}

for _ in range(int(input())):
    a, b = map(int, input().split())
    m = -1

    if b not in cache:
        pf = prime_factors(b)
        divs = all_divisors(pf)
        cache[b] = divs
    else:
        divs = cache[b]

    # print("Divisors:", divs)

    for d in divs:
        x = int(a*d + b//d)
        # print(x, d)
        if not x & 1:  # even
            m = max(m, x)

    print(m)
