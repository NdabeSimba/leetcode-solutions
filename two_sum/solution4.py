# one-pass hash table

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [table[complement], i]
            else:
                table[num] = i


nums = [2, 7, 11, 15]
target = 26
self = Solution()
print(Solution.twoSum(self, nums, target))
