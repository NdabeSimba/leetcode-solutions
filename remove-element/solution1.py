class Solution(object):
    def removeElement(nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

nums = [3,2,2,3]
val = 3
print(Solution.removeElement(nums, val), nums[:Solution.removeElement(nums, val)-1])