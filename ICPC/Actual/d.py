MOD = 998244353

def modular_inverse(x, mod):
    return pow(x, mod - 2, mod)

def solve(n, red_weights, green_weights):
    # Step 1: Calculate expected weights for each box
    expected_weights = [(r + g) / 2 for r, g in zip(red_weights, green_weights)]
    
    # Step 2: Sort expected weights in descending order
    expected_weights.sort(reverse=True)
    
    # Step 3: Compute prefix sums for expected weights
    prefix_sum = [0] * n
    prefix_sum[0] = expected_weights[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + expected_weights[i]
    
    # Step 4: Calculate results for each K from 1 to N
    results = []
    power_of_2 = 1  # this will be 2^K as K grows
    for k in range(1, n + 1):
        total_expected_weight = int(prefix_sum[k - 1] * power_of_2) % MOD
        mod_inverse_of_2k = modular_inverse(power_of_2, MOD)
        result = (total_expected_weight * mod_inverse_of_2k) % MOD
        results.append(result)
        power_of_2 = (power_of_2 * 2) % MOD  # increment 2^K
    
    print(" ".join(map(str, results)))

# Example usage:
n = 10
red_weights = [3, 1,5,3,1,3,5,4,2,2]
green_weights = [3,3,1,2,2,5,3,5,1,5]
solve(n, red_weights, green_weights)
