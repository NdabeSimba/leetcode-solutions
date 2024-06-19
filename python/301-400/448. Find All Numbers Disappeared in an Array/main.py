class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        result = []
        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                result.append(num)
        
        return result