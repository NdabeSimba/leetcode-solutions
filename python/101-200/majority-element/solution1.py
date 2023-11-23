class Solution:
    def majorityElement(self, nums) -> int:
        num_dict = dict()

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        con_dict = {v : k for k, v in num_dict.items()}

        return con_dict.get(max(con_dict.keys()))
    

self = Solution()

nums = [3,3,4]
print(Solution.majorityElement(self, nums))

nums = [2,2,1,1,1,2,2]
print(Solution.majorityElement(self, nums))