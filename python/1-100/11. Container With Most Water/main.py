class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0

        while l < r:
            result = max(result, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result


self = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution.maxArea(self, height))

height = [1, 1]
print(Solution.maxArea(self, height))
