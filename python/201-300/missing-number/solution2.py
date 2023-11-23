class Solution:
    def missingNumber(self, nums) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


self = Solution()

nums1 = [3, 0, 1]
print(Solution.missingNumber(self, nums1))

nums1 = [0, 1]
print(Solution.missingNumber(self, nums1))

nums1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution.missingNumber(self, nums1))
