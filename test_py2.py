class Solution:
    def rob(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return max(nums)
        else:
            dp = [0] * length
            dp[0] = nums[0]
            dp[1] = nums[1]
    
            for i in range(2, length):
                dp[i] = nums[i] + max(dp[i - 3], dp[i - 2])
                
            return max(dp[-2], dp[-1])
        


self = Solution()

nums = [0]
print(Solution.rob(self, nums))

nums = [2,7,9,3,1]
print(Solution.rob(self, nums))

nums = [2,5,7,8,5,3,4,7,9,6,4,3]
print(Solution.rob(self, nums))