input()
arr = list(map(int, input().split()))
mini = min(arr)
print(mini, arr.index(mini)+1)