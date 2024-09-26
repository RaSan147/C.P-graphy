input()

[print('A[{}] = {}'.format(i, x)) for i, x in enumerate(input().split()) if int(x) <=10]