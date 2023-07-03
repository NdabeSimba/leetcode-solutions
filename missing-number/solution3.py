class Solution:
    def missingNumber(self, nums) -> int:
        # initialize missing_num to n
        missing_num = len(nums)

        # loop through the array nums
        for i, num in enumerate(nums):
            # perform XOR operation with index and element
            missing_num ^= i ^ num

        # return the missing number
        return missing_num


self = Solution()

nums1 = [3, 0, 1]
print(Solution.missingNumber(self, nums1))

nums1 = [0, 1]
print(Solution.missingNumber(self, nums1))

nums1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution.missingNumber(self, nums1))
