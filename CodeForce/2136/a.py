# https://codeforces.com/contest/2136/problem/A


for n in range(int(input())):
	a,b,x,y = map(int, input().split())
	x,y = x-a, y-b
	if a<b:
		a,b=b,a
	if x<y:
		x,y=y,x
		
	if (a/2-1 > b):
		print("no")
	elif (x/2-1 > y):
		print("no")
	else:
		print("yes")