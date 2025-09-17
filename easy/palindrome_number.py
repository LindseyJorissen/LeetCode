# Title: Palindrome Number
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x):
        return str(x) == ''.join(reversed(str(x)))