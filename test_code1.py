class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while True:
            if len(nums) <= i:
                break
            print(i)
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
        
        print(nums)

self = Solution()

nums = [0,1,0,3,12]
Solution.moveZeroes(self, nums)