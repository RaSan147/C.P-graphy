# https://dimikoj.com/problems/7/count-numbers

import re

for T in range(int(input())):
	print(len(re.findall(r"\d+", input())))