# Title: Add Binary
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a, b):
        int_a = int(a,2)
        int_b = int(b,2)
        total_int = int_a + int_b
        return bin(total_int)[2:]