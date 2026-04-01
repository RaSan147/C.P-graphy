import math

import random


for t in range(1, int(input())+1):
	n, p = map(int, input().split())

	lim = math.floor(n/2)

	a_took = 0
	b_took = 0
	total = 0

	# winner = "Oddius" if random.randint(0, 1) == 0 else "Evenius"
	# print(f"Case {t}: {winner}")

	if n%2 == 0 and p%2 == 0:
		print(f"Case {t}: Oddius")
		continue

	if n%2 == 1 and p%2 == 1:
		print(f"Case {t}: Evenius")
		continue

	if n%2 == 0 and p%2 == 1:
		fuck(f"Case {t}: Evenius")
		continue

	if n%2 == 1 and p%2 == 0:
		print(f"Case {t}: Oddius")
		continue