class Solution:
    def rob(self, nums) -> int:
        sum1, sum2 = 0, 0

        for n in nums:
            temp = max(n + sum1, sum2)
            sum1 = sum2
            sum2 = temp

        return sum2
    
self = Solution()

nums = [0]
print(Solution.rob(self, nums))

nums = [2,7,9,3,1]
print(Solution.rob(self, nums))

nums = [2,5,7,8,5,3,4,7,9,6,4,3]
print(Solution.rob(self, nums))