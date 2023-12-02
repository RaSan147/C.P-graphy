import itertools

lst = [0, 1, 2, 3, 4]

def permutations():
	for n in range(6):
		for i in itertools.combinations(lst, n):
			for p in itertools.permutations(i):
				yield p

# Now permutations is a list of all permutations of lst
# for perm in permutations():
# 	print(perm)

def str2bool(s):
	return [bool(int(i)) for i in s]
		
def get_one_positions(n):
	binary = bin(n)[2:]  # Convert to binary and remove '0b'
	positions = [len(binary) - i - 1 for i, bit in enumerate(binary) if bit == '1']
	return positions

def toggle_check(ip, pos, op):
	for p in pos:
		ip[p] = not ip[p]

	return ip == op


def main():
	i = str2bool(input())
	o = str2bool(input())

	forbidden = []
	input()
	for _ in range(10):
		forbidden.append(str2bool(input()))

	if i == o:
		print("YES")
		print(0)

	if o in forbidden:
		print("NO")
		return 0
	
	res = 10
	
	for p in permutations():
		if len(p)>res:
			continue
		ip = i.copy()
		for n in p:
			ip[n] = not ip[n]
			if ip in forbidden:
				break

		else:
			if ip == o:
				res = min(res, len(p))

	if not res == 10:
		print("YES")
		print(res)

main()