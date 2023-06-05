class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[(i + 1)]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[-1]]
        return result


s = "XIV"
self = Solution()
print(Solution.romanToInt(self, s))