class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        result = 0
        prev_val = 0

        for sym in s[::-1]:
            if roman_val[sym] < prev_val:
                result -= roman_val[sym]
            else:
                result += roman_val[sym]
                prev_val = roman_val[sym]

        return result