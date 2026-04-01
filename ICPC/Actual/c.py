for t in range(1,int(input())+1):
	beds, days = map(int, input().split())
	count = 0
	for bed in range(beds):
		x, y = map(int, input().split())

		count += int(days//x)

	print(f"Case {t}: {count}")

