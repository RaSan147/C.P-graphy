[print(*n%4 and ['NO']or['YES']+[*range(2,n+1,2)]+[n+n//2-1]+[*range(1,n-1,2)]) for n in map(int, [*open(0)][1:])]