# Title: Remove Element
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums, val):
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k