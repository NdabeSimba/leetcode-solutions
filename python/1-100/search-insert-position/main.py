class Solution:
    def searchInsert(self, nums, target: int) -> int:
        count = 0
        for num in nums:
            if num >= target:
                break
            else:
                count += 1
        return count


self = Solution()

nums = [1, 3, 5, 6]
target = 5
print(Solution.searchInsert(self, nums, target))

nums = [1, 3, 5, 6]
target = 7
print(Solution.searchInsert(self, nums, target))
