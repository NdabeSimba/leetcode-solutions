class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


self = Solution()

nums = [1, 3, 5, 6]
target = 5
print(Solution.searchInsert(self, nums, target))

nums = [1, 3, 5, 6]
target = 7
print(Solution.searchInsert(self, nums, target))
