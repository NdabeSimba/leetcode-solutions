class Solution(object):
    def removeDuplicates(self, nums):
        replace = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace


self = Solution()

nums = [1,1,2]
print(Solution.removeDuplicates(self,nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(self, nums))
