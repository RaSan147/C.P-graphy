from urllib.parse import urljoin

pwd = '/'

for _ in range(int(input())):
	i = input().split()
	if i[0] == 'pwd':
		print(pwd)

	if i[0] == 'cd':
		if i[1] == '/':
			pwd = '/'
		else:
			pwd = urljoin(pwd, i[1] + '/')
