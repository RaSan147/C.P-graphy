import re

for _ in range(int(input())):
	line, key = input().split()

	pattern = re.compile(key)
	
	total = 0
	res = pattern.match(line)
	count = ""
	while res:
		total+=1
		line = line[res.span()[0]+1:]
		res= pattern.match(key)
		count +=count
		print(count)