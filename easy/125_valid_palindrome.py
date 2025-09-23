# Title: Valid Palindrome
            # Difficulty: Easy
            # Language: Python
            # Link:https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s):
        letters = ''.join(ch.lower() for ch in s if ch.isalnum())
        return letters == letters[::-1]
