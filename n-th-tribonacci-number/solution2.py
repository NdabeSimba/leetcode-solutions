class Solution:
    def tribonacci(self, n: int) -> int:
        tri = {0 : 0, 1 : 1, 2 : 1}
        for i in range(3, n + 1):
            tri[i] = tri[i - 3] + tri[i - 2] + tri[i - 1]
        return tri[n]
    

self = Solution()

n = 0
print(Solution.tribonacci(self, n))

n = 1
print(Solution.tribonacci(self, n))

n = 3
print(Solution.tribonacci(self, n))

n = 4
print(Solution.tribonacci(self, n))

n = 25
print(Solution.tribonacci(self, n))