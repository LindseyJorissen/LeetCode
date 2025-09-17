# Title: Contains Duplicate
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False