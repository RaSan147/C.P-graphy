input()
arr = input().split()
item = input()
print(arr.index(item) if item in arr else -1)