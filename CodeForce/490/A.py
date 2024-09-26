studs = {'1': [], '2': [], '3': []}
input(), [studs[i].append(n) for n, i in enumerate(input().split(), 1)]
print(min(map(len, studs.values())), *[' '.join(map(str, tup)) for tup in zip(*studs.values())], sep='\n')
# input() # ignore
# studs = {'1': [], '2': [], '3': []}
# for n, i in enumerate(input().split(), 1):
# 	studs[i].append(int(n))
# print(min(map(len, studs.values())))
# for i in zip(*studs.values()):
# 	print(*i)