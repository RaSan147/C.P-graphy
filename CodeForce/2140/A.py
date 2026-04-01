import sys

input = sys.stdin.readline
o = []
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    c = s.count('0')
    m = s[0:c].count('1')

    o.append(str(m))

print("\n".join(o))
