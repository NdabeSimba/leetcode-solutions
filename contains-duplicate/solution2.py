# sorting

class Solution(object):
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True
        return False

self = Solution()

nums = [1,2,3,4]
print(Solution.containsDuplicate(self, nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution.containsDuplicate(self, nums))