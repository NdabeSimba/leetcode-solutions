# two-pass hash table

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if ((target-num) in table) and (i != table[(target-num)]):
                return [i, table[(target-num)]]


nums = [2, 7, 11, 15]
target = 22
self = Solution()
print(Solution.twoSum(self, nums, target))