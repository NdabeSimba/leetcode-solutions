class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num = 0

        for i in range(len(nums)):
            if nums[num] == 0:
                nums.append(nums.pop(num))
            else:
                num += 1
