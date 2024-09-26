input()

print(' '.join('0' if x == '0' else ('2' if x[0] == '-' else '1') for x in input().split()))