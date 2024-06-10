

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[value] = i


nums = [2, 7, 11, 15]
target = 18
self = Solution()
print(Solution.twoSum(self, nums, target))
