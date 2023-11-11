# https://dimikoj.com/problems/7/count-numbers

import re

pattern = re.compile(r"\d+")
for T in range(int(input())):
	print(len(pattern.findall(input())))