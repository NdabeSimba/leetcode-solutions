class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        factor = 1
        for i in range(2, len(nums) + 1):
            factor *= i

        output = [nums]
        for _ in range(factor):
            for place in range(len(nums) - 1):
                nums[place], nums[place - 1] = nums[place - 1], nums[place]
                output.append(nums)
        
        return output


self = Solution()

nums = [1,2,3]
print(Solution.permute(self, nums))
