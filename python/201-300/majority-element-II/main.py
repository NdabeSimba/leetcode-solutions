class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        nums_dict = dict()
        result = list()

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        cre = len(nums) / 3

        for key in nums_dict:
            if nums_dict[key] > cre:
                result.append(key)

        return result


self = Solution()

nums = [3,2,3]
print(Solution.majorityElement(self, nums))
