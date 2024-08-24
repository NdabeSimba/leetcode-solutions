class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            temp = self.myPow(x, n // 2)
            temp = temp * temp

            if n % 2 == 1:
                return temp * x
            
            return temp
        
        if n < 0:
            return 1 / calc(x, -n)
        else:
            return calc(x, n)