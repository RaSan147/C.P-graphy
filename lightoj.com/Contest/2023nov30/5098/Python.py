def sum_of_series(a, r, N):
    if r == 1:
        return a * N
    else:
        return a * ((r**N - 1) / (r - 1))

# Example usage:
a = 1 # is the first term of the series,
r = 2 # is the common ratio (in this case, the number you're raising to the power of N)
N = 4 # is the number of terms in the series.


Total_power = int(input())
base = int(input())

n = 1
sum = sum_of_series(a, base, n)

while sum<=Total_power:
    # print(sum)
    n += 1

    sum = sum_of_series(a, base, n)

print(n-1)

