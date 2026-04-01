for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    mx = 0
    
    for i in range(n):
        # Create rotation
        rs = s[i:] + s[:i]
        
        # Count blocks
        blocks = 1
        for j in range(1, n):
            if rs[j] != rs[j-1]:
                blocks += 1
        
        mx = max(mx, blocks)
    
    print(mx)