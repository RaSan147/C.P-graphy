
V = "aeiou"

for T in range(int(input())):
	if T:
		print()
	txt = input()
	_v = "".join([c for c in txt if c in V])
	_c = "".join([c for c in txt if (c not in V and c!=" ")])

	print(_v)
	print(_c, end='')