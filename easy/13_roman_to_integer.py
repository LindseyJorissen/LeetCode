# Title: Roman to Integer
            # Difficulty: Easy
            # Language: Python
            # Link: https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s):
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        previous_value = 0

        for i in reversed(s):
            value = roman_numerals[i]
            if value < previous_value:
                total -= value
            else:
                total += value
            previous_value = value

        return total