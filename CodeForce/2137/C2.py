from sys import stdin, stdout
import math

input = stdin.readline
print = stdout.write

ab = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    ab.append((a,b))
    
def solver(a, b):
    """Generate only divisors d of b that make x even."""
    res = -1
    
    # b_mod4 = not (b & 3)
    a_odd = a & 1
    b_odd = b & 1
    
    
    def ranger(p):
    	root = int(math.isqrt(p))
    	
    	if b_odd:
    		return range(1, root+1, 2)
    	return range(1, root+1)

    for d in ranger(b):
        q, r = divmod(b,d)
        if not r:
            # test both d and q
            for val, v2 in ((d, q), (q, d)):
                val_odd = val & 1
                v2_e = not v2 & 1
                if (
                	(a_odd and b_odd and val_odd)     # case 1
                    or  ((not a_odd or not val_odd) and v2_e)
                 ):         # case 3
                    s = a*val + v2
                    if s > res:
                        res = s
    return res

gs = []
for a,b in ab:
    m = -1
    g = solver(a, b)
    gs.append(str(g))
    
print("\n".join(gs))