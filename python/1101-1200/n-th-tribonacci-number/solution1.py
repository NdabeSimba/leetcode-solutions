class Solution:
    def tribonacci(self, n: int) -> int:
        num1, num2, num3 = 0, 1, 1
        result = [0, 1, 1]

        if n <= 2:
            return result[n]

        for _ in range(3, n + 1):
            num1, num2, num3 = num2, num3, num1 + num2 + num3
        
        return num3


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