# https://dimikoj.com/problems/7/count-numbers

# Process 1 (the valid one)
import re
# This program will use regular expression. If you don't know what it is, you should start learning this
# We will use \d+ pattern to find all the numerical values
# regex is C optimized, so its really fast

pattern = re.compile(r"\d+") # compiling the patten to use later, if wasn't compiled, every time any regex is ran, it'll be compiled/look into cache (time expensive)
for T in range(int(input())):
	print(len(pattern.findall(input()))) # finds a list of numbers, then prints the len

# Process 2 (the cheating way, won't work here)
"""
# since we are doing online competition, the will be only numbers and spaces. each number is separated by a space (however this question said there can be multiple, so following process won't work)
# so 1 2 3 has 2 spaces, so 2+1 = 3 numbers
# so if we count the spaces, then we can solve it
# why its a cheat, because we are guaranteed there won't be multiple spaces and any Alphabets.

for T in range(int(input())):
	print(input().count(" ") + 1)
"""

# Process 3 (A safe way to process, will work)
"""
# we will check character by character,
# every time we hit a " ", and there is no space next to it, we keep adding 1, because there might be multiple spaces
# once we hit the end, we will add an extra 1, because last number doesn't has a space after it

for T in range(int(input())):
	txt = input()
	nums = 0
	l = len(txt)

	for n in range(l):
		if n != l-1 and txt[n]==" " and txt[n+1]!=" ":
			nums += 1
		# WHY are we checking n != l-1 (n is not the last number) at 1st of the if statement
		# >> Because if we hit the end of string and check for a item beyond its limit (here txt[n+1]), it will raise Error.

	nums += 1 # for the last number

	print(nums)
"""