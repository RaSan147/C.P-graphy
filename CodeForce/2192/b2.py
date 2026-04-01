t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ones = s.count('1')
    
    # Impossible case
    if n % 2 == 0 and ones % 2 == 1:
        print(-1)
        continue
    
    result = []
    
    if ones % 2 == 0:
        # pick all 1s
        for i in range(n):
            if s[i] == '1':
                result.append(i + 1)
    else:
        # pick all 0s
        for i in range(n):
            if s[i] == '0':
                result.append(i + 1)
    
    print(len(result))
    if result:
        print(*result)
    else:
        print()