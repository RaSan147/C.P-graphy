Q = int(input())
arr = []
for _ in range(Q):
	q = input().split()

	if q[0]=='0':
		arr.append(q[1])
	if q[0]=='1':
		print(arr[int(q[1])])
	if q[0]=='2':
		arr.pop()

