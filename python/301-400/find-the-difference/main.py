class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = 0

        for i in s:
            s_sum += ord(i)

        for j in t:
            t_sum += ord(j)

        result = t_sum - s_sum
        return chr(result)


self = Solution()

s = "abc"
t = "abcd"
print(Solution.findTheDifference(self, s, t))
