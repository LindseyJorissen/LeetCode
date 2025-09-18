# Title: Happy Number
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n):
        while n != 1 and n != 4:
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1