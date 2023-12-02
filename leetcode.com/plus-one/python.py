# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		for n in range(len(digits) -1, -1, -1):
			x = digits[n] + 1

			if x<10:
				digits[n] = x
				return digits
			
			digits[n] = 0
			
		digits.insert(0, 1)
		return digits

			