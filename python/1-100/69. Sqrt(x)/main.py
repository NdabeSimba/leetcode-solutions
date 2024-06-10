class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            temp = i**2
            if x == 0:
                return 0
            else:
                if temp == x:
                    return i
                elif temp > x:
                    return i - 1
                else:
                    i += 1


self = Solution()

x = 4
print(Solution.mySqrt(self, x))

x = 8
print(Solution.mySqrt(self, x))

x = 0
print(Solution.mySqrt(self, x))
