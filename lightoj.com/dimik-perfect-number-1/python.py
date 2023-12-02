def perfecto(num):
    if num <= 1:
        return False
    
    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if the number is in the form 2^(p-1) * (2^p - 1)
    p = 2
    while (2**p - 1) * (2**(p-1)) <= num:
        if num == (2**p - 1) * (2**(p-1)) and is_prime(2**p - 1) and is_prime(p):
            return True
        p += 1
    
    return False

		
T = input()

#for t in range(int(T)):
#	i = input()
for _ in range(int(T)):
	spot = int(input())
	
	if perfecto(spot):
		print(f"YES, {spot} is a perfect number!")
	else:
		print(f"NO, {spot} is not a perfect number!")