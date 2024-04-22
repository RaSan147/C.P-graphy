from string import ascii_lowercase, ascii_uppercase
import sys
from collections import deque

def main():
	small = deque()
	cap = deque()
	inp = input()
	for n, c in enumerate(inp):
		if c == 'b':
			size = n
			if not (size and small):
				continue
			
			small.pop()
		elif c == 'B':
			size = n
			if not (size and cap):
				continue
				
			cap.pop()
					
		else:
			if c in ascii_lowercase:
				small.append(n)
			else:
				cap.append(n)
			
	#print([cap, small])
	for n in range(len(inp)):
		if (cap and n==cap[0]):
			sys.stdout.write(inp[n])
			cap.popleft()
			
		if (small and n==small[0]):
			sys.stdout.write(inp[n])
			small.popleft()
			
			
			
			
	print()
			
	
for _ in range(int(input())):
	main()