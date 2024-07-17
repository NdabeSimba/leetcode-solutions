from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        hashmap = [0] * (n+1)

        for per1, per2 in trust:
            hashmap[per1] -= 1
            hashmap[per2] += 1
        
        for i in range(1, len(hashmap)):
            if hashmap[i] == n-1:
                return i
        
        return -1