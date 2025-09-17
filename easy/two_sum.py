# Title: Two Sum
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self,nums,target):
        tested = {}
        for i,num in enumerate(nums):
            if target - num in tested:
                return [tested[target-num],i]
            else:
                tested[num] = i