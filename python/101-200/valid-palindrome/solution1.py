class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""
        for i in s.lower():
            if i.isalnum() == True:
                palin = palin + i
        return palin == palin[::-1]


self = Solution()

s = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(self, s))

s = "0P"
print(Solution.isPalindrome(self, s))

s = " "
print(Solution.isPalindrome(self, s))
