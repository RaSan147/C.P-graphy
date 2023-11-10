# https://dimikoj.com/problems/8/small-to-large

def sort_of_3(n1, n2, n3):
	if n2 > n1:
		n1, n2 = n2, n1
	if n3 > n1:
		n1, n2, n3 = n3, n1, n2
	if n3 > n2:
		n1, n2, n3 = n1, n3, n2

	return n3, n2, n1

for T in range(int(input())):
	print(f"Case {T+1}:", *sort_of_3(*map(int, input().split())))
