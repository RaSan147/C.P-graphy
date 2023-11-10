# https://dimikoj.com/problems/6/summation

for T in range(int(input())):
	x = input()
	r = sum(map(int,[x[0], x[-1]]))
	print(f"Sum = {r}")