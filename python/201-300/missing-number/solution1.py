class Solution:
    def missingNumber(self, nums) -> int:
        try:
            for i in range(len(nums) + 1):
                nums.remove(i)
        except:
            return i


self = Solution()

nums1 = [3,0,1]
print(Solution.missingNumber(self, nums1))

nums1 = [0,1]
print(Solution.missingNumber(self, nums1))

nums1 = [9,6,4,2,3,5,7,0,1]
print(Solution.missingNumber(self, nums1))
