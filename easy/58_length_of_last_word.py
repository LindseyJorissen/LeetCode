# Title: Length of Last Word
            # Difficulty: Easy
            # Language: Python
            # Link:https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        last_word = s.rfind(" ")+1
        return len(s[last_word::])