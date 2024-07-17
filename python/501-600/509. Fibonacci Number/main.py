class Solution:
    def fib(self, n: int) -> int:
        num1, num2 = 0, 1

        for _ in range(n):
            num1, num2 = num2, num1 + num2

        return num1
    
# Bottom-Up DP Technique