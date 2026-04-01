from collections import Counter


input()

c = Counter(map(int, input().split()))


to_remove = 0
for i, count in c.items():
	if count > i:
		to_remove += count - i
	elif count < i:
		to_remove += count
		

print(to_remove)