class Solution:
    def majorityElement(self, nums) -> int:
        return sorted(nums)[len(nums) // 2]
    

self = Solution()

nums = [3,3,4]
print(Solution.majorityElement(self, nums))

nums = [2,2,1,1,1,2,2]
print(Solution.majorityElement(self, nums))