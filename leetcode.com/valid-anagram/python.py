# https://leetcode.com/problems/valid-anagram/

from collections import Counter

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		cs = Counter(s)
		ts = Counter(t)
		
		return cs == ts
		


class AltSolution:
	def isAnagram(self, s: str, t: str) -> bool:
		return sorted(t) == sorted(s)
	