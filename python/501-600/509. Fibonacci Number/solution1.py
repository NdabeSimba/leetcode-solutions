class Solution:
    def fib(self, n: int) -> int:
        num1, num2 = 0, 1
        if n == 0:
            return num1
        
        for _ in range(n - 1):
            num1, num2 = num2, num1 + num2
            
        return num2


self = Solution()

n = 0
print(Solution.fib(self, n))

n = 1
print(Solution.fib(self, n))

n = 2
print(Solution.fib(self, n))

n = 3
print(Solution.fib(self, n))

n = 4
print(Solution.fib(self, n))
