class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1

        return -1
    
self = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(Solution.search(self, nums, target))

nums = [-1,0,3,5,9,12]
target = 2

print(Solution.search(self, nums, target))