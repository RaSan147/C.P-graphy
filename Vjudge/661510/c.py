from itertools import permutations 


for T in range(int(input())):
	l, t = map(int, input().split())
	# Get all permutations of [1, 2, 3] 
	perm = permutations("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:l])
	
	# Print the obtained permutations 
	print(f"Case {T+1}:")
	for n, i in enumerate(perm, 1): 
		print(''.join(i))
		if n == t:
			break