smallest = None
second_smallest = None

si = None
ssi = None

for i in range(int(input())):
	input()
	arr = list(map(int, input().split()))


	res = None

	for j in range(1,len(arr)):
		for i in range(j):

			xx = arr[i] + arr[j] + j - i
			if res is None or xx < res:
				res = xx


	print(res)