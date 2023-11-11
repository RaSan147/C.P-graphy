# https://dimikoj.com/problems/1/even-odd-1

Tests = int(input()) # lets take the total amount of test cases as 1st input and convert it to integer

for T in range(Tests): # For every number for 0 ... Tests
	data = input() # lets take the input number
	last_digit = int(data[-1]) # since we are getting even or odd, converting the entire text -> int is more CPU intensive (under the hood), so we only convert the last digit

	# lets divide last_digit by 2 and take the remainders using mod %

	remainder = last_digit % 2 # this will be either 1 or 0 for odd and even respectively

	# since 1 can be said True, and 0 as False in programming
	if remainder: # if 1 (for odd)
		print("odd")
	else:
		print("even") # 0 can be also called False, so the else case is called