class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]